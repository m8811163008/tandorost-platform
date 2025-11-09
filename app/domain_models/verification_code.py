from pydantic import  BaseModel

class VerificationCode(BaseModel):
    created_at: str
    email_verification_code : str | None = None
    phone_number_verification_code : str | None = None