from enum import Enum

from pydantic import BaseModel, ConfigDict, Field

from data.local_database.model.pydantic_object_id import ObjectId


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
    model_config = ConfigDict(use_enum_values=True)

class UserBioData (BaseModel):
    id : ObjectId | None = Field(alias="_id", default= None, exclude= True)
    user_id : ObjectId
    gender : Gender
    age : int
    body_composition : BodyComposition
    model_config = ConfigDict(use_enum_values=True)
