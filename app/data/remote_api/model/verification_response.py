from pydantic import BaseModel


class VerificationResponse(BaseModel):
    is_verified: bool