from enum import Enum
from pydantic import BaseModel


class EnergyChangeValue(BaseModel):
    rest_day_change_value : float
    training_day_change_value : float


class ChangeWeightSpeed(Enum):
    # The value to reduce from TDEE in diet. 0.1 means reduce 10%
    CONSTANT = EnergyChangeValue(rest_day_change_value= 0, training_day_change_value= 0)
    SLOWANDEASY = EnergyChangeValue(rest_day_change_value= 0.1, training_day_change_value= 0)
    MEDIUM = EnergyChangeValue(rest_day_change_value= 0.1, training_day_change_value= 0.05)
    FASTANDHARD = EnergyChangeValue(rest_day_change_value= 0.15, training_day_change_value= 0.05)
