from abc import ABC, abstractmethod
from data.common_data_model.language import Language
from data.remote_api import VerifyPhoneNumberDetail
from data.remote_api.model.email_config import EmailDetail
from data.remote_api.model.food_ai_model import  UserRequestedFood


class RemoteApiInterface(ABC):
    # Users methods
    @abstractmethod
    async def send_sms_verification_code(self, detail : VerifyPhoneNumberDetail):
        """Verify phone number."""
        pass
    
    @abstractmethod
    async def send_email_verification_code(self, detail : EmailDetail):
        """Verify phone number."""
        pass

    
    # Ai methods    
    @abstractmethod
    async def read_foods_nutritions_by_text(self, foods : str) -> UserRequestedFood:
        pass

    @abstractmethod
    async def read_foods_nutritions_by_voice(self, foods : bytes,meme_type: str, language : Language) -> UserRequestedFood:
        pass
    
    
    @abstractmethod
    async def verifyByAi(self, fileBytes : bytes,meme_type: str, language : Language):
        pass
