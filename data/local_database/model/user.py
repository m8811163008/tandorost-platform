from data.local_database.model.pydantic_object_id import ObjectId
from domain_models.verification_code import VerificationCode
from pydantic import  BaseModel, Field

class Address(BaseModel):
    address_lines : str | None = None
    address_lines2 : str | None = None
    city :str | None = None
    state : str | None = None
    postcode : str | None = None
    country : str | None = None

class UserInDB(BaseModel):
    id : ObjectId | None = Field(alias="_id", default= None, exclude= True)
    phone_number: str
    address : Address | None = None
    full_name: str | None = None
    language: str = 'en'
    hashed_password: str | None = None
    verification_code: VerificationCode | None = None
    is_verified : bool = False






    