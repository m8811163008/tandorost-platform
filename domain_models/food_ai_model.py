from enum import StrEnum
from typing import List

from pydantic import BaseModel, ConfigDict

class UserLanguage(StrEnum):
    EN = 'en'
    FA = 'fa'

class MacroNutritionPerUnitOfMeasurement(BaseModel):
    fat: float
    carbohydrate: float
    protein: float

class CarbohydrateSource(StrEnum):
    FRUITS_OR_NON_STARCHY_VEGETABLES = 'fruits_or_non_starchy_vegetables'
    OTHERS = 'others'

class Food(BaseModel):
    user_language: UserLanguage
    user_native_language_food_name: str
    translated_to_english_food_name: str
    unit_of_measurement_native_language: str
    translated_to_english_unit_of_measurement: str
    calorie_per_unit_of_measurement: int  # Assuming calorie, not kcal
    weight_per_unit_of_measurement: int  # Grams
    quantity_of_unit_of_measurement: int
    carbohydrate_source: CarbohydrateSource

    model_config = ConfigDict(use_enum_values=True)

class UserRequestedFood(BaseModel):
    foods: List[Food]

