from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class ExcersiceGoal(StrEnum):
    LOSE_WEIGHT = 'lose_weight'
    POWER = 'power'
    STRENGTH = 'strength'
    ENDURANCE = 'endurance'
    HYPERTROPHY = 'hypertrophy'
    PREPARE_A_SPORTING_EVENT = 'prepare_a_sporting_event'
    
class ExerciseEquipment(StrEnum):
    BODY_WEIGHT = 'body_weight'
    WEIGHT_MACHINE = 'weight_machine'
    CABLE_MACHINE = 'cable_machine'
    BARBELL = 'barbell'
    DUMBBELL = 'dumbbell'
    BAND = 'band'
    KETTLEBELL = 'kettlebell'
    
class TraineeHistory(BaseModel):
    id : str | None = Field(alias="_id", default=None)
    user_id : str
    illness: str
    inguries: str
    disabilities: str
    sport_training_history: str
    current_practice_frequency_per_week: int
    excersice_goal: list[ExcersiceGoal]
    daily_activity_desc: str | None = None
    exercise_equipment: list[ExerciseEquipment]
    supplements: str | None = None
    coach_analysis : str | None = None
    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)
