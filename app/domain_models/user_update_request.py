from pydantic import BaseModel

from data.local_database.model.user import Address
from domain_models.data_models import Language, ChangeWeightSpeed, Role

class UserUpdateRequest(BaseModel):
    phone_number: str | None= None
    email: str | None= None
    address : Address | None = None
    full_name: str | None = None
    language: Language = Language.ENGLISH
    change_weight_speed : ChangeWeightSpeed  | None = None
    role : list[Role] | None = None
    is_time_restricted_eating : bool | None = None
    finance_card_id : str | None = None