from domain_models import ObjectId, VerificationCode
from pydantic import  BaseModel, Field

class User(BaseModel):
    username: str
    full_name: str | None = None


class UserInDB(User):
    id : ObjectId | None = Field(alias="_id", default= None)
    hashed_password: str | None = None
    verification_code: VerificationCode | None = None
    is_enabled : bool = False