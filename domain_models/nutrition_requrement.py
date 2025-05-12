from pydantic import BaseModel
class NutritionRequerment(BaseModel):
    # Grams per person
    fat : int
    protein : int
    carbohydrate_fruits_or_non_starchy_vegetables: int
    carbohydrate_other : int

class NutritionRequerments(BaseModel):
    rest_day: NutritionRequerment
    training_day : NutritionRequerment



