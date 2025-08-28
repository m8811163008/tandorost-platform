
from data.common_data_model.language import Language
from data.local_database.model.change_weight_speed import ChangeWeightSpeed
from data.local_database.model.roles import Role
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
    phone_number: str | None = None
    email: str | None = None
    address : Address | None = None
    full_name: str | None = None
    language: Language = Language.ENGLISH
    hashed_password: str | None = None
    verification_code: VerificationCode | None = None
    is_phone_number_verified : bool = False
    is_email_verified : bool = False
    #TODO move change_weight_speed and  is_time_restricted_eating to user_physical_data_collection
    change_weight_speed : ChangeWeightSpeed = ChangeWeightSpeed.CONSTANT
    is_time_restricted_eating : bool = False
    role : list[Role] = [Role.TRAINER]
    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)


    
        
    