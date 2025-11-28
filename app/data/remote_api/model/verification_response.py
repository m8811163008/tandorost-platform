from pydantic import BaseModel


class VerificationResponse(BaseModel):
    is_verified: bool
    reject_reason : None | str = None