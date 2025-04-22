import datetime
from enum import Enum

from pydantic import  BaseModel, ConfigDict, Field


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

class DataPoint(BaseModel):
    value : ActivityLevel | float
    create_date : datetime.datetime
    model_config = ConfigDict(use_enum_values=True,)

class UserBioData (BaseModel):
    id : str | None = Field(alias="_id", default=None)
    user_id : str
    gender : Gender
    age : int
    height: list[DataPoint]
    weight: list[DataPoint]
    waist_circumference: list[DataPoint]
    arm_circumference: list[DataPoint]
    chest_circumference: list[DataPoint]
    thigh_circumference: list[DataPoint]
    calf_muscle_circumference: list[DataPoint]
    hip_circumference: list[DataPoint]
    activity_level: list[DataPoint]
    model_config = ConfigDict(use_enum_values=True,)



class UserBioDataUpsert (BaseModel):
    gender : Gender | None = None
    age : int | None = None
    height: float | None = None
    weight: float | None = None
    waist_circumference: float | None = None
    arm_circumference: float | None = None
    chest_circumference: float | None = None
    thigh_circumference: float | None = None
    calf_muscle_circumference: float | None = None
    hip_circumference: float | None = None
    activity_level: ActivityLevel | None = None
    model_config = ConfigDict(use_enum_values=True,)
