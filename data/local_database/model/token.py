
from pydantic import  BaseModel, Field

from data.local_database.model.pydantic_object_id import ObjectId

class Token(BaseModel):
    id : ObjectId | None = Field(alias="_id", default= None)
    user_id : ObjectId
    access_token: str
    token_type: str
    


class TokenData(BaseModel):
    username: str | None = None

