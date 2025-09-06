
from typing import Any
import httpx
from data.common_data_model.language import Language
from data.remote_api import SMSPanelCongif, VerifyPhoneNumberDetail, NetworkConnectionError
from data.remote_api.model.ai_model_cache import CacheModel
from data.remote_api.model.email_config import EmailDetail, EmailSMTPCongif
from data.remote_api.model.exceptions import *
from data.remote_api.model.food_ai_model import UserRequestedFood
from data.remote_api.model.gemini_config import  GeminiConfig
from data.remote_api.remote_api_interface import RemoteApiInterface
from google import genai # type: ignore
from google.genai import types # type: ignore
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


verify_end_point_uri = 'https://api.payamak-panel.com/post/Send.asmx/SendByBaseNumber'

class RemoteApiImpl(RemoteApiInterface):
    def __init__(self, sms_config : SMSPanelCongif,email_config : EmailSMTPCongif, ai_config : GeminiConfig ):
        self.sms_config = sms_config
        self.email_config = email_config
        self.ai_config = ai_config
        self.ai_client = genai.Client(api_key= self.ai_config.api_key)
                
        
    async def send_sms_verification_code(self, detail : VerifyPhoneNumberDetail):
        payload: dict[str, Any] = {}
        payload.update(self.sms_config.model_dump())
        payload.update(detail.model_dump(exclude={'text'}))
        
        # Add repeated `text` keys for each message
        text_payload = [("text", message) for message in detail.text]
        payload.update(text_payload)
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(verify_end_point_uri, headers={"Content-Type": "application/x-www-form-urlencoded"}, data=payload)
                if response.status_code != 200:
                    response.raise_for_status()
            except Exception as e:
                print(e)
                raise NetworkConnectionError()   # Handle the response
            finally:
                await client.aclose()
                
    async def send_email_verification_code(self, detail : EmailDetail):
        sender_email = self.email_config.username
        sender_password = self.email_config.appPassword

        message = MIMEMultipart()
        message["From"] = detail.sender_email
        message["To"] = detail.recipient_email
        message["Subject"] = detail.subject
        body = detail.body
        #TODO add html body
        message.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP_SSL(self.email_config.host, self.email_config.port) as server:
                server.login(sender_email, sender_password)
                server.sendmail(detail.sender_email, detail.recipient_email, message.as_string())
        except Exception as e:
            print(e)
            raise NetworkConnectionError()

    
    async def read_foods_nutritions_by_text(self, foods : str) -> UserRequestedFood:
        return await self._read_foods_nutritions(contents = [foods])
        
    async def read_foods_nutritions_by_voice(self, foods : bytes,meme_type: str , language : Language) -> UserRequestedFood:
        return await self._read_foods_nutritions(contents=[
                    f'Input is audio and the user spoken language is : {language}',
                    types.Part.from_bytes(
                    data=foods,
                    mime_type=meme_type,
                    )
                ],)
        

    async def _read_foods_nutritions(self, contents: list[Any], current_model_index:int =0) -> UserRequestedFood:
        # Todo recursively use models
        try: 
            response = self.ai_client.models.generate_content(  # type: ignore
                model=self.ai_config.models[current_model_index],
                contents=contents,
                config = types.GenerateContentConfig(
                    # cached_content=self._context_caching.name,
                    system_instruction= CacheModel.system_instruction(),
                    temperature=0.0,
                    top_k = 1,
                    response_mime_type = 'application/json',
                    response_schema =  UserRequestedFood,
                )
            )
        except (InvalidArgumentError,FailedPreconditionError,PermissionDeniedError, NotFoundError,InternalError, ServiceUnavailableError, DeadlineExceededError) as e :
            raise e
        except ResourceExhaustedError as e:
            # recursively use models
            if current_model_index < len(self.ai_config.models):
                # TODO save model index to use
                current_model_index = current_model_index + 1
                return await self._read_foods_nutritions(contents = contents, current_model_index =current_model_index)
            else: 
                raise e
        except Exception as e:
            raise e
        
        try:
            if response.text is None:
                raise ParameterError()
            
            food_dict = json.loads(response.text)
            return UserRequestedFood(**food_dict)
        
        except json.JSONDecodeError:
            raise ParameterError()
        

        
    @property
    def _context_caching(self):
        # Create a cache with a 3 days TTL
        return self.ai_client.caches.create(
            model=self.ai_config.models[0],
            config=types.CreateCachedContentConfig(
                display_name='food_cache', # used to identify the cache
                system_instruction= CacheModel.system_instruction(),
                ttl=f"{60 * 60 * 72}s",
            )
        )


