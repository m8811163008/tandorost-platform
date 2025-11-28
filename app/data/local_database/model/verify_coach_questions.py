

from enum import StrEnum
from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict

from .verify_coach_question import VerifyCoachQuestion

from .program_enrollment import ExerciseDefinition, ExerciseMetricType, FocusArea
from .trainee_history import ExerciseEquipment

from pydantic import BaseModel, ConfigDict, computed_field


class VerifyCoachQuestions:
    questions: List[VerifyCoachQuestion] = [
        VerifyCoachQuestion(
            question = "V_Q_Question_A",
            correct_answer = "V_Q_Correct_AnswerA",
            wronge_answers= [
                'V_Q_Wronge_AnswerA_A',
                'V_Q_Wronge_AnswerA_B',
            ],
        ),
    ]
