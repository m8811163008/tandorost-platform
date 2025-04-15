from pydantic import BaseModel
from data.local_database.model.user import Address

class UserUpdateRequest(BaseModel):
    phone_number: str
    address : Address | None = None
    full_name: str | None = None
    language: str = 'en'