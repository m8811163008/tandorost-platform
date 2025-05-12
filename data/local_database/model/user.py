
from data.common_data_model.language import Language
from data.local_database.model.change_weight_speed import ChangeWeightSpeed
from domain_models.verification_code import VerificationCode
from pydantic import  BaseModel, Field,ConfigDict, field_serializer, field_validator


class Address(BaseModel):
    address_lines : str | None = None
    address_lines2 : str | None = None
    city :str | None = None
    state : str | None = None
    postcode : str | None = None
    country : str | None = None


class UserInDB(BaseModel):
    id : str | None = Field(alias="_id", default=None)
    phone_number: str
    address : Address | None = None
    full_name: str | None = None
    language: Language = Language.ENGLISH
    hashed_password: str | None = None
    verification_code: VerificationCode | None = None
    is_verified : bool = False
    change_weight_speed : ChangeWeightSpeed = ChangeWeightSpeed.CONSTANT
    model_config = ConfigDict(use_enum_values=True)

    @field_serializer("changeWeightSpeed")
    def serialize_change_weight_speed(self, value: ChangeWeightSpeed) -> dict[str, float]:
        # Serialize the ChangeWeightSpeed enum into a dictionary
        return value.value.model_dump()


    @field_validator("changeWeightSpeed", mode="before")
    def validate_change_weight_speed(cls, value: dict[str, float]) -> ChangeWeightSpeed:
        # Convert a dictionary back into a ChangeWeightSpeed enum
        for enum_member in ChangeWeightSpeed:
            if enum_member.value.model_dump() == value:
                return enum_member
        raise ValueError(f"Invalid value for ChangeWeightSpeed: {value}")
        
    