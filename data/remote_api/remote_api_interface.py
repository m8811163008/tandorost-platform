from abc import ABC, abstractmethod
from data.remote_api.model.verify_phone_number_config import VerifyPhoneNumberDetail


class RemoteApiInterface(ABC):
    # Users methods
    @abstractmethod
    async def verify_phone_number(self, detail : VerifyPhoneNumberDetail):
        """Verify phone number."""
        pass