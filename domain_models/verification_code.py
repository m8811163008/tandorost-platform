from pydantic import  BaseModel

class VerificationCode(BaseModel):
    created_at: str | None = None
    verification_code : int