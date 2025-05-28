from datetime import datetime, date
from enum import  StrEnum

from pydantic import  BaseModel, ConfigDict, Field


class Gender(StrEnum):
    MALE = 'male'
    FEMALE = 'female'

class ActivityLevel(StrEnum):
    SEDENTARY = 'sedentary'
    FAIRLY_ACTIVE = 'fairy_active'
    MODERATELY_ACTIVE = 'moderately_active'
    ACTIVE = 'active'
    VERY_ACTIVE = 'very_active'
    OTHER = 'other'

    @classmethod
    def multiplier(cls, value: str) -> float:
        multipliers = {
            cls.SEDENTARY.value: 1.2,
            cls.FAIRLY_ACTIVE.value: 1.3,
            cls.MODERATELY_ACTIVE.value: 1.4,
            cls.ACTIVE.value: 1.5,
            cls.VERY_ACTIVE.value: 1.7,
            cls.OTHER.value: 1.0,  # Default multiplier for 'other'
        }
        return multipliers.get(value, 1.0)  # Default to 1.0 if value is not found


class DataPoint(BaseModel):
    data_point_id : str
    value : ActivityLevel | float
    create_date : datetime
    model_config = ConfigDict(use_enum_values=True,)

class UserPhysicalData (BaseModel):
    id : str | None = Field(alias="_id", default=None)
    user_id : str
    gender : Gender
    birthday: datetime
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



class UserPhysicalDataUpsert (BaseModel):
    gender : Gender | None = None
    birthday : date | None = None
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
