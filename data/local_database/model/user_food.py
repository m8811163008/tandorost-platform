import datetime
from enum import StrEnum
from typing import List, Optional

from bcp47 import BCP47 # type: ignore
from pydantic import BaseModel, ConfigDict, Field


class TotalMacroNutritionPerFood(BaseModel):
    fat: float
    carbohydrate: float
    protein: float

class CarbohydrateSourceLD(StrEnum):
    FRUITS_OR_NON_STARCHY_VEGETABLES = 'fruits_or_non_starchy_vegetables'
    OTHERS = 'others'


class Food(BaseModel):
    food_id : str
    upsert_date: datetime.datetime
    user_language: BCP47

    user_native_language_food_name: str
    translated_to_english_food_name : str

    unit_of_measurement_native_language: str
    translated_to_english_unit_of_measurement: str
    calculated_calorie: int

    quantity_of_unit_of_measurement: int

    carbohydrate_source : CarbohydrateSourceLD
    macro_nutrition : TotalMacroNutritionPerFood



class UserFood(BaseModel):
    """
    Represents a food log for a specific user, organized by date.

    This model links a user ID to a collection of food entries (`Food` objects),
    where each entry is associated with the date it was logged or consumed.

    Attributes:
        id (Optional[str]): The database identifier (e.g., MongoDB `_id`).
            Defaults to None. Aliased as `_id` for database compatibility.
        user_id (str): The unique identifier of the user this food log belongs to.
        foods List[Food]: A dictionary where keys are
            datetime objects representing specific dates, and values are lists
            of `Food` objects logged for that date.
    """
    id : Optional[str] = Field(alias="_id", default=None)
    user_id : str
    foods : List[Food]
    model_config = ConfigDict(use_enum_values=True,)