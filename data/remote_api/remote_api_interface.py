from abc import ABC, abstractmethod
from data.remote_api import VerifyPhoneNumberDetail


class RemoteApiInterface(ABC):
    # Users methods
    @abstractmethod
    async def send_verification_code(self, detail : VerifyPhoneNumberDetail):
        """Verify phone number."""
        pass
    
    # Ai methods    
    @abstractmethod
    async def read_foods_nutritions_by_text(self, foods : str):
        pass