
from data.common_data_model.language import Language
from domain_models.verification_code import VerificationCode
from pydantic import  BaseModel, Field,ConfigDict


class Address(BaseModel):
    address_lines : str | None = None
    address_lines2 : str | None = None
    city :str | None = None
    state : str | None = None
    postcode : str | None = None
    country : str | None = None

class UserInDB(BaseModel):
    id : str | None = Field(alias="_id", default=None)
    phone_number: str
    address : Address | None = None
    full_name: str | None = None
    language: Language = Language.ENGLISH
    hashed_password: str | None = None
    verification_code: VerificationCode | None = None
    is_verified : bool = False
    model_config = ConfigDict(use_enum_values=True)







    