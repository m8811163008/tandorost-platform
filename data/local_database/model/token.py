
from pydantic import  UUID4, BaseModel, Field, ConfigDict, field_serializer
from uuid import uuid4
class Token(BaseModel):
    id : UUID4 = Field(alias="_id", default= uuid4())
    user_id : UUID4
    access_token: str
    token_type: str
    model_config = ConfigDict(use_enum_values=True,
                              arbitrary_types_allowed = True
                              )
    @field_serializer('id')
    def serialize_id(self, id: UUID4) -> str:
        return str(id)
    
    @field_serializer('user_id')
    def serialize_user_id(self, id: UUID4) -> str:
        return str(id)

class TokenData(BaseModel):
    username: str | None = None

