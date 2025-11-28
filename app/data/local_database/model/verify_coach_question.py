

from enum import StrEnum
from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict

from .program_enrollment import ExerciseDefinition, ExerciseMetricType, FocusArea
from .trainee_history import ExerciseEquipment

from pydantic import BaseModel, ConfigDict, computed_field



class VerifyCoachQuestion(BaseModel):
    question : str
    correct_answer : str 
    wronge_answers : list[str] 

    
    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)
