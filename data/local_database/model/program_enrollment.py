import datetime
from enum import StrEnum
from pydantic import BaseModel, ConfigDict, Field
from data.local_database.model.trainee_history import ExerciseEquipment


# =======================================================================
# Section 1: Enumerations
# =======================================================================

class FocusArea(StrEnum):
    """Enumeration for primary muscle groups targeted by an exercise."""
    ARM = 'arm'
    SHOULDER = 'shoulder'
    CHEST = 'chest'
    BACK = 'back'
    LEG = 'leg'
    BUTTOCKS = 'buttocks'
    ABDOMEN = 'abdomen'
    FULL_BODY = 'full_body'


class ExerciseMetricType(StrEnum):
    """
    Enumeration for how an exercise's performance is measured.
    Renamed from 'ExerciseRecordType' for clarity.
    """
    REPS_ONLY = 'reps_only' 
    PERCENT_1RM_AND_REPS = 'percent_1rm_and_reps'  
    TIME_BASED = 'time_based'

# =======================================================================
# Section 2: Core "Library" Models (Referenced Documents)
# =======================================================================

class ExerciseDefinition(BaseModel):
    """
    Represents the blueprint for an exercise.

    This model stores static, reusable information about a single exercise,
    such as its name, instructions, and target muscle groups. It should be
    stored in its own collection and referenced by its ID in other documents.
    """
    id: str | None = Field(alias="_id", default=None)
    title: str
    video_url: str | None = None
    thumb_image_url: str | None = None
    cover_image_url: str | None = None
    preparation_steps: list[str]  
    execution_steps: list[str]  
    key_tips: list[str]
    focus_areas: list[FocusArea]  
    equipment: ExerciseEquipment 
    metric_type: ExerciseMetricType 

    model_config = ConfigDict(
        use_enum_values=True,
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "title": "Barbell Bench Press",
                "preparation_steps": ["Lie flat on the bench.", "Grasp the bar with a medium grip."],
                "execution_steps": ["Lower the bar to your mid-chest.", "Press the bar back up."],
                "key_tips": ["Keep your feet flat on the floor."],
                "focus_areas": ["chest", "shoulder"],
                "equipment": "barbell",
                "metric_type": "percent_1rm_and_reps"
            }
        }
    )


# =======================================================================
# Section 3: Program Structure (Embedded Documents)
# =======================================================================

class RestPeriod(BaseModel):
    """
    Represents a rest period within a workout.

    This is a small, self-contained model intended to be embedded within a list
    of sets or exercises.
    """
    duration_seconds: int 
    note: str | None = None  


class PrescribedExercise(BaseModel):
    """
    Defines a specific exercise prescription within a workout day.

    This model links to an ExerciseDefinition and specifies the target sets,
    reps, duration, or intensity for a trainee. It should be embedded within a WorkoutDay.
    """
    exercise_definition_id: str 
    note: str | None = None  

    # The lists below represent sets. They can contain a number (reps, seconds, %)
    # or a RestPeriod object for rest between sets.
    duration_seconds: list[int | RestPeriod] | None = None
    repetitions: list[int | RestPeriod] | None = None 
    percent_1rm: list[int | RestPeriod] | None = None


class WorkoutDay(BaseModel):
    """
    Represents a single day within a workout program.

    It can either be a rest day or a training day containing a list of exercises
    and inter-exercise rest periods. This model should be embedded within a WorkoutProgram.
    """
    is_rest_day: bool = True
    activities: list[PrescribedExercise | RestPeriod] | None = None 


class WorkoutProgram(BaseModel):
    """
    Represents a complete, structured workout plan.

    This is the top-level object for a workout plan, containing a sequence of
    workout days. It should be stored in its own collection.
    """
    id: str | None = Field(alias="_id", default=None)
    name: str 
    description: str | None = None 
    # "A list of daily workouts. When a program is created, "
    # "this is auto-populated with rest days based on 'coach_program duration_weeks'. "
    # "A coach can then modify individual days by adding exercises."
    days: list[WorkoutDay] 

# =======================================================================
# Section 4: Linking and Logging Models (Referenced Documents)
# =======================================================================

class ProgramEnrollment(BaseModel):
    """
    Links a trainee to a specific workout program assigned by a coach.

    This model acts as a junction table/document, connecting users to the
    programs they are enrolled in. It should be stored in its own collection.
    """
    id: str | None = Field(alias="_id", default=None)
    trainee_id: str
    coach_id: str
    workout_program_id: str 
    enrollment_date: datetime.datetime = Field(default_factory=datetime.datetime.now(datetime.timezone.utc))
    coach_analysis: str | None = None

    model_config = ConfigDict(populate_by_name=True)


class ExerciseLog(BaseModel):
    """
    Records a trainee's actual performance of an exercise on a specific date.
    """
    id: str | None = Field(alias="_id", default=None)
    trainee_id: str 
    exercise_definition_id: str 
    completed_at: datetime.datetime
    # These lists represent the actual performance for each set
    duration_seconds: list[int] | None = None
    repetitions: list[int] | None = None  
    weight_grams: list[int | None] | None = None 

    model_config = ConfigDict(populate_by_name=True)
    