from enum import StrEnum
from pydantic import BaseModel

class ChangeWeightSpeed(StrEnum):
    # The value to reduce from TDEE in diet. 0.1 means reduce 10%
    CONSTANT = 'constant'
    SLOWANDEASY = 'slow_and_easy'
    MEDIUM = 'medium'
    FAST = 'fast'
    FASTANDHARD = 'fast_and_hard'


class EnergyChangeValue(BaseModel):
    rest_day_change_value : float
    training_day_change_value : float

    @classmethod
    def change_weight_speed(cls, change_weight_speed : ChangeWeightSpeed ):
        match change_weight_speed:
            case ChangeWeightSpeed.CONSTANT:
                return EnergyChangeValue(rest_day_change_value= 0, training_day_change_value= 0)
            case ChangeWeightSpeed.SLOWANDEASY:
                return EnergyChangeValue(rest_day_change_value= 0.1, training_day_change_value= 0)
            case ChangeWeightSpeed.MEDIUM:
                return EnergyChangeValue(rest_day_change_value= 0.1, training_day_change_value= 0.05)
            case ChangeWeightSpeed.FAST:
                return EnergyChangeValue(rest_day_change_value= 0.1, training_day_change_value= 0.05)
            case ChangeWeightSpeed.FASTANDHARD:
                return EnergyChangeValue(rest_day_change_value= 0.15, training_day_change_value= 0.15)
            case _:
                raise Exception('not defined ChangeWeightSpeed')






