from uuid import uuid4
from domain_models.verification_code import VerificationCode
from pydantic import  UUID4, BaseModel, Field,ConfigDict

class Address(BaseModel):
    address_lines : str | None = None
    address_lines2 : str | None = None
    city :str | None = None
    state : str | None = None
    postcode : str | None = None
    country : str | None = None

class UserInDB(BaseModel):
    id : UUID4 = Field(alias="_id", default= uuid4(), exclude= True)
    phone_number: str
    address : Address | None = None
    full_name: str | None = None
    language: str = 'en'
    hashed_password: str | None = None
    verification_code: VerificationCode | None = None
    is_verified : bool = False
    model_config = ConfigDict(use_enum_values=True,
                            arbitrary_types_allowed = True
                            )






    