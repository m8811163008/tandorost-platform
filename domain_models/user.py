from domain_models import ObjectId, VerificationCode
from pydantic import  BaseModel, Field

class Address(BaseModel):
    address_lines : str
    city :str
    state : str
    postcode : str
    country : str

class UserInDB(BaseModel):
    id : ObjectId | None = Field(alias="_id", default= None)
    phone_number: str
    address : Address | None = None
    full_name: str | None = None
    language: str = 'en'
    hashed_password: str | None = None
    verification_code: VerificationCode | None = None
    is_active : bool = False






    