from typing import Any
import httpx
from data.remote_api.remote_api_interface import RemoteApiInterface
from data.remote_api.model.verify_phone_number_config import SMSPanelCongif, VerifyPhoneNumberDetail

verify_end_point_uri = 'https://api.payamak-panel.com/post/Send.asmx/SendByBaseNumber'

class RemoteApiImpl(RemoteApiInterface):
    def __init__(self, config : SMSPanelCongif, ):
        self.config = config
        
        
    async def verify_phone_number(self, detail : VerifyPhoneNumberDetail):
        payload: dict[str, Any] = {}
        payload.update(self.config.model_dump())
        payload.update(detail.model_dump(exclude={'text'}))
        
        # Add repeated `text` keys for each message
        text_payload = [("text", message) for message in detail.text]
        payload.update(text_payload)
        async with httpx.AsyncClient() as client:
            try:
              response = await client.post(verify_end_point_uri, headers={"Content-Type": "application/x-www-form-urlencoded"}, data=payload)
              print(response.content)
            except Exception as e:
                print(e)   # Handle the response
            
            # if response.status_code != 200:
            #     response.raise_for_status()
            await client.aclose()
