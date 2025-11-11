
from datetime import datetime, timedelta, timezone
from random import Random
from typing import Any, Callable


from fastapi import HTTPException, UploadFile, status
from fastapi.responses import JSONResponse

from data.common_data_model.language import Language
from data.local_database import DatabaseInterface, Token, username_type, UsernameType
from data.remote_api import VerifyPhoneNumberDetail, RemoteApiInterface
from data.remote_api.model.email_config import EmailDetail, SenderEmails
from domain_models import InvalidPassword, UsernameAlreadyInUse, UsernameIsInactive, UsernameNotRegisteredYet, InvalidVerificationCode, NetworkConnectionError, HTTPStatusError,VerificationCode,VerificationType, UserInDB
from domain_models.response_model import ErrorResponse
from repositories.auth.utility import create_access_token, get_password_hash,is_valid_password
from utility.envirement_variables import EnvirenmentVariable
from utility.translation_keys import TranslationKeys




class AuthRepository:
    def __init__(self, database: DatabaseInterface, remote_api:RemoteApiInterface, sms_body_id:str):
        self.database = database
        self.remote_api = remote_api
        self.sms_body_id = sms_body_id

    #TODO user name is phone number , in future change to use both email and phone number
    async def save_verification_code(self, identifier : str,  verification_type: VerificationType):
        user_in_db = await self.database.read_user_by_identifier(identifier=identifier)
        
        if user_in_db is None and verification_type.is_forgot_password():
            raise UsernameNotRegisteredYet()
        
        user_type = username_type(username=identifier)
        if user_in_db is not None and verification_type.is_register():
            
            if user_type == UsernameType.PHONENUMBER and user_in_db.is_phone_number_verified:
                raise UsernameAlreadyInUse()
            if user_type == UsernameType.EMAIL and user_in_db.is_email_verified:
                raise UsernameAlreadyInUse()
        
        user_id =  None
        if user_in_db is not None and user_in_db.id is not None:
            user_id = user_in_db.id
        user_in_db_verification_code = None if user_in_db is None else user_in_db.verification_code

        random_code = str(Random().randint(1000, 9999))
        phone_number_verification_code = None if user_in_db_verification_code == None else user_in_db_verification_code.phone_number_verification_code
        email_verification_code = None if user_in_db_verification_code == None else user_in_db_verification_code.email_verification_code
        verification_code = VerificationCode(created_at= datetime.now(timezone.utc).isoformat(),
                                             phone_number_verification_code=random_code if user_type == UsernameType.PHONENUMBER else phone_number_verification_code,
                                             email_verification_code=random_code if user_type == UsernameType.EMAIL else email_verification_code,)
        current_user_phone_number =  None if user_in_db is None else user_in_db.phone_number
        current_is_user_phone_number_verify =  False if user_in_db is None else user_in_db.is_phone_number_verified
        current_user_email =  None if user_in_db is None else user_in_db.email
        current_is_email_verify =  False if user_in_db is None else user_in_db.is_email_verified
    
        user = UserInDB(_id = user_id ,
                        phone_number = identifier if user_type == UsernameType.PHONENUMBER else current_user_phone_number,
                        is_phone_number_verified = False if user_type == UsernameType.PHONENUMBER else current_is_user_phone_number_verify,
                        email = identifier if user_type == UsernameType.EMAIL else current_user_email,
                        is_email_verified = False if user_type == UsernameType.EMAIL else current_is_email_verify,
                        verification_code=verification_code,
                        )
        
        await self.database.upsert_user(user=user)
        

            
    async def send_sms_verification_code(self,username : str,):
        user_in_db = await self.database.read_user_by_identifier(identifier=username)
        try:
            detail = VerifyPhoneNumberDetail(text=[user_in_db.verification_code.phone_number_verification_code],to=username, body_id=self.sms_body_id )
            await self.remote_api.send_sms_verification_code(detail=detail)
        except (HTTPStatusError, NetworkConnectionError, Exception):
            raise NetworkConnectionError()
    
    async def send_email_verification_code(self,username : str,subject:str, body:str):
        user_in_db = await self.database.read_user_by_identifier(identifier=username)
        # update body
        body_with_code = body.format(code = user_in_db.verification_code.email_verification_code)
        
        try:
            detail = EmailDetail(sender_email = SenderEmails.verificationSender, recipient_email=username, subject=subject, body=body_with_code)
            await self.remote_api.send_email_verification_code(detail=detail)
        except Exception:
            raise NetworkConnectionError()
        

    async def verify_by_ai(self,user_id : str,video_gallary_files: UploadFile, user_spoken_language : Language):
        # Todo recursively use models
        try:
            prompt_bytes = await video_gallary_files.read()
            await self.remote_api.verifyByAi(fileBytes= prompt_bytes, meme_type = video_gallary_files.content_type, language=user_spoken_language)
            # return await self._upsert_foods_on_database(user_id = user_id, user_requested_food=user_requested_food, )
        except Exception as e:
            raise e
    
    async def verify_code(self, username:str, verification_code : str, is_register_request : bool = True):
        user = await self.database.read_user_by_identifier(identifier=username)
        if user is None :
            raise UsernameNotRegisteredYet()
        if user.verification_code is None:
            raise UsernameNotRegisteredYet()
        if (user.is_phone_number_verified or user.is_email_verified) and is_register_request:
            raise UsernameAlreadyInUse()
        user_type = username_type(username=username)
        if user_type == UsernameType.PHONENUMBER:
            if user.verification_code.phone_number_verification_code != verification_code:
                raise InvalidVerificationCode()
        if user_type == UsernameType.EMAIL:
            if user.verification_code.email_verification_code != verification_code:
                raise InvalidVerificationCode()


    async def update_user_account(self, password: str, username: str, is_verified: bool = True) -> UserInDB:
        user = await self.database.read_user_by_identifier(identifier=username)
        user_type = username_type(username=username)
        try:
            
            hashed_password = get_password_hash(password=password)
        except Exception as e:
            print(e.__str__())

        if user is None:
            # Registration flow: create new user
            user_data = {
                "hashed_password": hashed_password,
                "verification_code": None,
                "is_phone_number_verified": False,
                "is_email_verified": False,
            }
            if user_type == UsernameType.PHONENUMBER:
                user_data["phone_number"] = username
                user_data["is_phone_number_verified"] = is_verified
            elif user_type == UsernameType.EMAIL:
                user_data["email"] = username
                user_data["is_email_verified"] = is_verified

            user = UserInDB(**user_data)
        else:
            # Update flow: update password and verification status
            user.hashed_password = hashed_password
            if user_type == UsernameType.PHONENUMBER:
                user.is_phone_number_verified = is_verified
            elif user_type == UsernameType.EMAIL:
                user.is_email_verified = is_verified

        return await self.database.upsert_user(user=user)

    async def authenticate(self,username: str, password: str) :
        user = await self.database.read_user_by_identifier(identifier=username)
        if user is None or user.hashed_password is None:
            raise UsernameNotRegisteredYet()
        if user.is_phone_number_verified is False and user.is_email_verified is False:
            raise UsernameIsInactive()
        if is_valid_password(password, user.hashed_password) is False:
            raise InvalidPassword()
    
    async def issue_access_token(self,username: str, access_token_expire_minute: float) -> Token:
        # Todo implement refresh token
        user = await self.database.read_user_by_identifier(identifier=username)
        assert(user is not None and user.id is not None)
        access_token_expires = timedelta(minutes=access_token_expire_minute)

        # Determine scopes based on user roles
        scopes = []
        if hasattr(user, "role"):
            if "trainer" in user.role:
                scopes.append("trainer")
            if "bodybuilding_coach" in user.role:
                scopes.append("coach")


        access_token = create_access_token(
            data={"sub": username,
                  "user_id" : user.id.__str__(),
                  "scopes": scopes
                  }, 
            key = EnvirenmentVariable.SECRET_KEY(),
            algorithm= EnvirenmentVariable.ALGORITHM(),
            expires_delta=access_token_expires
        )
        token_instance = Token(user_id= user.id,access_token=access_token, token_type="bearer")
        tokne_in_db = await self.database.read_token(user_id = user.id)
        if tokne_in_db is not None:
            token_instance.id = tokne_in_db.id
        return await self.database.upsert_token(token = token_instance)
    
    async def logout(self,user_id: str,) -> None:
        return await self.database.delete_token(user_id = user_id)
    
    async def read_user_by_identifier(self, identifier: str):
        return await self.database.read_user_by_identifier(identifier=identifier)
        
        
    async def send_sms_najva(self,numbers : list[str],):
        result = await self.database.save_najva_sms_to_local(numbers=numbers)
        notDuplicatedNumbers = result[0]
        countSavedNumbers = result[1]
        _exception = 0
        for index in range(0, len(result[0])):
            try:
                #save on data base
                detail = VerifyPhoneNumberDetail(text=[str(countSavedNumbers - index)[:2]],to=notDuplicatedNumbers[index], body_id="364791" )
                _exception = notDuplicatedNumbers[index]
                await self.remote_api.send_sms_verification_code(detail=detail)
            except (HTTPStatusError, NetworkConnectionError, Exception) as e:
                print(f"Failed to send number for ${_exception}")
                raise NetworkConnectionError()


