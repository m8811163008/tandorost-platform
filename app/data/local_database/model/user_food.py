import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from ...common_data_model.language import Language


class TotalMacroNutritionPerFood(BaseModel):
    fat: float
    carbohydrate: float
    protein: float

class CarbohydrateSourceLD(StrEnum):
    FRUITS_OR_NON_STARCHY_VEGETABLES = 'fruits_or_non_starchy_vegetables'
    OTHERS = 'others'


class Food(BaseModel):
    id : Annotated[ str | None , Field(alias="_id")] = None
    user_id : str
    upsert_date: datetime.datetime
    user_language: Language

    user_native_language_food_name: str
    translated_to_english_food_name : str

    unit_of_measurement_native_language: str
    translated_to_english_unit_of_measurement: str
    calculated_calorie: int

    quantity_of_unit_of_measurement: int

    carbohydrate_source : CarbohydrateSourceLD
    macro_nutrition : TotalMacroNutritionPerFood
    model_config = ConfigDict(use_enum_values=True,populate_by_name=True)


