import datetime
from enum import StrEnum
from typing import List, Dict, Optional

from pydantic import BaseModel, ConfigDict, Field

from data.local_database.model.user import Language

class MacroNutritionPerUnitOfMeasurement(BaseModel):
    fat: float
    carbohydrate: float
    protein: float

class CarbohydrateSource(StrEnum):
    FRUITS_OR_NON_STARCHY_VEGETABLES = 'fruits_or_non_starchy_vegetables'
    OTHERS = 'others'


class Food(BaseModel):
    food_id : str
    created_date: datetime.datetime
    updated_date: datetime.datetime
    user_language: Language

    user_native_language_food_name: str
    translated_to_english_food_name : str

    unit_of_measurement_native_language: str
    translated_to_english_unit_of_measurement: str

    # based on calorie not Kilo calorie per unit of measurement(e.g., an apple might be 70000 cal not 70 kcal)
    calorie_per_unit_of_measurement: int

    # Grams
    weight_per_unit_of_measurement: int
    quantity_of_unit_of_measurement: int

    carbohydrate_source : CarbohydrateSource


    # Grams including water and fibers and macro nutritions and micro nutritions
    @property
    def total_weight(self) -> float:
        """Calculates total weight in grams for the specified quantity."""
        return self.weight_per_unit_of_measurement * self.quantity_of_unit_of_measurement

    @property
    def total_calorie(self) -> float:
        return self.total_weight * self.calorie_per_unit_of_measurement / 1000


class UserFood(BaseModel):
    """
    Represents a food log for a specific user, organized by date.

    This model links a user ID to a collection of food entries (`Food` objects),
    where each entry is associated with the date it was logged or consumed.

    Attributes:
        id (Optional[str]): The database identifier (e.g., MongoDB `_id`).
            Defaults to None. Aliased as `_id` for database compatibility.
        user_id (str): The unique identifier of the user this food log belongs to.
        foods (Dict[datetime.datetime, List[Food]]): A dictionary where keys are
            datetime objects representing specific dates, and values are lists
            of `Food` objects logged for that date.
    """
    id : Optional[str] = Field(alias="_id", default=None)
    user_id : str
    foods : Dict[datetime.datetime, List[Food]]
    model_config = ConfigDict(use_enum_values=True,)