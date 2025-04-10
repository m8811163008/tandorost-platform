from pydantic import  BaseModel

class VerificationCode(BaseModel):
    created_at: str
    verification_code : str