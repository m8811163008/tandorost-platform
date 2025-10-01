from data.local_database.model.program_enrollment import ExerciseDefinition, ExerciseMetricType, FocusArea
from data.local_database.model.trainee_history import ExerciseEquipment

class ExercisesDefinition:
    exercises = [ExerciseDefinition(
        title = '',
        video_url= '',
        thumb_image_url='',
        cover_image_url='',
        preparation_steps=['',''],
        execution_steps=['',''],
        key_tips=['',''],
        focus_areas=[FocusArea.ARM],
        equipment=ExerciseEquipment.BARBELL,
        metric_type=ExerciseMetricType.REPS_ONLY
    )]