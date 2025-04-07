
from pydantic import  BaseModel, Field

from domain_models.pydantic_object_id import ObjectId

class Token(BaseModel):
    id : ObjectId | None = Field(alias="_id", default= None)
    user_id : ObjectId
    access_token: str
    token_type: str
    


class TokenData(BaseModel):
    username: str | None = None