async def _handle_food_request(request: Callable[..., Any], **kwargs: Any) -> JSONResponse:
    try:
        foods = await request(**kwargs)    

    # read subscriptions
        user_id = kwargs.get("user_id")
        assert(user_id != None)
        subscriptions = await dm.payment_repo.read_payment_subscription(user_id= user_id)
        # add count to user_ai_requested_foods for the earliest active subscription
        # if there is no active subscription raise Error
        # if foods are zero then return empty list
        
        if(len(foods) != 0):
            active_subscriptions = [s for s in subscriptions if getattr(s, "is_active", False)]
            if not active_subscriptions:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=ErrorResponse(
                        error_detail='TranslationKeys.PERMISSION_DENIED',
                        message=TranslationKeys.PERMISSION_DENIED
                    ).model_dump()
                )
            earliest_subscription = min(active_subscriptions, key=lambda s: getattr(s, "purchase_date", datetime.max))
            earliest_subscription.user_ai_requested_foods = getattr(earliest_subscription, "user_ai_requested_foods", 0) + 1
            await dm.payment_repo.update_payment_subscription(payment_subscription=earliest_subscription)

        return JSONResponse(
            content=[jsonable_encoder(food.model_dump()) for food in foods]
        )   
    except InvalidArgumentError :
        message = TranslationKeys.INVALID_ARGUMENT
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorResponse(
                error_detail='TranslationKeys.INVALID_ARGUMENT',
                message=message
            ).model_dump()
        )
    except FailedPreconditionError :
        message = TranslationKeys.FAILED_PRECONDITION
        raise HTTPException(
            status_code=status.HTTP_412_PRECONDITION_FAILED,
            detail=ErrorResponse(
                error_detail='TranslationKeys.FAILED_PRECONDITION',
                message=message
            ).model_dump()
        )
    except  PermissionDeniedError :
        message = TranslationKeys.PERMISSION_DENIED
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=ErrorResponse(
                error_detail='TranslationKeys.PERMISSION_DENIED',
                message=message
            ).model_dump()
        )
    except  NotFoundError :
        message = TranslationKeys.NOT_FOUND
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ErrorResponse(
                error_detail='TranslationKeys.NOT_FOUND',
                message=message
            ).model_dump()
        )
    except  InternalError :
        message = TranslationKeys.INTERNAL_ERROR
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=ErrorResponse(
                error_detail='TranslationKeys.INTERNAL_ERROR',
                message=message
            ).model_dump()
        )
    except  ServiceUnavailableError :
        message = TranslationKeys.SERVICE_UNAVAILABLE
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=ErrorResponse(
                error_detail='TranslationKeys.SERVICE_UNAVAILABLE',
                message=message
            ).model_dump()
        )
    except  DeadlineExceededError :
        message = TranslationKeys.DEADLINE_EXCEEDED
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail=ErrorResponse(
                error_detail='TranslationKeys.DEADLINE_EXCEEDED',
                message=message
            ).model_dump()
        )
    except  ResourceExhaustedError :
        message = TranslationKeys.RESOURCE_EXHAUSTED
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=ErrorResponse(
                error_detail='TranslationKeys.RESOURCE_EXHAUSTED',
                message=message
            ).model_dump()
        )
    except Exception :
        message = TranslationKeys.SERVICE_UNAVAILABLE
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=ErrorResponse(
                error_detail='TranslationKeys.SERVICE_UNAVAILABLE',
                message=message
            ).model_dump()
        )