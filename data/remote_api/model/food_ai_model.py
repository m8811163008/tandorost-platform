from enum import StrEnum
from typing import List

from pydantic import BaseModel, ConfigDict

from data.common_data_model.language import Language





class MacroNutritionPerUnitOfMeasurement(BaseModel):
    fat: float
    carbohydrate: float
    protein: float

class CarbohydrateSource(StrEnum):
    FRUITS_OR_NON_STARCHY_VEGETABLES = 'fruits_or_non_starchy_vegetables'
    OTHERS = 'others'

    def is_fruit_or_non_starchy_vegetable(self) -> bool:
        return self == CarbohydrateSource.FRUITS_OR_NON_STARCHY_VEGETABLES

class Ingredient(BaseModel):
    user_language: Language
    user_native_language_ingredient_name: str
    translated_to_english_ingredient_name: str
    unit_of_measurement_native_language: str
    translated_to_english_unit_of_measurement: str
    unit_of_measurement_weight : int
    quantity_of_unit_of_measurement: int
    calculated_calorie: int
    total_fat_in_grams : float
    total_carbohydrate_in_grams : float
    total_protein_in_grams : float
    carbohydrate_source: CarbohydrateSource

    model_config = ConfigDict(use_enum_values=True)

class UserRequestedFood(BaseModel):
    ingredients: List[Ingredient]

