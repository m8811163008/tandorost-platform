from enum import Enum

from pydantic import UUID4, BaseModel, ConfigDict, Field
from uuid import uuid4

class Gender(Enum):
    MALE = 'male'
    FEMALE = 'female'

class ActivityLevel(Enum):
    SEDENTARY = 'sedentary'
    FAIRLY_ACTIVE = 'fairyActive'
    MODERATELY_ACTIVE = 'moderatelyActive'
    ACTIVE = 'active'
    VERY_ACTIVE = 'veryActive'
    OTHER = 'other'

class BodyComposition(BaseModel):
    height: list[float]
    weight: list[float]
    waist_circumference: list[float]
    arm_circumference: list[float]
    chest_circumference: list[float]
    thigh_circumference: list[float]
    calf_muscle_circumference: list[float]
    hip_circumference: list[float]
    activity_level: list[ActivityLevel]
    model_config = ConfigDict(use_enum_values=True,
                              )

class UserBioData (BaseModel):
    id : UUID4 = Field(alias="_id", default= uuid4() , exclude= True)
    user_id : UUID4
    gender : Gender
    age : int
    body_composition : BodyComposition
    model_config = ConfigDict(use_enum_values=True,
                              arbitrary_types_allowed = True
                              )

