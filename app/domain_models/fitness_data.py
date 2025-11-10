
from pydantic import BaseModel, computed_field

from domain_models.bmi_level import BmiLevel

class FitnessData(BaseModel):
    resting_metabolic_rate :float
    total_daily_energy_expenditure : float
    bmi : float
    waist_circumference_to_height_ratio : float | None
    is_waist_circumference_to_height_ratio_safe : bool | None
    is_waist_circumference_safe_range : bool | None

    @computed_field
    @property
    def bmi_prime(self) -> float:
        return self.bmi / 25
    
    @computed_field
    @property
    def bmi_level(self) -> BmiLevel:
        if self.bmi < 18.5:
            return BmiLevel.UNDERWEIGHT
        elif 18.5 <= self.bmi < 25.0:
            return BmiLevel.HEALTHY_WEIGHT
        elif 25.0 <= self.bmi < 30.0:
            return BmiLevel.OVERWEIGHT
        elif 30.0 <= self.bmi < 35.0:
            return BmiLevel.OBESE_CLASS_ONE
        elif 35.0 <= self.bmi < 40.0:
            return BmiLevel.OBESE_CLASS_TWO
        else:
            return BmiLevel.OBESE_CLASS_THREE
    




    