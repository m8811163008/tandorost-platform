from uuid import UUID
from pydantic import BaseModel, Field

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    id : UUID | None = Field(alias="_id", default=None)
    hashed_password: str
