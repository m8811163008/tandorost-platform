from pydantic import BaseModel
from data.local_database.model.user import Address
from domain_models.data_models import Language

class UserUpdateRequest(BaseModel):
    phone_number: str
    address : Address | None = None
    full_name: str | None = None
    language: Language = Language.ENGLISH