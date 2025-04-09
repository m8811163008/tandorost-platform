from domain_models.pydantic_object_id import ObjectId
from pydantic import  BaseModel, Field

from domain_models.verification_code import VerificationCode

class User(BaseModel):
    username: str
    full_name: str | None = None


class UserInDB(User):
    id : ObjectId | None = Field(alias="_id", default= None)
    hashed_password: str | None = None
    verification_code: VerificationCode | None = None
    is_enabled : bool = False