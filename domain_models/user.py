from domain_models import ObjectId, VerificationCode
from pydantic import  BaseModel, Field


class UserInDB(BaseModel):
    id : ObjectId | None = Field(alias="_id", default= None)
    phone_number: str
    full_name: str | None = None
    language: str = 'en'
    hashed_password: str | None = None
    verification_code: VerificationCode | None = None
    is_enabled : bool = False




    