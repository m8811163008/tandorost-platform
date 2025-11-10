from enum import StrEnum


class BmiLevel(StrEnum): 
  UNDERWEIGHT = 'under_weight'
  HEALTHY_WEIGHT = 'healthy_weight'
  OVERWEIGHT = 'over_weight'
  OBESE_CLASS_ONE = 'obese_class_one'
  OBESE_CLASS_TWO = 'obese_class_two'
  OBESE_CLASS_THREE = 'obese_class_three'
