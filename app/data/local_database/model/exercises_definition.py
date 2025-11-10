

from enum import StrEnum
from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict

from .program_enrollment import ExerciseDefinition, ExerciseMetricType, FocusArea
from .trainee_history import ExerciseEquipment


class ExercisesDefinition:
    """Container class holding a list of all defined ExerciseDefinition objects."""
    exercises: List[ExerciseDefinition] = [
        ExerciseDefinition(
            id='exercise-1',
            title="E_D_AB_WHEEL_TITLE",
            video_urls=['regular_directory/exercises/videos/ab_wheel.mp4'],
            cover_image_url=['regular_directory/exercises/images/ab_wheel.png'],
            preparation_steps=[
                'E_D_AB_WHEEL_PREP_ONE',
                'E_D_AB_WHEEL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_AB_WHEEL_EXEC_ONE',
                'E_D_AB_WHEEL_EXEC_TWO',
                'E_D_AB_WHEEL_EXEC_THREE'
            ],
            key_tips=[
                'E_D_AB_WHEEL_TIP_ONE',
                'E_D_AB_WHEEL_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN, FocusArea.SHOULDER, FocusArea.BACK],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-2',
            title="E_D_ALTERNATING_PUNCH_TITLE",
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/alternating_punch.png'],
            preparation_steps=[
                'E_D_ALTERNATING_PUNCH_PREP_ONE',
                'E_D_ALTERNATING_PUNCH_PREP_TWO',
                'E_D_ALTERNATING_PUNCH_PREP_THREE'
            ],
            execution_steps=[
                'E_D_ALTERNATING_PUNCH_EXEC_ONE',
                'E_D_ALTERNATING_PUNCH_EXEC_TWO',
                'E_D_ALTERNATING_PUNCH_EXEC_THREE'
            ],
            key_tips=[
                'E_D_ALTERNATING_PUNCH_TIP_ONE',
                'E_D_ALTERNATING_PUNCH_TIP_TWO',
                'E_D_ALTERNATING_PUNCH_TIP_THREE'
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.ARM, FocusArea.CHEST],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-3',
            title="E_D_ALTERNATING_V_UP_BAND_TITLE",
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/alternating_v_up_band.png'],
            preparation_steps=[
                'E_D_ALTERNATING_V_UP_BAND_PREP_ONE',
                'E_D_ALTERNATING_V_UP_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_ALTERNATING_V_UP_BAND_EXEC_ONE',
                'E_D_ALTERNATING_V_UP_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_ALTERNATING_V_UP_BAND_TIP_ONE'
            ],
            focus_areas=[FocusArea.ABDOMEN, FocusArea.LEG],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-4',
            title="E_D_ARM_CIRCLES_TITLE",
            video_urls=['regular_directory/exercises/videos/arm_circles.mp4'],
            cover_image_url=['regular_directory/exercises/images/arm_circles.png'],
            preparation_steps=[
                'E_D_ARM_CIRCLES_PREP_ONE',
                'E_D_ARM_CIRCLES_PREP_TWO'
            ],
            execution_steps=[
                'E_D_ARM_CIRCLES_EXEC_ONE',
                'E_D_ARM_CIRCLES_EXEC_TWO',
                'E_D_ARM_CIRCLES_EXEC_THREE'
            ],
            key_tips=[
                'E_D_ARM_CIRCLES_TIP_ONE',
                'E_D_ARM_CIRCLES_TIP_TWO'
            ],
            focus_areas=[FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-5',
            title="E_D_ARNOLD_PRESS_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/arnold_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/arnold_dumbbell.png'],
            preparation_steps=[
                'E_D_ARNOLD_PRESS_DUMBBELL_PREP_ONE',
                'E_D_ARNOLD_PRESS_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_ARNOLD_PRESS_DUMBBELL_EXEC_ONE',
                'E_D_ARNOLD_PRESS_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_ARNOLD_PRESS_DUMBBELL_TIP_ONE',
                'E_D_ARNOLD_PRESS_DUMBBELL_TIP_TWO',
                'E_D_ARNOLD_PRESS_DUMBBELL_TIP_THREE'
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        ExerciseDefinition(
            id='exercise-6',
            title="E_D_BACK_EXTENSION_TITLE",
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/back_extension.png'],
            preparation_steps=[
                'E_D_BACK_EXTENSION_PREP_ONE',
                'E_D_BACK_EXTENSION_PREP_TWO'
            ],
            execution_steps=[
                'E_D_BACK_EXTENSION_EXEC_ONE',
                'E_D_BACK_EXTENSION_EXEC_TWO'
            ],
            key_tips=[
                'E_D_BACK_EXTENSION_TIP_ONE',
                'E_D_BACK_EXTENSION_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.BUTTOCKS, FocusArea.LEG],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-7',
            title="E_D_BACK_EXTENSION_ON_FLOOR_TITLE",
            video_urls=['regular_directory/exercises/videos/back_extension_on_floor.mp4'],
            cover_image_url=['regular_directory/exercises/images/back_extension_on_floor.png'],
            preparation_steps=[
                'E_D_BACK_EXTENSION_ON_FLOOR_PREP_ONE'
            ],
            execution_steps=[
                'E_D_BACK_EXTENSION_ON_FLOOR_EXEC_ONE',
                'E_D_BACK_EXTENSION_ON_FLOOR_EXEC_TWO'
            ],
            key_tips=[
                'E_D_BACK_EXTENSION_ON_FLOOR_TIP_ONE',
                'E_D_BACK_EXTENSION_ON_FLOOR_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-8',
            title="E_D_BACK_EXTENSION_BAND_TITLE",
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/back_extension_band.png'],
            preparation_steps=[
                'E_D_BACK_EXTENSION_BAND_PREP_ONE',
                'E_D_BACK_EXTENSION_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_BACK_EXTENSION_BAND_EXEC_ONE',
                'E_D_BACK_EXTENSION_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_BACK_EXTENSION_BAND_TIP_ONE',
                'E_D_BACK_EXTENSION_BAND_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-9',
            title="E_D_BACK_EXTENSION_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/back_extension_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/back_extension_machine.png'],
            preparation_steps=[
                'E_D_BACK_EXTENSION_MACHINE_PREP_ONE',
                'E_D_BACK_EXTENSION_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_BACK_EXTENSION_MACHINE_EXEC_ONE',
                'E_D_BACK_EXTENSION_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_BACK_EXTENSION_MACHINE_TIP_ONE',
                'E_D_BACK_EXTENSION_MACHINE_TIP_TWO',
                'E_D_BACK_EXTENSION_MACHINE_TIP_THREE'
            ],
            focus_areas=[FocusArea.BACK],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-10',
            title="E_D_BACKWARD_LUNGE_TITLE",
            video_urls=['regular_directory/exercises/videos/backward_lunge.mp4'],
            cover_image_url=['regular_directory/exercises/images/backward_lunge.png'],
            preparation_steps=[
                'E_D_BACKWARD_LUNGE_PREP_ONE',
                'E_D_BACKWARD_LUNGE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_BACKWARD_LUNGE_EXEC_ONE',
                'E_D_BACKWARD_LUNGE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_BACKWARD_LUNGE_TIP_ONE',
                'E_D_BACKWARD_LUNGE_TIP_TWO',
                'E_D_BACKWARD_LUNGE_TIP_THREE'
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-11',
            title="E_D_BACKWARD_LUNGE_WITH_LEG_LIFT_TITLE",
            video_urls=['regular_directory/exercises/videos/backward_lunge_with_leg.mp4'],
            cover_image_url=['regular_directory/exercises/images/backward_lunge_with_leg.png'],
            preparation_steps=[
                'E_D_BACKWARD_LUNGE_WITH_LEG_LIFT_PREP_ONE'
            ],
            execution_steps=[
                'E_D_BACKWARD_LUNGE_WITH_LEG_LIFT_EXEC_ONE',
                'E_D_BACKWARD_LUNGE_WITH_LEG_LIFT_EXEC_TWO'
            ],
            key_tips=[
                'E_D_BACKWARD_LUNGE_WITH_LEG_LIFT_TIP_ONE',
                'E_D_BACKWARD_LUNGE_WITH_LEG_LIFT_TIP_TWO',
                'E_D_BACKWARD_LUNGE_WITH_LEG_LIFT_TIP_THREE'
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-12',
            title="E_D_BACKWARD_LUNGE_BARBELL_TITLE",
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/backward_lunge_barbell.png'],
            preparation_steps=[
                'E_D_BACKWARD_LUNGE_BARBELL_PREP_ONE',
                'E_D_BACKWARD_LUNGE_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_BACKWARD_LUNGE_BARBELL_EXEC_ONE',
                'E_D_BACKWARD_LUNGE_BARBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_BACKWARD_LUNGE_BARBELL_TIP_ONE',
                'E_D_BACKWARD_LUNGE_BARBELL_TIP_TWO',
                'E_D_BACKWARD_LUNGE_BARBELL_TIP_THREE'
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-13',
            title="E_D_BACKWARD_LUNGE_CABLE_TITLE",
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/backward_lunge_cable.png'],
            preparation_steps=[
                'E_D_BACKWARD_LUNGE_CABLE_PREP_ONE',
                'E_D_BACKWARD_LUNGE_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_BACKWARD_LUNGE_CABLE_EXEC_ONE',
                'E_D_BACKWARD_LUNGE_CABLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_BACKWARD_LUNGE_CABLE_TIP_ONE',
                'E_D_BACKWARD_LUNGE_CABLE_TIP_TWO',
                'E_D_BACKWARD_LUNGE_CABLE_TIP_THREE'
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-14',
            title="E_D_BACKWARD_LUNGE_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/backward_lunge_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/backward_lunge_dumbbell.png'],
            preparation_steps=[
                'E_D_BACKWARD_LUNGE_DUMBBELL_PREP_ONE'
            ],
            execution_steps=[
                'E_D_BACKWARD_LUNGE_DUMBBELL_EXEC_ONE',
                'E_D_BACKWARD_LUNGE_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_BACKWARD_LUNGE_DUMBBELL_TIP_ONE',
                'E_D_BACKWARD_LUNGE_DUMBBELL_TIP_TWO',
                'E_D_BACKWARD_LUNGE_DUMBBELL_TIP_THREE'
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-15',
            title="E_D_BACKWARD_LUNGE_KETTLEBELL_TITLE",
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/backward_lunge kettlebell.png'],
            preparation_steps=[
                'E_D_BACKWARD_LUNGE_KETTLEBELL_PREP_ONE',
                'E_D_BACKWARD_LUNGE_KETTLEBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_BACKWARD_LUNGE_KETTLEBELL_EXEC_ONE',
                'E_D_BACKWARD_LUNGE_KETTLEBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_BACKWARD_LUNGE_KETTLEBELL_TIP_ONE',
                'E_D_BACKWARD_LUNGE_KETTLEBELL_TIP_TWO',
                'E_D_BACKWARD_LUNGE_KETTLEBELL_TIP_THREE'
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
            equipment=ExerciseEquipment.KETTLEBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-16',
            title="E_D_BACKWARD_LUNGE_SMITH_MACHINE_TITLE",
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/backward_lunge_smith_machine.png'],
            preparation_steps=[
                'E_D_BACKWARD_LUNGE_SMITH_MACHINE_PREP_ONE',
                'E_D_BACKWARD_LUNGE_SMITH_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_BACKWARD_LUNGE_SMITH_MACHINE_EXEC_ONE',
                'E_D_BACKWARD_LUNGE_SMITH_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_BACKWARD_LUNGE_SMITH_MACHINE_TIP_ONE',
                'E_D_BACKWARD_LUNGE_SMITH_MACHINE_TIP_TWO',
                'E_D_BACKWARD_LUNGE_SMITH_MACHINE_TIP_THREE'
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
            equipment=ExerciseEquipment.SMITH_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-17',
            title="E_D_BALL_SLAMS_TITLE",
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/ball_slams.png'],
            preparation_steps=[
                'E_D_BALL_SLAMS_PREP_ONE',
                'E_D_BALL_SLAMS_PREP_TWO'
            ],
            execution_steps=[
                'E_D_BALL_SLAMS_EXEC_ONE',
                'E_D_BALL_SLAMS_EXEC_TWO',
                'E_D_BALL_SLAMS_EXEC_THREE'
            ],
            key_tips=[
                'E_D_BALL_SLAMS_TIP_ONE',
                'E_D_BALL_SLAMS_TIP_TWO'
            ],
            focus_areas=[FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-18',
            title="E_D_BAND_PULL_THROUGH_TITLE",
            video_urls=['regular_directory/exercises/videos/band_pull_through.mp4'],
            cover_image_url=['regular_directory/exercises/images/band_pull_through.png'],
            preparation_steps=[
                'E_D_BAND_PULL_THROUGH_PREP_ONE',
                'E_D_BAND_PULL_THROUGH_PREP_TWO'
            ],
            execution_steps=[
                'E_D_BAND_PULL_THROUGH_EXEC_ONE',
                'E_D_BAND_PULL_THROUGH_EXEC_TWO',
                'E_D_BAND_PULL_THROUGH_EXEC_THREE'
            ],
            key_tips=[
                'E_D_BAND_PULL_THROUGH_TIP_ONE',
                'E_D_BAND_PULL_THROUGH_TIP_TWO',
                'E_D_BAND_PULL_THROUGH_TIP_THREE',
                'E_D_BAND_PULL_THROUGH_TIP_FOUR'
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.BACK, FocusArea.LEG],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-19',
            title="E_D_BENCH_FLY_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/bench_fly_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/bench_fly_cable.png'],
            preparation_steps=[
                'E_D_BENCH_FLY_CABLE_PREP_ONE',
                'E_D_BENCH_FLY_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_BENCH_FLY_CABLE_EXEC_ONE',
                'E_D_BENCH_FLY_CABLE_EXEC_TWO',
                'E_D_BENCH_FLY_CABLE_EXEC_THREE'
            ],
            key_tips=[
                'E_D_BENCH_FLY_CABLE_TIP_ONE',
                'E_D_BENCH_FLY_CABLE_TIP_TWO',
                'E_D_BENCH_FLY_CABLE_TIP_THREE'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-20',
            title="E_D_BENCH_FLY_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/bench_fly_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/bench_fly_dumbbell.png'],
            preparation_steps=[
                'E_D_BENCH_FLY_DUMBBELL_PREP_ONE',
                'E_D_BENCH_FLY_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_BENCH_FLY_DUMBBELL_EXEC_ONE',
                'E_D_BENCH_FLY_DUMBBELL_EXEC_TWO',
                'E_D_BENCH_FLY_DUMBBELL_EXEC_THREE'
            ],
            key_tips=[
                'E_D_BENCH_FLY_DUMBBELL_TIP_ONE',
                'E_D_BENCH_FLY_DUMBBELL_TIP_TWO',
                'E_D_BENCH_FLY_DUMBBELL_TIP_THREE'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-21',
            title="E_D_BENCH_JUMP_TITLE",
            video_urls=['regular_directory/exercises/videos/bench_jump.mp4'],
            cover_image_url=['regular_directory/exercises/images/bench_jump.png'],
            preparation_steps=[
                'E_D_BENCH_JUMP_PREP_ONE',
                'E_D_BENCH_JUMP_PREP_TWO',
                'E_D_BENCH_JUMP_PREP_THREE'
            ],
            execution_steps=[
                'E_D_BENCH_JUMP_EXEC_ONE',
                'E_D_BENCH_JUMP_EXEC_TWO',
                'E_D_BENCH_JUMP_EXEC_THREE',
                'E_D_BENCH_JUMP_EXEC_FOUR'
            ],
            key_tips=[
                'E_D_BENCH_JUMP_TIP_ONE',
                'E_D_BENCH_JUMP_TIP_TWO',
                'E_D_BENCH_JUMP_TIP_THREE',
                'E_D_BENCH_JUMP_TIP_FOUR'
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-22',
            title="E_D_BENCH_PISTOL_SQUAT_TITLE",
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/bench_pistol_squat.png'],
            preparation_steps=[
                'E_D_BENCH_PISTOL_SQUAT_PREP_ONE',
                'E_D_BENCH_PISTOL_SQUAT_PREP_TWO',
                'E_D_BENCH_PISTOL_SQUAT_PREP_THREE'
            ],
            execution_steps=[
                'E_D_BENCH_PISTOL_SQUAT_EXEC_ONE',
                'E_D_BENCH_PISTOL_SQUAT_EXEC_TWO'
            ],
            key_tips=[
                'E_D_BENCH_PISTOL_SQUAT_TIP_ONE',
                'E_D_BENCH_PISTOL_SQUAT_TIP_TWO',
                'E_D_BENCH_PISTOL_SQUAT_TIP_THREE',
                'E_D_BENCH_PISTOL_SQUAT_TIP_FOUR',
                'E_D_BENCH_PISTOL_SQUAT_TIP_FIVE'
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-24',
            title= "E_D_BENCH_PRESS_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/bench_press_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/bench_press_band.png'],
            preparation_steps=[
                'E_D_BENCH_PRESS_BAND_PREP_ONE', # Lie on a bench and loop a resistance band around your back and hold the ends.
                'E_D_BENCH_PRESS_BAND_PREP_TWO'  # Position your hands shoulder-width apart, elbows bent.
            ],
            execution_steps=[
                'E_D_BENCH_PRESS_BAND_EXEC_ONE',  # Exhale and press the band away from your chest until your arms are fully extended.
                'E_D_BENCH_PRESS_BAND_EXEC_TWO',  # Hold briefly at the top.
                'E_D_BENCH_PRESS_BAND_EXEC_THREE' # Inhale and slowly lower your hands back to the starting position.
            ],
            key_tips=[
                'E_D_BENCH_PRESS_BAND_TIP_ONE', # Keep your feet flat on the floor and maintain a slight arch in your lower back.
                'E_D_BENCH_PRESS_BAND_TIP_TWO' # Control the eccentric (lowering) phase slowly.
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-25',
            title= "E_D_BENCH_PRESS_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/bench_press_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/bench_press_barbell.png'],
            preparation_steps=[
                'E_D_BENCH_PRESS_BARBELL_PREP_ONE', # Lie on a flat bench with your eyes directly under the bar.
                'E_D_BENCH_PRESS_BARBELL_PREP_TWO'  # Grip the bar slightly wider than shoulder-width, unrack the bar.
            ],
            execution_steps=[
                'E_D_BENCH_PRESS_BARBELL_EXEC_ONE',  # Inhale and lower the bar slowly to your mid-chest.
                'E_D_BENCH_PRESS_BARBELL_EXEC_TWO',  # Pause for a moment.
                'E_D_BENCH_PRESS_BARBELL_EXEC_THREE' # Exhale and press the bar back up to the starting position.
            ],
            key_tips=[
                'E_D_BENCH_PRESS_BARBELL_TIP_ONE', # Drive your feet into the ground and keep your shoulders pulled back and down.
                'E_D_BENCH_PRESS_BARBELL_TIP_TWO' # Keep your wrists straight and forearms vertical.
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        ExerciseDefinition(
            id='exercise-26',
            title= "E_D_BENCH_PRESS_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/bench_press_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/bench_press_cable.png'],
            preparation_steps=[
                'E_D_BENCH_PRESS_CABLE_PREP_ONE', # Lie on a flat bench centered between two low cable pulleys.
                'E_D_BENCH_PRESS_CABLE_PREP_TWO'  # Grab the handles with an overhand grip, palms facing forward.
            ],
            execution_steps=[
                'E_D_BENCH_PRESS_CABLE_EXEC_ONE',  # Exhale and push the handles straight up until your arms are fully extended.
                'E_D_BENCH_PRESS_CABLE_EXEC_TWO',  # Squeeze your chest at the top of the movement.
                'E_D_BENCH_PRESS_CABLE_EXEC_THREE' # Inhale and slowly lower the handles back to the starting position.
            ],
            key_tips=[
                'E_D_BENCH_PRESS_CABLE_TIP_ONE', # Focus on controlled movement throughout the entire range of motion.
                'E_D_BENCH_PRESS_CABLE_TIP_TWO' # Keep your core engaged and lower back stable against the bench.
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-27',
            title= "E_D_BENCH_PRESS_CLOSE_GRIP_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/bench_press_close_grip_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/bench_press_close_grip_barbell.png'],
            preparation_steps=[
                'E_D_BENCH_PRESS_CLOSE_GRIP_BARBELL_PREP_ONE', # Lie on a flat bench and take a close, overhand grip on the barbell (about shoulder-width apart).
                'E_D_BENCH_PRESS_CLOSE_GRIP_BARBELL_PREP_TWO'  # Unrack the bar and hold it over your chest with arms fully extended.
            ],
            execution_steps=[
                'E_D_BENCH_PRESS_CLOSE_GRIP_BARBELL_EXEC_ONE',  # Inhale and lower the bar slowly towards your lower chest/upper abdomen.
                'E_D_BENCH_PRESS_CLOSE_GRIP_BARBELL_EXEC_TWO',  # Touch your chest lightly.
                'E_D_BENCH_PRESS_CLOSE_GRIP_BARBELL_EXEC_THREE' # Exhale and press the bar back up powerfully to the starting position.
            ],
            key_tips=[
                'E_D_BENCH_PRESS_CLOSE_GRIP_BARBELL_TIP_ONE', # Keep your elbows tucked in close to your body.
                'E_D_BENCH_PRESS_CLOSE_GRIP_BARBELL_TIP_TWO' # Focus on using your triceps to drive the weight up.
            ],
            focus_areas=[FocusArea.ARM, FocusArea.CHEST, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        ExerciseDefinition(
            id='exercise-28',
            title= "E_D_BENCH_PRESS_CLOSE_GRIP_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/bench_press_close_grip_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/bench_press_close_grip_dumbbell.png'],
            preparation_steps=[
                'E_D_BENCH_PRESS_CLOSE_GRIP_DUMBBELL_PREP_ONE', # Lie on a flat bench, holding a dumbbell in each hand.
                'E_D_BENCH_PRESS_CLOSE_GRIP_DUMBBELL_PREP_TWO'  # Bring the dumbbells together above your chest, palms facing each other (neutral grip).
            ],
            execution_steps=[
                'E_D_BENCH_PRESS_CLOSE_GRIP_DUMBBELL_EXEC_ONE',  # Inhale and lower the dumbbells slowly to the sides of your chest while keeping them touching.
                'E_D_BENCH_PRESS_CLOSE_GRIP_DUMBBELL_EXEC_TWO',  # Maintain contact between the dumbbells.
                'E_D_BENCH_PRESS_CLOSE_GRIP_DUMBBELL_EXEC_THREE' # Exhale and press the dumbbells back up to the starting position.
            ],
            key_tips=[
                'E_D_BENCH_PRESS_CLOSE_GRIP_DUMBBELL_TIP_ONE', # Keep your elbows tight to your sides to maximize triceps engagement.
                'E_D_BENCH_PRESS_CLOSE_GRIP_DUMBBELL_TIP_TWO' # Squeeze the dumbbells together throughout the entire movement.
            ],
            focus_areas=[FocusArea.ARM, FocusArea.CHEST, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-29',
            title= "E_D_BENCH_PRESS_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/bench_press_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/bench_press_dumbbell.png'],
            preparation_steps=[
                'E_D_BENCH_PRESS_DUMBBELL_PREP_ONE', # Lie on a flat bench with a dumbbell in each hand, palms facing forward.
                'E_D_BENCH_PRESS_DUMBBELL_PREP_TWO'  # Position the dumbbells at shoulder level with your elbows bent at a 90-degree angle.
            ],
            execution_steps=[
                'E_D_BENCH_PRESS_DUMBBELL_EXEC_ONE',  # Exhale and press the dumbbells upwards until your arms are fully extended over your chest.
                'E_D_BENCH_PRESS_DUMBBELL_EXEC_TWO',  # Squeeze your chest muscles at the top.
                'E_D_BENCH_PRESS_DUMBBELL_EXEC_THREE' # Inhale and slowly lower the dumbbells back to the starting position.
            ],
            key_tips=[
                'E_D_BENCH_PRESS_DUMBBELL_TIP_ONE', # Keep your shoulders pressed into the bench.
                'E_D_BENCH_PRESS_DUMBBELL_TIP_TWO' # Use a full range of motion, allowing a deep stretch in the chest at the bottom.
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-30',
            title= "E_D_BENCH_PRESS_SMITH_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/bench_press_smith_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/bench_press_smith_machine.png'],
            preparation_steps=[
                'E_D_BENCH_PRESS_SMITH_MACHINE_PREP_ONE', # Set up a flat bench inside the Smith Machine.
                'E_D_BENCH_PRESS_SMITH_MACHINE_PREP_TWO'  # Lie down and grip the bar slightly wider than shoulder-width, unhook the bar.
            ],
            execution_steps=[
                'E_D_BENCH_PRESS_SMITH_MACHINE_EXEC_ONE',  # Inhale and slowly lower the bar to your mid-chest.
                'E_D_BENCH_PRESS_SMITH_MACHINE_EXEC_TWO',  # Briefly pause when the bar touches your chest.
                'E_D_BENCH_PRESS_SMITH_MACHINE_EXEC_THREE' # Exhale and press the bar back up until your arms are fully extended.
            ],
            key_tips=[
                'E_D_BENCH_PRESS_SMITH_MACHINE_TIP_ONE', # Position the bench so the bar descends to your mid-chest.
                'E_D_BENCH_PRESS_SMITH_MACHINE_TIP_TWO' # The fixed path allows for better isolation; focus on muscle contraction.
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.SMITH_MACHINE,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        ExerciseDefinition(
            id='exercise-31',
            title= "E_D_BENCH_PRESS_WIDE_GRIP_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/bench_press_wide_grip_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/bench_press_wide_grip_barbell.png'],
            preparation_steps=[
                'E_D_BENCH_PRESS_WIDE_GRIP_BARBELL_PREP_ONE', # Lie on a flat bench and grip the barbell significantly wider than shoulder-width.
                'E_D_BENCH_PRESS_WIDE_GRIP_BARBELL_PREP_TWO'  # Unrack the bar and hold it over your chest.
            ],
            execution_steps=[
                'E_D_BENCH_PRESS_WIDE_GRIP_BARBELL_EXEC_ONE',  # Inhale and lower the bar slowly to your chest.
                'E_D_BENCH_PRESS_WIDE_GRIP_BARBELL_EXEC_TWO',  # Ensure your elbows flare out slightly.
                'E_D_BENCH_PRESS_WIDE_GRIP_BARBELL_EXEC_THREE' # Exhale and press the bar back up to the starting position.
            ],
            key_tips=[
                'E_D_BENCH_PRESS_WIDE_GRIP_BARBELL_TIP_ONE', # Use a controlled range of motion to protect your shoulders.
                'E_D_BENCH_PRESS_WIDE_GRIP_BARBELL_TIP_TWO' # This grip emphasizes the chest more than the triceps.
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        ExerciseDefinition(
            id='exercise-32',
            title= "E_D_BENCH_PRESS_WIDE_GRIP_SMITH_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/bench_press_wide_grip_smith_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/bench_press_wide_grip_smith_machine.png'],
            preparation_steps=[
                'E_D_BENCH_PRESS_WIDE_GRIP_SMITH_MACHINE_PREP_ONE', # Set up a flat bench inside the Smith Machine.
                'E_D_BENCH_PRESS_WIDE_GRIP_SMITH_MACHINE_PREP_TWO'  # Lie down and grip the bar significantly wider than shoulder-width, unhook the bar.
            ],
            execution_steps=[
                'E_D_BENCH_PRESS_WIDE_GRIP_SMITH_MACHINE_EXEC_ONE',  # Inhale and slowly lower the bar to your chest.
                'E_D_BENCH_PRESS_WIDE_GRIP_SMITH_MACHINE_EXEC_TWO',  # Maintain your wide grip throughout the set.
                'E_D_BENCH_PRESS_WIDE_GRIP_SMITH_MACHINE_EXEC_THREE' # Exhale and press the bar back up until your arms are extended.
            ],
            key_tips=[
                'E_D_BENCH_PRESS_WIDE_GRIP_SMITH_MACHINE_TIP_ONE', # The fixed bar path helps isolate the chest muscles.
                'E_D_BENCH_PRESS_WIDE_GRIP_SMITH_MACHINE_TIP_TWO' # Do not bounce the bar off your chest.
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.SMITH_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-33',
            title= "E_D_BENCH_SQUAT_TITLE",
            video_urls=[], # No video provided in your list
            cover_image_url=['regular_directory/exercises/images/bench_squat.png'],
            preparation_steps=[
                'E_D_BENCH_SQUAT_PREP_ONE', # Stand in front of a sturdy bench or box with feet shoulder-width apart.
                'E_D_BENCH_SQUAT_PREP_TWO'  # Keep your chest up, eyes looking straight ahead.
            ],
            execution_steps=[
                'E_D_BENCH_SQUAT_EXEC_ONE',  # Inhale and lower your hips down and back as if sitting in a chair until you lightly touch the bench.
                'E_D_BENCH_SQUAT_EXEC_TWO',  # Do not fully rest on the bench, just a light tap.
                'E_D_BENCH_SQUAT_EXEC_THREE' # Exhale and drive through your heels to stand back up to the starting position.
            ],
            key_tips=[
                'E_D_BENCH_SQUAT_TIP_ONE', # The bench helps ensure you reach the proper squat depth.
                'E_D_BENCH_SQUAT_TIP_TWO' # Keep your knees tracking over your toes and your back straight.
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
ExerciseDefinition(
            id='exercise-34',
            title= "E_D_BENCH_SQUAT_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/bench_squat_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/bench_squat_barbell.png'],
            preparation_steps=[
                'E_D_BENCH_SQUAT_BARBELL_PREP_ONE', # Load a barbell onto your upper back and stand in front of a bench.
                'E_D_BENCH_SQUAT_BARBELL_PREP_TWO'  # Ensure your feet are shoulder-width apart and chest is up.
            ],
            execution_steps=[
                'E_D_BENCH_SQUAT_BARBELL_EXEC_ONE',  # Lower your body slowly by pushing your hips back until you lightly touch the bench.
                'E_D_BENCH_SQUAT_BARBELL_EXEC_TWO',  # Maintain tension and do not fully sit down.
                'E_D_BENCH_SQUAT_BARBELL_EXEC_THREE' # Drive through your heels and stand back up, squeezing your glutes.
            ],
            key_tips=[
                'E_D_BENCH_SQUAT_BARBELL_TIP_ONE', # The bench acts as a depth marker; don't collapse onto it.
                'E_D_BENCH_SQUAT_BARBELL_TIP_TWO' # Keep a neutral spine and the barbell balanced securely.
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS, FocusArea.BACK],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        ExerciseDefinition(
            id='exercise-35',
            title= "E_D_BENCH_SQUAT_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/bench_squat_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/bench_squat_dumbbell.png'],
            preparation_steps=[
                'E_D_BENCH_SQUAT_DUMBBELL_PREP_ONE', # Hold a dumbbell in each hand or a single dumbbell vertically (goblet style).
                'E_D_BENCH_SQUAT_DUMBBELL_PREP_TWO'  # Stand in front of a bench, feet shoulder-width apart.
            ],
            execution_steps=[
                'E_D_BENCH_SQUAT_DUMBBELL_EXEC_ONE',  # Lower your hips until you lightly contact the bench.
                'E_D_BENCH_SQUAT_DUMBBELL_EXEC_TWO',  # Keep your chest lifted and back straight throughout the movement.
                'E_D_BENCH_SQUAT_DUMBBELL_EXEC_THREE' # Push back up to the standing position by extending your hips and knees.
            ],
            key_tips=[
                'E_D_BENCH_SQUAT_DUMBBELL_TIP_ONE', # Control the descent to maximize muscle engagement.
                'E_D_BENCH_SQUAT_DUMBBELL_TIP_TWO' # Maintain the weight in your heels to target the posterior chain.
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-36',
            title= "E_D_BENT_ARM_PULLOVER_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/bent_arm_pullover_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/bent_arm_pullover_barbell.png'],
            preparation_steps=[
                'E_D_BENT_ARM_PULLOVER_BARBELL_PREP_ONE', # Lie perpendicular across a flat bench, supporting your upper back and shoulders.
                'E_D_BENT_ARM_PULLOVER_BARBELL_PREP_TWO'  # Hold a barbell with a slightly bent-arm grip over your chest.
            ],
            execution_steps=[
                'E_D_BENT_ARM_PULLOVER_BARBELL_EXEC_ONE',  # Inhale and slowly lower the barbell in an arc behind your head.
                'E_D_BENT_ARM_PULLOVER_BARBELL_EXEC_TWO',  # Go as low as possible without arching your lower back excessively.
                'E_D_BENT_ARM_PULLOVER_BARBELL_EXEC_THREE' # Exhale and pull the barbell back over your chest using your lats and chest muscles.
            ],
            key_tips=[
                'E_D_BENT_ARM_PULLOVER_BARBELL_TIP_ONE', # Keep a slight bend in your elbows throughout the entire movement.
                'E_D_BENT_ARM_PULLOVER_BARBELL_TIP_TWO' # Focus on squeezing the rib cage and lats, not just the arms.
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-37',
            title= "E_D_BENT_KNEE_BICYCLE_CRUNCH_TITLE",
            video_urls=[], # No video provided in your list
            cover_image_url=['regular_directory/exercises/images/bent_knee_bicycle_crunch.png'],
            preparation_steps=[
                'E_D_BENT_KNEE_BICYCLE_CRUNCH_PREP_ONE', # Lie flat on your back, interlace your fingers behind your head.
                'E_D_BENT_KNEE_BICYCLE_CRUNCH_PREP_TWO'  # Lift your shoulders slightly off the floor and bring your knees up to a 90-degree angle.
            ],
            execution_steps=[
                'E_D_BENT_KNEE_BICYCLE_CRUNCH_EXEC_ONE',  # Bring your right elbow and left knee toward each other while extending your right leg.
                'E_D_BENT_KNEE_BICYCLE_CRUNCH_EXEC_TWO',  # Reverse the motion, bringing your left elbow toward your right knee.
                'E_D_BENT_KNEE_BICYCLE_CRUNCH_EXEC_THREE' # Continue alternating sides in a continuous cycling motion.
            ],
            key_tips=[
                'E_D_BENT_KNEE_BICYCLE_CRUNCH_TIP_ONE', # Focus on rotating your torso, not just moving your elbows.
                'E_D_BENT_KNEE_BICYCLE_CRUNCH_TIP_TWO' # Ensure your lower back remains pressed into the floor throughout.
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-38',
            title= "E_D_BENT_KNEE_SIDE_PLANK_TITLE",
            video_urls=['regular_directory/exercises/videos/bent_knee_side_plank.mp4'],
            cover_image_url=['regular_directory/exercises/images/bent_knee_side_plank.png'],
            preparation_steps=[
                'E_D_BENT_KNEE_SIDE_PLANK_PREP_ONE', # Lie on your side with your knees bent and stacked.
                'E_D_BENT_KNEE_SIDE_PLANK_PREP_TWO'  # Prop yourself up on your forearm, ensuring your elbow is directly under your shoulder.
            ],
            execution_steps=[
                'E_D_BENT_KNEE_SIDE_PLANK_EXEC_ONE',  # Lift your hips off the ground until your body forms a straight line from head to knees.
                'E_D_BENT_KNEE_SIDE_PLANK_EXEC_TWO',  # Hold this position, engaging your core and glutes.
                'E_D_BENT_KNEE_SIDE_PLANK_EXEC_THREE' # Slowly lower your hips back down and repeat on the other side.
            ],
            key_tips=[
                'E_D_BENT_KNEE_SIDE_PLANK_TIP_ONE', # Keep your chest open and avoid letting your hips sag.
                'E_D_BENT_KNEE_SIDE_PLANK_TIP_TWO' # This modification is easier on the lower back and is perfect for beginners.
            ],
            focus_areas=[FocusArea.ABDOMEN, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.TIME_BASED
        ),
        ExerciseDefinition(
            id='exercise-39',
            title= "E_D_BENT_KNEE_WIPERS_TITLE",
            video_urls=['regular_directory/exercises/videos/bent_knee_wipers.mp4'],
            cover_image_url=['regular_directory/exercises/images/bent_knee_wipers.png'],
            preparation_steps=[
                'E_D_BENT_KNEE_WIPERS_PREP_ONE', # Lie on your back with arms extended out to the sides for balance.
                'E_D_BENT_KNEE_WIPERS_PREP_TWO'  # Bend your knees and lift your feet off the floor until your thighs are vertical.
            ],
            execution_steps=[
                'E_D_BENT_KNEE_WIPERS_EXEC_ONE',  # Keeping your knees bent, slowly lower your legs toward one side, stopping before your shoulders lift.
                'E_D_BENT_KNEE_WIPERS_EXEC_TWO',  # Contract your oblique muscles to pull your legs back to the center.
                'E_D_BENT_KNEE_WIPERS_EXEC_THREE' # Repeat the movement to the opposite side, moving like windshield wipers.
            ],
            key_tips=[
                'E_D_BENT_KNEE_WIPERS_TIP_ONE', # Control the movement; do not let momentum take over.
                'E_D_BENT_KNEE_WIPERS_TIP_TWO' # Keep your upper back flat on the floor to maximize core engagement.
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-40',
            title= "E_D_BENT_OVER_REAR_DELT_ROW_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/bent_over_rear_delt_row_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/bent_over_rear_delt_row_band.png'],
            preparation_steps=[
                'E_D_BENT_OVER_REAR_DELT_ROW_BAND_PREP_ONE', # Stand on the middle of a resistance band, holding the ends.
                'E_D_BENT_OVER_REAR_DELT_ROW_BAND_PREP_TWO'  # Hinge at the hips so your torso is nearly parallel to the floor, arms hanging straight down.
            ],
            execution_steps=[
                'E_D_BENT_OVER_REAR_DELT_ROW_BAND_EXEC_ONE',  # Pull your hands up and out to the sides, squeezing your shoulder blades together.
                'E_D_BENT_OVER_REAR_DELT_ROW_BAND_EXEC_TWO',  # Focus on driving the elbows toward the ceiling.
                'E_D_BENT_OVER_REAR_DELT_ROW_BAND_EXEC_THREE' # Slowly lower your arms back to the starting position with control.
            ],
            key_tips=[
                'E_D_BENT_OVER_REAR_DELT_ROW_BAND_TIP_ONE', # Keep your core braced and maintain a flat back throughout the set.
                'E_D_BENT_OVER_REAR_DELT_ROW_BAND_TIP_TWO' # The resistance increases as you pull, emphasizing the contraction.
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.BACK],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-41',
            title= "E_D_BENT_OVER_REAR_DELT_ROW_BARBELL_TITLE",
            video_urls=[], # No video provided in your list
            cover_image_url=['regular_directory/exercises/images/bent_over_rear_delt_row_barbell.png'],
            preparation_steps=[
                'E_D_BENT_OVER_REAR_DELT_ROW_BARBELL_PREP_ONE', # Load a barbell and take a wide grip (palms facing down).
                'E_D_BENT_OVER_REAR_DELT_ROW_BARBELL_PREP_TWO'  # Hinge forward at the hips, keeping your back flat, until your torso is parallel to the ground.
            ],
            execution_steps=[
                'E_D_BENT_OVER_REAR_DELT_ROW_BARBELL_EXEC_ONE',  # Pull the barbell straight up toward your upper chest/collarbone area.
                'E_D_BENT_OVER_REAR_DELT_ROW_BARBELL_EXEC_TWO',  # Flare your elbows out to target the rear delts.
                'E_D_BENT_OVER_REAR_DELT_ROW_BARBELL_EXEC_THREE' # Slowly lower the bar back to the starting position.
            ],
            key_tips=[
                'E_D_BENT_OVER_REAR_DELT_ROW_BARBELL_TIP_ONE', # Use a weight that allows strict form; swinging indicates it is too heavy.
                'E_D_BENT_OVER_REAR_DELT_ROW_BARBELL_TIP_TWO' # Focus on squeezing the rear deltoids and upper back.
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.BACK],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-42',
            title= "E_D_BENT_OVER_REAR_DELT_ROW_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/bent_over_rear_delt_row_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/bent_over_rear_delt_row_dumbbell.png'],
            preparation_steps=[
                'E_D_BENT_OVER_REAR_DELT_ROW_DUMBBELL_PREP_ONE', # Hold a dumbbell in each hand (neutral grip).
                'E_D_BENT_OVER_REAR_DELT_ROW_DUMBBELL_PREP_TWO'  # Bend over until your torso is nearly parallel to the floor, arms hanging straight down.
            ],
            execution_steps=[
                'E_D_BENT_OVER_REAR_DELT_ROW_DUMBBELL_EXEC_ONE',  # Pull the dumbbells up and out to the sides, leading with your elbows.
                'E_D_BENT_OVER_REAR_DELT_ROW_DUMBBELL_EXEC_TWO',  # Squeeze your shoulder blades hard at the top of the movement.
                'E_D_BENT_OVER_REAR_DELT_ROW_DUMBBELL_EXEC_THREE' # Lower the dumbbells slowly back to the start.
            ],
            key_tips=[
                'E_D_BENT_OVER_REAR_DELT_ROW_DUMBBELL_TIP_ONE', # Keep your hips stable and your core tight to protect your lower back.
                'E_D_BENT_OVER_REAR_DELT_ROW_DUMBBELL_TIP_TWO' # The dumbbells should move wide and high, aiming to target the rear part of the shoulder.
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.BACK],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-43',
            title= "E_D_BENT_OVER_REAR_DELT_ROW_KETTLEBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/bent_over_rear_delt_row_kettlebell.mp4'],
            cover_image_url=['regular_directory/exercises/images/bent_over_rear_delt_row_kettlebell.png'],
            preparation_steps=[
                'E_D_BENT_OVER_REAR_DELT_ROW_KETTLEBELL_PREP_ONE', # Hold a kettlebell in each hand by the handles.
                'E_D_BENT_OVER_REAR_DELT_ROW_KETTLEBELL_PREP_TWO'  # Hinge at the hips with a flat back, arms extended downward.
            ],
            execution_steps=[
                'E_D_BENT_OVER_REAR_DELT_ROW_KETTLEBELL_EXEC_ONE',  # Pull the kettlebells up and out to the sides, driving the elbows high.
                'E_D_BENT_OVER_REAR_DELT_ROW_KETTLEBELL_EXEC_TWO',  # Maintain the bent-over position rigidly.
                'E_D_BENT_OVER_REAR_DELT_ROW_KETTLEBELL_EXEC_THREE' # Slowly return the kettlebells to the starting hang position.
            ],
            key_tips=[
                'E_D_BENT_OVER_REAR_DELT_ROW_KETTLEBELL_TIP_ONE', # The shape of the kettlebell may allow a slightly deeper squeeze at the top.
                'E_D_BENT_OVER_REAR_DELT_ROW_KETTLEBELL_TIP_TWO' # Concentrate on retracting the shoulder blades fully.
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.BACK],
            equipment=ExerciseEquipment.KETTLEBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-44',
            title= "E_D_BENT_OVER_REAR_DELT_ROW_SMITH_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/bent_over_rear_delt_row_smith_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/bent_over_rear_delt_row_smith_machine.png'],
            preparation_steps=[
                'E_D_BENT_OVER_REAR_DELT_ROW_SMITH_MACHINE_PREP_ONE', # Set the Smith Machine bar height for your starting position.
                'E_D_BENT_OVER_REAR_DELT_ROW_SMITH_MACHINE_PREP_TWO'  # Stand under the bar, bend your knees slightly, and hinge at the hips until your torso is parallel to the ground, grabbing the bar wide.
            ],
            execution_steps=[
                'E_D_BENT_OVER_REAR_DELT_ROW_SMITH_MACHINE_EXEC_ONE',  # Pull the bar toward your upper chest, flaring your elbows wide.
                'E_D_BENT_OVER_REAR_DELT_ROW_SMITH_MACHINE_EXEC_TWO',  # The fixed bar path helps isolate the rear delts.
                'E_D_BENT_OVER_REAR_DELT_ROW_SMITH_MACHINE_EXEC_THREE' # Control the bar slowly back down to the starting point.
            ],
            key_tips=[
                'E_D_BENT_OVER_REAR_DELT_ROW_SMITH_MACHINE_TIP_ONE', # The fixed path ensures consistent form, making it good for isolation.
                'E_D_BENT_OVER_REAR_DELT_ROW_SMITH_MACHINE_TIP_TWO' # Ensure your grip is wide enough to target the rear shoulders effectively.
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.BACK],
            equipment=ExerciseEquipment.SMITH_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-45',
            title= "E_D_BENT_OVER_REVERSE_FLY_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/bent_over_reverse_fly_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/bent_over_reverse_fly_band.png'],
            preparation_steps=[
                'E_D_BENT_OVER_REVERSE_FLY_BAND_PREP_ONE', # Stand on the middle of a resistance band, cross the ends, and hold them in your hands.
                'E_D_BENT_OVER_REVERSE_FLY_BAND_PREP_TWO'  # Hinge at your hips with a slight bend in your knees until your torso is parallel to the floor.
            ],
            execution_steps=[
                'E_D_BENT_OVER_REVERSE_FLY_BAND_EXEC_ONE',  # Keeping a slight bend in your elbows, raise your arms out to the sides in an arc.
                'E_D_BENT_OVER_REVERSE_FLY_BAND_EXEC_TWO',  # Squeeze your shoulder blades together at the peak of the movement.
                'E_D_BENT_OVER_REVERSE_FLY_BAND_EXEC_THREE' # Slowly lower your arms back to the starting position against the band's tension.
            ],
            key_tips=[
                'E_D_BENT_OVER_REVERSE_FLY_BAND_TIP_ONE', # Focus on movement in the shoulder joints, not the elbows.
                'E_D_BENT_OVER_REVERSE_FLY_BAND_TIP_TWO' # Control the speed, especially on the return, for muscle time under tension.
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.BACK],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-46',
            title= "E_D_BENT_OVER_REVERSE_FLY_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/bent_over_reverse_fly_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/bent_over_reverse_fly_cable.png'],
            preparation_steps=[
                'E_D_BENT_OVER_REVERSE_FLY_CABLE_PREP_ONE', # Set up two cable pulleys at a low height and stand between them.
                'E_D_BENT_OVER_REVERSE_FLY_CABLE_PREP_TWO'  # Grab the opposite handle (right hand grabs left cable, and vice versa), and bend over at the hips.
            ],
            execution_steps=[
                'E_D_BENT_OVER_REVERSE_FLY_CABLE_EXEC_ONE',  # Keeping a slight bend in your elbows, pull the cables out to the sides in a wide arc.
                'E_D_BENT_OVER_REVERSE_FLY_CABLE_EXEC_TWO',  # Contract your rear delts fully.
                'E_D_BENT_OVER_REVERSE_FLY_CABLE_EXEC_THREE' # Slowly return the handles to the starting position, allowing the cables to cross.
            ],
            key_tips=[
                'E_D_BENT_OVER_REVERSE_FLY_CABLE_TIP_ONE', # The crossover starting position ensures maximum range of motion.
                'E_D_BENT_OVER_REVERSE_FLY_CABLE_TIP_TWO' # Maintain a steady torso angle throughout the exercise.
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.BACK],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-47',
            title= "E_D_BENT_OVER_REVERSE_FLY_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/bent_over_reverse_fly_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/bent_over_reverse_fly_dumbbell.png'],
            preparation_steps=[
                'E_D_BENT_OVER_REVERSE_FLY_DUMBBELL_PREP_ONE', # Hold a dumbbell in each hand (neutral grip).
                'E_D_BENT_OVER_REVERSE_FLY_DUMBBELL_PREP_TWO'  # Hinge at the hips until your torso is parallel to the floor, arms extended down.
            ],
            execution_steps=[
                'E_D_BENT_OVER_REVERSE_FLY_DUMBBELL_EXEC_ONE',  # Raise the dumbbells out to the sides, keeping a slight bend in your elbows (like a bird flapping its wings).
                'E_D_BENT_OVER_REVERSE_FLY_DUMBBELL_EXEC_TWO',  # Focus on squeezing your upper back/rear shoulders.
                'E_D_BENT_OVER_REVERSE_FLY_DUMBBELL_EXEC_THREE' # Lower the weights slowly and controlled back to the starting position.
            ],
            key_tips=[
                'E_D_BENT_OVER_REVERSE_FLY_DUMBBELL_TIP_ONE', # To prevent swinging, use a lighter weight and emphasize isolation.
                'E_D_BENT_OVER_REVERSE_FLY_DUMBBELL_TIP_TWO' # If your lower back fatigues, prop your forehead on an incline bench for support.
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.BACK],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-48',
            title= "E_D_BENT_OVER_ROW_BAND_TITLE",
            video_urls=[], # No video provided in your list
            cover_image_url=['regular_directory/exercises/images/bent_over_row_band.png'],
            preparation_steps=[
                'E_D_BENT_OVER_ROW_BAND_PREP_ONE', # Stand on the middle of a resistance band with feet shoulder-width apart, holding the ends.
                'E_D_BENT_OVER_ROW_BAND_PREP_TWO'  # Hinge at the hips so your torso is at a 45-degree angle to the floor, arms hanging straight.
            ],
            execution_steps=[
                'E_D_BENT_OVER_ROW_BAND_EXEC_ONE',  # Pull the ends of the band toward your lower chest/waistline, squeezing your back muscles.
                'E_D_BENT_OVER_ROW_BAND_EXEC_TWO',  # Keep your elbows close to your body.
                'E_D_BENT_OVER_ROW_BAND_EXEC_THREE' # Slowly return your arms to the starting position, controlling the tension.
            ],
            key_tips=[
                'E_D_BENT_OVER_ROW_BAND_TIP_ONE', # Use an overhand or underhand grip to vary the focus on the back muscles.
                'E_D_BENT_OVER_ROW_BAND_TIP_TWO' # Maintain a strong, flat back throughout the movement.
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-49',
            title= "E_D_BENT_OVER_ROW_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/bent_over_row_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/bent_over_row_barbell.png'],
            preparation_steps=[
                'E_D_BENT_OVER_ROW_BARBELL_PREP_ONE', # Stand over a barbell with feet shoulder-width apart, grip the bar overhand.
                'E_D_BENT_OVER_ROW_BARBELL_PREP_TWO'  # Hinge at the hips with a flat back until your torso is roughly 45 degrees, hanging the bar with straight arms.
            ],
            execution_steps=[
                'E_D_BENT_OVER_ROW_BARBELL_EXEC_ONE',  # Pull the barbell explosively up towards your abdomen/lower chest.
                'E_D_BENT_OVER_ROW_BARBELL_EXEC_TWO',  # Squeeze your lats and middle back as you reach the top.
                'E_D_BENT_OVER_ROW_BARBELL_EXEC_THREE' # Slowly lower the bar back to the starting position.
            ],
            key_tips=[
                'E_D_BENT_OVER_ROW_BARBELL_TIP_ONE', # Avoid standing up or "cheating" with your legs; the back muscles should initiate the pull.
                'E_D_BENT_OVER_ROW_BARBELL_TIP_TWO' # Keep your core extremely tight to prevent back rounding.
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        ExerciseDefinition(
            id='exercise-50',
            title= "E_D_BENT_OVER_ROW_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/bent_over_row_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/bent_over_row_dumbbell.png'],
            preparation_steps=[
                'E_D_BENT_OVER_ROW_DUMBBELL_PREP_ONE', # Hold a dumbbell in each hand (neutral grip) and stand tall.
                'E_D_BENT_OVER_ROW_DUMBBELL_PREP_TWO'  # Hinge at the hips until your torso is roughly 45 degrees, maintaining a flat back.
            ],
            execution_steps=[
                'E_D_BENT_OVER_ROW_DUMBBELL_EXEC_ONE',  # Pull the dumbbells up toward your waist, keeping your elbows close to your body.
                'E_D_BENT_OVER_ROW_DUMBBELL_EXEC_TWO',  # Squeeze your back muscles (lats) at the peak contraction.
                'E_D_BENT_OVER_ROW_DUMBBELL_EXEC_THREE' # Lower the dumbbells slowly back to the starting hang.
            ],
            key_tips=[
                'E_D_BENT_OVER_ROW_DUMBBELL_TIP_ONE', # Dumbbells allow a greater range of motion compared to the barbell.
                'E_D_BENT_OVER_ROW_DUMBBELL_TIP_TWO' # Perform single-arm rows using a bench for lower back support, if needed.
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-51',
            title= "E_D_BENT_OVER_ROW_KETTLEBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/bent_over_row_kettlebell.mp4'],
            cover_image_url=['regular_directory/exercises/images/bent_over_row_kettlebell.png'],
            preparation_steps=[
                'E_D_BENT_OVER_ROW_KETTLEBELL_PREP_ONE', # Hold a kettlebell in each hand by the handle.
                'E_D_BENT_OVER_ROW_KETTLEBELL_PREP_TWO'  # Hinge at the hips, keeping your back flat, until your torso is around a 45-degree angle.
            ],
            execution_steps=[
                'E_D_BENT_OVER_ROW_KETTLEBELL_EXEC_ONE',  # Pull the kettlebells toward your waistline, leading with the elbows.
                'E_D_BENT_OVER_ROW_KETTLEBELL_EXEC_TWO',  # The kettlebell handles may allow for a slightly more comfortable neutral grip.
                'E_D_BENT_OVER_ROW_KETTLEBELL_EXEC_THREE' # Lower the weights slowly and deliberately back down.
            ],
            key_tips=[
                'E_D_BENT_OVER_ROW_KETTLEBELL_TIP_ONE', # Focus on pulling back and squeezing your shoulder blades together.
                'E_D_BENT_OVER_ROW_KETTLEBELL_TIP_TWO' # Keep your chin tucked to maintain spinal alignment.
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.KETTLEBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-52',
            title= "E_D_BENT_OVER_ROW_REVERSE_GRIP_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/bent_over_row_reverse_grip_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/bent_over_row_reverse_grip_barbell.png'],
            preparation_steps=[
                'E_D_BENT_OVER_ROW_REVERSE_GRIP_BARBELL_PREP_ONE', # Stand over a barbell and grip it with an underhand (reverse) grip, hands shoulder-width apart.
                'E_D_BENT_OVER_ROW_REVERSE_GRIP_BARBELL_PREP_TWO'  # Hinge forward at the hips to the bent-over position.
            ],
            execution_steps=[
                'E_D_BENT_OVER_ROW_REVERSE_GRIP_BARBELL_EXEC_ONE',  # Pull the barbell towards your abdomen/navel, keeping your elbows tucked.
                'E_D_BENT_OVER_ROW_REVERSE_GRIP_BARBELL_EXEC_TWO',  # The reverse grip strongly activates the biceps and lower lats.
                'E_D_BENT_OVER_ROW_REVERSE_GRIP_BARBELL_EXEC_THREE' # Lower the bar slowly back to the starting position.
            ],
            key_tips=[
                'E_D_BENT_OVER_ROW_REVERSE_GRIP_BARBELL_TIP_ONE', # Ensure a secure grip as the bar may want to roll out of your hands.
                'E_D_BENT_OVER_ROW_REVERSE_GRIP_BARBELL_TIP_TWO' # Focus on pulling with your elbows to maximize back involvement.
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        ExerciseDefinition(
            id='exercise-53',
            title= "E_D_BENT_OVER_ROW_REVERSE_GRIP_DUMBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/bent_over_row_reverse_grip_dumbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/bent_over_row_reverse_grip_dumbell.png'],
            preparation_steps=[
                'E_D_BENT_OVER_ROW_REVERSE_GRIP_DUMBELL_PREP_ONE', # Hold a dumbbell in each hand with an underhand (supinated) grip.
                'E_D_BENT_OVER_ROW_REVERSE_GRIP_DUMBELL_PREP_TWO'  # Hinge forward at the hips to assume the bent-over position.
            ],
            execution_steps=[
                'E_D_BENT_OVER_ROW_REVERSE_GRIP_DUMBELL_EXEC_ONE',  # Pull the dumbbells toward your lower chest/waistline, keeping your palms facing up.
                'E_D_BENT_OVER_ROW_REVERSE_GRIP_DUMBELL_EXEC_TWO',  # Squeeze the back and biceps simultaneously.
                'E_D_BENT_OVER_ROW_REVERSE_GRIP_DUMBELL_EXEC_THREE' # Lower the dumbbells slowly back down.
            ],
            key_tips=[
                'E_D_BENT_OVER_ROW_REVERSE_GRIP_DUMBELL_TIP_ONE', # Use the flexibility of the dumbbells to find the most comfortable pulling path.
                'E_D_BENT_OVER_ROW_REVERSE_GRIP_DUMBELL_TIP_TWO' # Keep your gaze slightly forward to help maintain a neutral neck.
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-54',
            title= "E_D_BENT_OVER_ROW_SMITH_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/bent_over_row_smith_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/bent_over_row_smith_machine.png'],
            preparation_steps=[
                'E_D_BENT_OVER_ROW_SMITH_MACHINE_PREP_ONE', # Stand facing the Smith Machine bar, setting it at a height where you can bend over and grab it.
                'E_D_BENT_OVER_ROW_SMITH_MACHINE_PREP_TWO'  # Hinge at the hips, grab the bar with an overhand grip, and unhook it.
            ],
            execution_steps=[
                'E_D_BENT_OVER_ROW_SMITH_MACHINE_EXEC_ONE',  # Pull the bar straight up toward your abdomen.
                'E_D_BENT_OVER_ROW_SMITH_MACHINE_EXEC_TWO',  # The fixed path ensures strict vertical movement, isolating the back.
                'E_D_BENT_OVER_ROW_SMITH_MACHINE_EXEC_THREE' # Slowly return the bar to the starting position before racking it.
            ],
            key_tips=[
                'E_D_BENT_OVER_ROW_SMITH_MACHINE_TIP_ONE', # Stand close enough to the bar so the pull is directly upward, not forward.
                'E_D_BENT_OVER_ROW_SMITH_MACHINE_TIP_TWO' # Avoid using leg drive; focus on pure upper body pulling.
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.SMITH_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-55',
            title= "E_D_BENT_OVER_ROW_WITH_TWIST_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/bent_over_row_with_twist_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/bent_over_row_with_twist_band.png'],
            preparation_steps=[
                'E_D_BENT_OVER_ROW_WITH_TWIST_BAND_PREP_ONE', # Stand on the middle of a resistance band, holding both ends.
                'E_D_BENT_OVER_ROW_WITH_TWIST_BAND_PREP_TWO'  # Hinge at the hips with a flat back, arms extended.
            ],
            execution_steps=[
                'E_D_BENT_OVER_ROW_WITH_TWIST_BAND_EXEC_ONE',  # Pull one hand up to your side (row), and simultaneously rotate your torso slightly to that side.
                'E_D_BENT_OVER_ROW_WITH_TWIST_BAND_EXEC_TWO',  # Return the hand to the starting position while untwisting.
                'E_D_BENT_OVER_ROW_WITH_TWIST_BAND_EXEC_THREE' # Repeat the row and twist motion on the opposite side, alternating.
            ],
            key_tips=[
                'E_D_BENT_OVER_ROW_WITH_TWIST_BAND_TIP_ONE', # This variation targets the core (obliques) along with the back.
                'E_D_BENT_OVER_ROW_WITH_TWIST_BAND_TIP_TWO' # Keep the twisting motion controlled and originating from the core.
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ABDOMEN, FocusArea.ARM],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-24',
            title='E_D_BICEP_CURL_TITLE',
            video_urls=['regular_directory/exercises/videos/bicep_curl.mp4'],
            cover_image_url=['regular_directory/exercises/images/bicep_curl.png'],
            preparation_steps=[
                'E_D_BICEP_CURL_PREP_ONE',
                'E_D_BICEP_CURL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_BICEP_CURL_EXEC_ONE',
                'E_D_BICEP_CURL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_BICEP_CURL_TIP_ONE',
                'E_D_BICEP_CURL_TIP_TWO'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 2. Bicep Curl: Band
        ExerciseDefinition(
            id='exercise-25',
            title='E_D_BICEP_CURL_BAND_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/bicep_curl_band.png'],
            preparation_steps=[
                'E_D_BICEP_CURL_BAND_PREP_ONE',
                'E_D_BICEP_CURL_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_BICEP_CURL_BAND_EXEC_ONE',
                'E_D_BICEP_CURL_BAND_EXEC_TWO',
                'E_D_BICEP_CURL_BAND_EXEC_THREE'
            ],
            key_tips=[
                'E_D_BICEP_CURL_BAND_TIP_ONE',
                'E_D_BICEP_CURL_BAND_TIP_TWO'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 3. Bicep Curl: Barbell
        ExerciseDefinition(
            id='exercise-26',
            title='E_D_BICEP_CURL_BARBELL_TITLE',
            video_urls=['regular_directory/exercises/videos/bicep_curl_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/bicep_curl_barbell.png'],
            preparation_steps=[
                'E_D_BICEP_CURL_BARBELL_PREP_ONE',
                'E_D_BICEP_CURL_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_BICEP_CURL_BARBELL_EXEC_ONE',
                'E_D_BICEP_CURL_BARBELL_EXEC_TWO',
                'E_D_BICEP_CURL_BARBELL_EXEC_THREE'
            ],
            key_tips=[
                'E_D_BICEP_CURL_BARBELL_TIP_ONE',
                'E_D_BICEP_CURL_BARBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        # 4. Bicep Curl: Cable
        ExerciseDefinition(
            id='exercise-27',
            title='E_D_BICEP_CURL_CABLE_TITLE',
            video_urls=['regular_directory/exercises/videos/bicep_curl_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/bicep_curl_cable.png'],
            preparation_steps=[
                'E_D_BICEP_CURL_CABLE_PREP_ONE'
            ],
            execution_steps=[
                'E_D_BICEP_CURL_CABLE_EXEC_ONE',
                'E_D_BICEP_CURL_CABLE_EXEC_TWO',
                'E_D_BICEP_CURL_CABLE_EXEC_THREE'
            ],
            key_tips=[
                'E_D_BICEP_CURL_CABLE_TIP_ONE',
                'E_D_BICEP_CURL_CABLE_TIP_TWO',
                'E_D_BICEP_CURL_CABLE_TIP_THREE'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 5. Bicep Curl: Dumbbell
        ExerciseDefinition(
            id='exercise-28',
            title='E_D_BICEP_CURL_DUMBBELL_TITLE',
            video_urls=['regular_directory/exercises/videos/bicep_curl_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/bicep_curl_dumbbell.png'],
            preparation_steps=[
                'E_D_BICEP_CURL_DUMBBELL_PREP_ONE'
            ],
            execution_steps=[
                'E_D_BICEP_CURL_DUMBBELL_EXEC_ONE',
                'E_D_BICEP_CURL_DUMBBELL_EXEC_TWO',
                'E_D_BICEP_CURL_DUMBBELL_EXEC_THREE'
            ],
            key_tips=[
                'E_D_BICEP_CURL_DUMBBELL_TIP_ONE',
                'E_D_BICEP_CURL_DUMBBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 6. Bicep Curl: Machine
        ExerciseDefinition(
            id='exercise-29',
            title='E_D_BICEP_CURL_MACHINE_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/bicep_curl_machine.png'],
            preparation_steps=[
                'E_D_BICEP_CURL_MACHINE_PREP_ONE',
                'E_D_BICEP_CURL_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_BICEP_CURL_MACHINE_EXEC_ONE',
                'E_D_BICEP_CURL_MACHINE_EXEC_TWO',
                'E_D_BICEP_CURL_MACHINE_EXEC_THREE',
                'E_D_BICEP_CURL_MACHINE_EXEC_FOUR'
            ],
            key_tips=[
                'E_D_BICEP_CURL_MACHINE_TIP_ONE',
                'E_D_BICEP_CURL_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 7. Bicep Curl: Smith Machine
        ExerciseDefinition(
            id='exercise-30',
            title='E_D_BICEP_CURL_SMITH_MACHINE_TITLE',
            video_urls=['regular_directory/exercises/videos/bicep_curl_smith_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/bicep_curl_smith_machine.png'],
            preparation_steps=[
                'E_D_BICEP_CURL_SMITH_MACHINE_PREP_ONE',
                'E_D_BICEP_CURL_SMITH_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_BICEP_CURL_SMITH_MACHINE_EXEC_ONE',
                'E_D_BICEP_CURL_SMITH_MACHINE_EXEC_TWO',
                'E_D_BICEP_CURL_SMITH_MACHINE_EXEC_THREE'
            ],
            key_tips=[
                'E_D_BICEP_CURL_SMITH_MACHINE_TIP_ONE',
                'E_D_BICEP_CURL_SMITH_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.SMITH_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 8. Bicycle Crunch
        ExerciseDefinition(
            id='exercise-31',
            title='E_D_BICYCLE_CRUNCH_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/bicycle_crunch.png'],
            preparation_steps=[
                'E_D_BICYCLE_CRUNCH_PREP_ONE'
            ],
            execution_steps=[
                'E_D_BICYCLE_CRUNCH_EXEC_ONE',
                'E_D_BICYCLE_CRUNCH_EXEC_TWO'
            ],
            key_tips=[
                'E_D_BICYCLE_CRUNCH_TIP_ONE',
                'E_D_BICYCLE_CRUNCH_TIP_TWO',
                'E_D_BICYCLE_CRUNCH_TIP_THREE'
            ],
            focus_areas=[FocusArea.ABDOMEN, FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 9. Bicycle Crunch: Band
        ExerciseDefinition(
            id='exercise-32',
            title='E_D_BICYCLE_CRUNCH_BAND_TITLE',
            video_urls=['regular_directory/exercises/videos/bicycle_crunch_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/bicycle_crunch_band.png'],
            preparation_steps=[
                'E_D_BICYCLE_CRUNCH_BAND_PREP_ONE',
                'E_D_BICYCLE_CRUNCH_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_BICYCLE_CRUNCH_BAND_EXEC_ONE',
                'E_D_BICYCLE_CRUNCH_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_BICYCLE_CRUNCH_BAND_TIP_ONE',
                'E_D_BICYCLE_CRUNCH_BAND_TIP_TWO',
                'E_D_BICYCLE_CRUNCH_BAND_TIP_THREE'
            ],
            focus_areas=[FocusArea.ABDOMEN, FocusArea.LEG],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 10. Bird Dog
        ExerciseDefinition(
            id='exercise-33',
            title='E_D_BIRD_DOG_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/bird_dog.png'],
            preparation_steps=[
                'E_D_BIRD_DOG_PREP_ONE'
            ],
            execution_steps=[
                'E_D_BIRD_DOG_EXEC_ONE',
                'E_D_BIRD_DOG_EXEC_TWO'
            ],
            key_tips=[
                'E_D_BIRD_DOG_TIP_ONE',
                'E_D_BIRD_DOG_TIP_TWO'
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.BACK, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 11. Boxer Shuffle
        ExerciseDefinition(
            id='exercise-34',
            title='E_D_BOXER_SHUFFLE_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/boxer_shuffle.png'],
            preparation_steps=[
                'E_D_BOXER_SHUFFLE_PREP_ONE',
                'E_D_BOXER_SHUFFLE_PREP_TWO',
                'E_D_BOXER_SHUFFLE_PREP_THREE'
            ],
            execution_steps=[
                'E_D_BOXER_SHUFFLE_EXEC_ONE',
                'E_D_BOXER_SHUFFLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_BOXER_SHUFFLE_TIP_ONE',
                'E_D_BOXER_SHUFFLE_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.TIME_BASED
        ),
        # 12. Bulgarian Split Squat
        ExerciseDefinition(
            id='exercise-35',
            title='E_D_BULGARIAN_SPLIT_SQUAT_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/bulgarian_split_squat.png'],
            preparation_steps=[
                'E_D_BULGARIAN_SPLIT_SQUAT_PREP_ONE',
                'E_D_BULGARIAN_SPLIT_SQUAT_PREP_TWO'
            ],
            execution_steps=[
                'E_D_BULGARIAN_SPLIT_SQUAT_EXEC_ONE',
                'E_D_BULGARIAN_SPLIT_SQUAT_EXEC_TWO',
                'E_D_BULGARIAN_SPLIT_SQUAT_EXEC_THREE',
                'E_D_BULGARIAN_SPLIT_SQUAT_EXEC_FOUR'
            ],
            key_tips=[
                'E_D_BULGARIAN_SPLIT_SQUAT_TIP_ONE',
                'E_D_BULGARIAN_SPLIT_SQUAT_TIP_TWO',
                'E_D_BULGARIAN_SPLIT_SQUAT_TIP_THREE',
                'E_D_BULGARIAN_SPLIT_SQUAT_TIP_FOUR'
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 13. Bulgarian Split Squat: Barbell
        ExerciseDefinition(
            id='exercise-36',
            title='E_D_BULGARIAN_SPLIT_SQUAT_BARBELL_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/bulgarian_split_squat_barbell.png'],
            preparation_steps=[
                'E_D_BULGARIAN_SPLIT_SQUAT_BARBELL_PREP_ONE',
                'E_D_BULGARIAN_SPLIT_SQUAT_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_BULGARIAN_SPLIT_SQUAT_BARBELL_EXEC_ONE',
                'E_D_BULGARIAN_SPLIT_SQUAT_BARBELL_EXEC_TWO',
                'E_D_BULGARIAN_SPLIT_SQUAT_BARBELL_EXEC_THREE',
                'E_D_BULGARIAN_SPLIT_SQUAT_BARBELL_EXEC_FOUR'
            ],
            key_tips=[
                'E_D_BULGARIAN_SPLIT_SQUAT_BARBELL_TIP_ONE',
                'E_D_BULGARIAN_SPLIT_SQUAT_BARBELL_TIP_TWO',
                'E_D_BULGARIAN_SPLIT_SQUAT_BARBELL_TIP_THREE',
                'E_D_BULGARIAN_SPLIT_SQUAT_BARBELL_TIP_FOUR'
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        # 14. Bulgarian Split Squat - Dumbbell
        ExerciseDefinition(
            id='exercise-37',
            title='E_D_BULGARIAN_SPLIT_SQUAT_DUMBBELL_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/bulgarian_split_squat_dumbbell.png'],
            preparation_steps=[
                'E_D_BULGARIAN_SPLIT_SQUAT_DUMBBELL_PREP_ONE',
                'E_D_BULGARIAN_SPLIT_SQUAT_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_BULGARIAN_SPLIT_SQUAT_DUMBBELL_EXEC_ONE',
                'E_D_BULGARIAN_SPLIT_SQUAT_DUMBBELL_EXEC_TWO',
                'E_D_BULGARIAN_SPLIT_SQUAT_DUMBBELL_EXEC_THREE',
                'E_D_BULGARIAN_SPLIT_SQUAT_DUMBBELL_EXEC_FOUR'
            ],
            key_tips=[
                'E_D_BULGARIAN_SPLIT_SQUAT_DUMBBELL_TIP_ONE',
                'E_D_BULGARIAN_SPLIT_SQUAT_DUMBBELL_TIP_TWO',
                'E_D_BULGARIAN_SPLIT_SQUAT_DUMBBELL_TIP_THREE',
                'E_D_BULGARIAN_SPLIT_SQUAT_DUMBBELL_TIP_FOUR'
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 15. Burpee
        ExerciseDefinition(
            id='exercise-38',
            title='E_D_BURPEE_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/burpee.png'],
            preparation_steps=[
                'E_D_BURPEE_PREP_ONE',
                'E_D_BURPEE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_BURPEE_EXEC_ONE',
                'E_D_BURPEE_EXEC_TWO',
                'E_D_BURPEE_EXEC_THREE',
                'E_D_BURPEE_EXEC_FOUR'
            ],
            key_tips=[
                'E_D_BURPEE_TIP_ONE',
                'E_D_BURPEE_TIP_TWO',
                'E_D_BURPEE_TIP_THREE'
            ],
            focus_areas=[FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 16. Butt Kicks
        ExerciseDefinition(
            id='exercise-39',
            title='E_D_BUTT_KICKS_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/butt_kicks.png'],
            preparation_steps=[
                'E_D_BUTT_KICKS_PREP_ONE'
            ],
            execution_steps=[
                'E_D_BUTT_KICKS_EXEC_ONE',
                'E_D_BUTT_KICKS_EXEC_TWO'
            ],
            key_tips=[
                'E_D_BUTT_KICKS_TIP_ONE',
                'E_D_BUTT_KICKS_TIP_TWO',
                'E_D_BUTT_KICKS_TIP_THREE'
            ],
            focus_areas=[FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.TIME_BASED
        ),
        # 17. Cable Pull Through
        ExerciseDefinition(
            id='exercise-40',
            title='E_D_CABLE_PULL_THROUGH_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/cable_pull_through.png'],
            preparation_steps=[
                'E_D_CABLE_PULL_THROUGH_PREP_ONE',
                'E_D_CABLE_PULL_THROUGH_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CABLE_PULL_THROUGH_EXEC_ONE',
                'E_D_CABLE_PULL_THROUGH_EXEC_TWO',
                'E_D_CABLE_PULL_THROUGH_EXEC_THREE'
            ],
            key_tips=[
                'E_D_CABLE_PULL_THROUGH_TIP_ONE',
                'E_D_CABLE_PULL_THROUGH_TIP_TWO',
                'E_D_CABLE_PULL_THROUGH_TIP_THREE',
                'E_D_CABLE_PULL_THROUGH_TIP_FOUR',
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.BACK, FocusArea.LEG],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 18. Chest Dip
        ExerciseDefinition(
            id='exercise-41',
            title='E_D_CHEST_DIP_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/chest_dip.png'],
            preparation_steps=[
                'E_D_CHEST_DIP_PREP_ONE',
                'E_D_CHEST_DIP_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CHEST_DIP_EXEC_ONE',
                'E_D_CHEST_DIP_EXEC_TWO'
            ],
            key_tips=[
                'E_D_CHEST_DIP_TIP_ONE',
                'E_D_CHEST_DIP_TIP_TWO',
                'E_D_CHEST_DIP_TIP_THREE'
            ],
            focus_areas=[FocusArea.ARM, FocusArea.CHEST, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 19. Chest Dip: Assisted
        ExerciseDefinition(
            id='exercise-42',
            title='E_D_CHEST_DIP_ASSISTED_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/chest_dip_assisted.png'],
            preparation_steps=[
                'E_D_CHEST_DIP_ASSISTED_PREP_ONE',
                'E_D_CHEST_DIP_ASSISTED_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CHEST_DIP_ASSISTED_EXEC_ONE',
                'E_D_CHEST_DIP_ASSISTED_EXEC_TWO'
            ],
            key_tips=[
                'E_D_CHEST_DIP_ASSISTED_TIP_ONE',
                'E_D_CHEST_DIP_ASSISTED_TIP_TWO',
                'E_D_CHEST_DIP_ASSISTED_TIP_THREE'
            ],
            focus_areas=[FocusArea.ARM, FocusArea.CHEST, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 20. Chin Up
        ExerciseDefinition(
            id='exercise-43',
            title='E_D_CHIN_UP_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/chin_up.png'],
            preparation_steps=[
                'E_D_CHIN_UP_PREP_ONE',
                'E_D_CHIN_UP_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CHIN_UP_EXEC_ONE',
                'E_D_CHIN_UP_EXEC_TWO',
                'E_D_CHIN_UP_EXEC_THREE'
            ],
            key_tips=[
                'E_D_CHIN_UP_TIP_ONE',
                'E_D_CHIN_UP_TIP_TWO',
                'E_D_CHIN_UP_TIP_THREE'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 21. Chin Up: Assisted
        ExerciseDefinition(
            id='exercise-44',
            title='E_D_CHIN_UP_ASSISTED_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/chin_up_assisted.png'],
            preparation_steps=[
                'E_D_CHIN_UP_ASSISTED_PREP_ONE',
                'E_D_CHIN_UP_ASSISTED_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CHIN_UP_ASSISTED_EXEC_ONE',
                'E_D_CHIN_UP_ASSISTED_EXEC_TWO',
                'E_D_CHIN_UP_ASSISTED_EXEC_THREE'
            ],
            key_tips=[
                'E_D_CHIN_UP_ASSISTED_TIP_ONE',
                'E_D_CHIN_UP_ASSISTED_TIP_TWO',
                'E_D_CHIN_UP_ASSISTED_TIP_THREE'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 22. Clean and Press: Barbell
        ExerciseDefinition(
            id='exercise-45',
            title='E_D_CLEAN_PRESS_BARBELL_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/clean_and_press_barbell.png'],
            preparation_steps=[
                'E_D_CLEAN_PRESS_BARBELL_PREP_ONE',
            ],
            execution_steps=[
                'E_D_CLEAN_PRESS_BARBELL_EXEC_ONE',
                'E_D_CLEAN_PRESS_BARBELL_EXEC_TWO',
                'E_D_CLEAN_PRESS_BARBELL_EXEC_THREE',
                'E_D_CLEAN_PRESS_BARBELL_EXEC_FOUR',
                'E_D_CLEAN_PRESS_BARBELL_EXEC_FIVE'
            ],
            key_tips=[
                'E_D_CLEAN_PRESS_BARBELL_TIP_ONE',
                'E_D_CLEAN_PRESS_BARBELL_TIP_TWO',
                'E_D_CLEAN_PRESS_BARBELL_TIP_THREE'
            ],
            focus_areas=[FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        # 23. Clean and Press: Kettlebell
        ExerciseDefinition(
            id='exercise-46',
            title='E_D_CLEAN_PRESS_KETTLEBELL_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/clean_and_press_kettlebell.png'],
            preparation_steps=[
                'E_D_CLEAN_PRESS_KETTLEBELL_PREP_ONE',
                'E_D_CLEAN_PRESS_KETTLEBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CLEAN_PRESS_KETTLEBELL_EXEC_ONE',
                'E_D_CLEAN_PRESS_KETTLEBELL_EXEC_TWO',
                'E_D_CLEAN_PRESS_KETTLEBELL_EXEC_THREE',
                'E_D_CLEAN_PRESS_KETTLEBELL_EXEC_FOUR',
                'E_D_CLEAN_PRESS_KETTLEBELL_EXEC_FIVE'
            ],
            key_tips=[
                'E_D_CLEAN_PRESS_KETTLEBELL_TIP_ONE',
                'E_D_CLEAN_PRESS_KETTLEBELL_TIP_TWO',
                'E_D_CLEAN_PRESS_KETTLEBELL_TIP_THREE'
            ],
            focus_areas=[FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.KETTLEBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 24. Clean: Barbell
        ExerciseDefinition(
            id='exercise-47',
            title='E_D_CLEAN_BARBELL_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/clean_barbell.png'],
            preparation_steps=[
                'E_D_CLEAN_BARBELL_PREP_ONE',
                'E_D_CLEAN_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CLEAN_BARBELL_EXEC_ONE',
                'E_D_CLEAN_BARBELL_EXEC_TWO',
                'E_D_CLEAN_BARBELL_EXEC_THREE',
                'E_D_CLEAN_BARBELL_EXEC_FOUR'
            ],
            key_tips=[
                'E_D_CLEAN_BARBELL_TIP_ONE',
                'E_D_CLEAN_BARBELL_TIP_TWO',
                'E_D_CLEAN_BARBELL_TIP_THREE'
            ],
            focus_areas=[FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        # 25. Close Grip Push Up
        ExerciseDefinition(
            id='exercise-48',
            title='E_D_CLOSE_GRIP_PUSH_UP_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/close_grip_push_up.png'],
            preparation_steps=[
                'E_D_CLOSE_GRIP_PUSH_UP_PREP_ONE',
                'E_D_CLOSE_GRIP_PUSH_UP_PREP_TWO',
                'E_D_CLOSE_GRIP_PUSH_UP_PREP_THREE'
            ],
            execution_steps=[
                'E_D_CLOSE_GRIP_PUSH_UP_EXEC_ONE',
                'E_D_CLOSE_GRIP_PUSH_UP_EXEC_TWO'
            ],
            key_tips=[
                'E_D_CLOSE_GRIP_PUSH_UP_TIP_ONE',
                'E_D_CLOSE_GRIP_PUSH_UP_TIP_TWO',
                'E_D_CLOSE_GRIP_PUSH_UP_TIP_THREE'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.ARM],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 26. Concentration Curl: Band
        ExerciseDefinition(
            id='exercise-49',
            title='E_D_CONCENTRATION_CURL_BAND_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/concentration_curl_band.png'],
            preparation_steps=[
                'E_D_CONCENTRATION_CURL_BAND_PREP_ONE',
                'E_D_CONCENTRATION_CURL_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CONCENTRATION_CURL_BAND_EXEC_ONE',
                'E_D_CONCENTRATION_CURL_BAND_EXEC_TWO',
                'E_D_CONCENTRATION_CURL_BAND_EXEC_THREE',
                'E_D_CONCENTRATION_CURL_BAND_EXEC_FOUR'
            ],
            key_tips=[
                'E_D_CONCENTRATION_CURL_BAND_TIP_ONE',
                'E_D_CONCENTRATION_CURL_BAND_TIP_TWO'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 27. Concentration Curl: Barbell
        ExerciseDefinition(
            id='exercise-50',
            title='E_D_CONCENTRATION_CURL_BARBELL_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/concentration_curl_barbell.png'],
            preparation_steps=[
                'E_D_CONCENTRATION_CURL_BARBELL_PREP_ONE',
                'E_D_CONCENTRATION_CURL_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CONCENTRATION_CURL_BARBELL_EXEC_ONE',
                'E_D_CONCENTRATION_CURL_BARBELL_EXEC_TWO',
                'E_D_CONCENTRATION_CURL_BARBELL_EXEC_THREE',
            ],
            key_tips=[
                'E_D_CONCENTRATION_CURL_BARBELL_TIP_ONE',
                'E_D_CONCENTRATION_CURL_BARBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        # 28. Concentration Curl: Cable
        ExerciseDefinition(
            id='exercise-51',
            title='E_D_CONCENTRATION_CURL_CABLE_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/concentration_curl_cable.png'],
            preparation_steps=[
                'E_D_CONCENTRATION_CURL_CABLE_PREP_ONE',
                'E_D_CONCENTRATION_CURL_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CONCENTRATION_CURL_CABLE_EXEC_ONE',
                'E_D_CONCENTRATION_CURL_CABLE_EXEC_TWO',
                'E_D_CONCENTRATION_CURL_CABLE_EXEC_THREE',
                'E_D_CONCENTRATION_CURL_CABLE_EXEC_FOUR'
            ],
            key_tips=[
                'E_D_CONCENTRATION_CURL_CABLE_TIP_ONE',
                'E_D_CONCENTRATION_CURL_CABLE_TIP_TWO'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 29. Concentration Curl: Dumbbell
        ExerciseDefinition(
            id='exercise-52',
            title='E_D_CONCENTRATION_CURL_DUMBBELL_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/concentration_curl_dumbbell.png'],
            preparation_steps=[
                'E_D_CONCENTRATION_CURL_DUMBBELL_PREP_ONE',
                'E_D_CONCENTRATION_CURL_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CONCENTRATION_CURL_DUMBBELL_EXEC_ONE',
                'E_D_CONCENTRATION_CURL_DUMBBELL_EXEC_TWO',
                'E_D_CONCENTRATION_CURL_DUMBBELL_EXEC_THREE',
                'E_D_CONCENTRATION_CURL_DUMBBELL_EXEC_FOUR'
            ],
            key_tips=[
                'E_D_CONCENTRATION_CURL_DUMBBELL_TIP_ONE',
                'E_D_CONCENTRATION_CURL_DUMBBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 30. Crossbody Crunch
        ExerciseDefinition(
            id='exercise-53',
            title='E_D_CROSSBODY_CRUNCH_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/crossbody_crunch.png'],
            preparation_steps=[
                'E_D_CROSSBODY_CRUNCH_PREP_ONE',
                'E_D_CROSSBODY_CRUNCH_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CROSSBODY_CRUNCH_EXEC_ONE',
                'E_D_CROSSBODY_CRUNCH_EXEC_TWO',
                'E_D_CROSSBODY_CRUNCH_EXEC_THREE'
            ],
            key_tips=[
                'E_D_CROSSBODY_CRUNCH_TIP_ONE',
                'E_D_CROSSBODY_CRUNCH_TIP_TWO',
                'E_D_CROSSBODY_CRUNCH_TIP_THREE'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 31. Crossbody Hammer Curl: Dumbbell
        ExerciseDefinition(
            id='exercise-54',
            title='E_D_CROSSBODY_HAMMER_CURL_DUMBBELL_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/crossbody_hammer_curl_dumbbell.png'],
            preparation_steps=[
                'E_D_CROSSBODY_HAMMER_CURL_DUMBBELL_PREP_ONE',
                'E_D_CROSSBODY_HAMMER_CURL_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CROSSBODY_HAMMER_CURL_DUMBBELL_EXEC_ONE',
                'E_D_CROSSBODY_HAMMER_CURL_DUMBBELL_EXEC_TWO',
                'E_D_CROSSBODY_HAMMER_CURL_DUMBBELL_EXEC_THREE',
                'E_D_CROSSBODY_HAMMER_CURL_DUMBBELL_EXEC_FOUR'
            ],
            key_tips=[
                'E_D_CROSSBODY_HAMMER_CURL_DUMBBELL_TIP_ONE',
                'E_D_CROSSBODY_HAMMER_CURL_DUMBBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 32. Crossbody Mountain Climber
        ExerciseDefinition(
            id='exercise-55',
            title='E_D_CROSSBODY_MOUNTAIN_CLIMBER_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/crossbody_mountain_climber.png'],
            preparation_steps=[
                'E_D_CROSSBODY_MOUNTAIN_CLIMBER_PREP_ONE',
                'E_D_CROSSBODY_MOUNTAIN_CLIMBER_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CROSSBODY_MOUNTAIN_CLIMBER_EXEC_ONE',
                'E_D_CROSSBODY_MOUNTAIN_CLIMBER_EXEC_TWO',
                'E_D_CROSSBODY_MOUNTAIN_CLIMBER_EXEC_THREE'
            ],
            key_tips=[
                'E_D_CROSSBODY_MOUNTAIN_CLIMBER_TIP_ONE',
                'E_D_CROSSBODY_MOUNTAIN_CLIMBER_TIP_TWO',
                'E_D_CROSSBODY_MOUNTAIN_CLIMBER_TIP_THREE',
                'E_D_CROSSBODY_MOUNTAIN_CLIMBER_TIP_FOUR'
            ],
            focus_areas=[FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.TIME_BASED
        ),
        # 33. Crunch
        ExerciseDefinition(
            id='exercise-56',
            title='E_D_CRUNCH_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/crunch.png'],
            preparation_steps=[
                'E_D_CRUNCH_PREP_ONE',
                'E_D_CRUNCH_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CRUNCH_EXEC_ONE',
                'E_D_CRUNCH_EXEC_TWO'
            ],
            key_tips=[
                'E_D_CRUNCH_TIP_ONE',
                'E_D_CRUNCH_TIP_TWO',
                'E_D_CRUNCH_TIP_THREE'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 34. Crunch: Legs on Stability Ball
        ExerciseDefinition(
            id='exercise-57',
            title='E_D_CRUNCH_LEGS_ON_STABILITY_BALL_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/crunch_legs_on_stability_ball.png'],
            preparation_steps=[
                'E_D_CRUNCH_LEGS_ON_STABILITY_BALL_PREP_ONE',
                'E_D_CRUNCH_LEGS_ON_STABILITY_BALL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CRUNCH_LEGS_ON_STABILITY_BALL_EXEC_ONE',
                'E_D_CRUNCH_LEGS_ON_STABILITY_BALL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_CRUNCH_LEGS_ON_STABILITY_BALL_TIP_ONE',
                'E_D_CRUNCH_LEGS_ON_STABILITY_BALL_TIP_TWO',
                'E_D_CRUNCH_LEGS_ON_STABILITY_BALL_TIP_THREE'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 35. Crunch: Machine
        ExerciseDefinition(
            id='exercise-58',
            title='E_D_CRUNCH_MACHINE_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/crunch_machine.png'],
            preparation_steps=[
                'E_D_CRUNCH_MACHINE_PREP_ONE',
                'E_D_CRUNCH_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CRUNCH_MACHINE_EXEC_ONE',
                'E_D_CRUNCH_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_CRUNCH_MACHINE_TIP_ONE',
                'E_D_CRUNCH_MACHINE_TIP_TWO',
                'E_D_CRUNCH_MACHINE_TIP_THREE'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 36. Cuban Rotation
        ExerciseDefinition(
            id='exercise-59',
            title='E_D_CUBAN_ROTATION_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/cuban_rotation.png'],
            preparation_steps=[
                'E_D_CUBAN_ROTATION_PREP_ONE',
                'E_D_CUBAN_ROTATION_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CUBAN_ROTATION_EXEC_ONE',
                'E_D_CUBAN_ROTATION_EXEC_TWO'
            ],
            key_tips=[
                'E_D_CUBAN_ROTATION_TIP_ONE',
                'E_D_CUBAN_ROTATION_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 37. Cuban Rotation: Band
        ExerciseDefinition(
            id='exercise-60',
            title='E_D_CUBAN_ROTATION_BAND_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/cuban_rotation_band.png'],
            preparation_steps=[
                'E_D_CUBAN_ROTATION_BAND_PREP_ONE',
                'E_D_CUBAN_ROTATION_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CUBAN_ROTATION_BAND_EXEC_ONE',
                'E_D_CUBAN_ROTATION_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_CUBAN_ROTATION_BAND_TIP_ONE',
                'E_D_CUBAN_ROTATION_BAND_TIP_TWO',
                'E_D_CUBAN_ROTATION_BAND_TIP_THREE'
            ],
            focus_areas=[FocusArea.BACK],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 38. Cuban Rotation: Dumbbell
        ExerciseDefinition(
            id='exercise-61',
            title='E_D_CUBAN_ROTATION_DUMBBELL_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/cuban_rotation_dumbbell.png'],
            preparation_steps=[
                'E_D_CUBAN_ROTATION_DUMBBELL_PREP_ONE',
                'E_D_CUBAN_ROTATION_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CUBAN_ROTATION_DUMBBELL_EXEC_ONE',
                'E_D_CUBAN_ROTATION_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_CUBAN_ROTATION_DUMBBELL_TIP_ONE',
                'E_D_CUBAN_ROTATION_DUMBBELL_TIP_TWO',
                'E_D_CUBAN_ROTATION_DUMBBELL_TIP_THREE'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 39. Curtsey Lunge
        ExerciseDefinition(
            id='exercise-62',
            title='E_D_CURTSEY_LUNGE_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/curtsey_lunge.png'],
            preparation_steps=[
                'E_D_CURTSEY_LUNGE_PREP_ONE',
                'E_D_CURTSEY_LUNGE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CURTSEY_LUNGE_EXEC_ONE',
                'E_D_CURTSEY_LUNGE_EXEC_TWO',
                'E_D_CURTSEY_LUNGE_EXEC_THREE',
                'E_D_CURTSEY_LUNGE_EXEC_FOUR'
            ],
            key_tips=[
                'E_D_CURTSEY_LUNGE_TIP_ONE',
                'E_D_CURTSEY_LUNGE_TIP_TWO',
                'E_D_CURTSEY_LUNGE_TIP_THREE'
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 40. Curtsey Lunge: Barbell
        ExerciseDefinition(
            id='exercise-63',
            title='E_D_CURTSEY_LUNGE_BARBELL_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/curtsey_lunge_barbell.png'],
            preparation_steps=[
                'E_D_CURTSEY_LUNGE_BARBELL_PREP_ONE',
                'E_D_CURTSEY_LUNGE_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CURTSEY_LUNGE_BARBELL_EXEC_ONE',
                'E_D_CURTSEY_LUNGE_BARBELL_EXEC_TWO',
                'E_D_CURTSEY_LUNGE_BARBELL_EXEC_THREE',
                'E_D_CURTSEY_LUNGE_BARBELL_EXEC_FOUR'
            ],
            key_tips=[
                'E_D_CURTSEY_LUNGE_BARBELL_TIP_ONE',
                'E_D_CURTSEY_LUNGE_BARBELL_TIP_TWO',
                'E_D_CURTSEY_LUNGE_BARBELL_TIP_THREE'
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        # 41. Curtsey Lunge: Dumbbell
        ExerciseDefinition(
            id='exercise-64',
            title='E_D_CURTSEY_LUNGE_DUMBBELL_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/curtsey_lunge_dumbbell.png'],
            preparation_steps=[
                'E_D_CURTSEY_LUNGE_DUMBBELL_PREP_ONE',
                'E_D_CURTSEY_LUNGE_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CURTSEY_LUNGE_DUMBBELL_EXEC_ONE',
                'E_D_CURTSEY_LUNGE_DUMBBELL_EXEC_TWO',
                'E_D_CURTSEY_LUNGE_DUMBBELL_EXEC_THREE',
                'E_D_CURTSEY_LUNGE_DUMBBELL_EXEC_FOUR'
            ],
            key_tips=[
                'E_D_CURTSEY_LUNGE_DUMBBELL_TIP_ONE',
                'E_D_CURTSEY_LUNGE_DUMBBELL_TIP_TWO',
                'E_D_CURTSEY_LUNGE_DUMBBELL_TIP_THREE'
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 42. Curtsey Lunge: Kettlebell
        ExerciseDefinition(
            id='exercise-65',
            title='E_D_CURTSEY_LUNGE_KETTLEBELL_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/curtsey_lunge_kettlebell.png'],
            preparation_steps=[
                'E_D_CURTSEY_LUNGE_KETTLEBELL_PREP_ONE',
                'E_D_CURTSEY_LUNGE_KETTLEBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_CURTSEY_LUNGE_KETTLEBELL_EXEC_ONE',
                'E_D_CURTSEY_LUNGE_KETTLEBELL_EXEC_TWO',
                'E_D_CURTSEY_LUNGE_KETTLEBELL_EXEC_THREE',
                'E_D_CURTSEY_LUNGE_KETTLEBELL_EXEC_FOUR'
            ],
            key_tips=[
                'E_D_CURTSEY_LUNGE_KETTLEBELL_TIP_ONE',
                'E_D_CURTSEY_LUNGE_KETTLEBELL_TIP_TWO',
                'E_D_CURTSEY_LUNGE_KETTLEBELL_TIP_THREE'
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
            equipment=ExerciseEquipment.KETTLEBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 43. Deadlift High Pull- Barbell
        ExerciseDefinition(
            id='exercise-66',
            title='E_D_DEADLIFT_HIGH_PULL_BARBELL_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/deadlift_high_pull_barbell.png'],
            preparation_steps=[
                'E_D_DEADLIFT_HIGH_PULL_BARBELL_PREP_ONE',
                'E_D_DEADLIFT_HIGH_PULL_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_DEADLIFT_HIGH_PULL_BARBELL_EXEC_ONE',
                'E_D_DEADLIFT_HIGH_PULL_BARBELL_EXEC_TWO',
                'E_D_DEADLIFT_HIGH_PULL_BARBELL_EXEC_THREE',
                'E_D_DEADLIFT_HIGH_PULL_BARBELL_EXEC_FOUR'
            ],
            key_tips=[
                'E_D_DEADLIFT_HIGH_PULL_BARBELL_TIP_ONE',
                'E_D_DEADLIFT_HIGH_PULL_BARBELL_TIP_TWO',
                'E_D_DEADLIFT_HIGH_PULL_BARBELL_TIP_THREE',
                'E_D_DEADLIFT_HIGH_PULL_BARBELL_TIP_FOUR'
            ],
            focus_areas=[FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        # 44. Deadlift - Band
        ExerciseDefinition(
            id='exercise-67',
            title='E_D_DEADLIFT_BAND_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/deadlift_band.png'],
            preparation_steps=[
                'E_D_DEADLIFT_BAND_PREP_ONE',
                'E_D_DEADLIFT_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_DEADLIFT_BAND_EXEC_ONE',
                'E_D_DEADLIFT_BAND_EXEC_TWO',
                'E_D_DEADLIFT_BAND_EXEC_THREE',
                'E_D_DEADLIFT_BAND_EXEC_FOUR'
            ],
            key_tips=[
                'E_D_DEADLIFT_BAND_TIP_ONE',
                'E_D_DEADLIFT_BAND_TIP_TWO',
                'E_D_DEADLIFT_BAND_TIP_THREE',
                'E_D_DEADLIFT_BAND_TIP_FOUR'
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.BACK, FocusArea.LEG],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 45. Deadlift - Barbell
        ExerciseDefinition(
            id='exercise-68',
            title='E_D_DEADLIFT_BARBELL_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/deadlift_barbell.png'],
            preparation_steps=[
                'E_D_DEADLIFT_BARBELL_PREP_ONE',
                'E_D_DEADLIFT_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_DEADLIFT_BARBELL_EXEC_ONE',
                'E_D_DEADLIFT_BARBELL_EXEC_TWO',
                'E_D_DEADLIFT_BARBELL_EXEC_THREE',
                'E_D_DEADLIFT_BARBELL_EXEC_FOUR'
            ],
            key_tips=[
                'E_D_DEADLIFT_BARBELL_TIP_ONE',
                'E_D_DEADLIFT_BARBELL_TIP_TWO',
                'E_D_DEADLIFT_BARBELL_TIP_THREE',
                'E_D_DEADLIFT_BARBELL_TIP_FOUR',
                'E_D_DEADLIFT_BARBELL_TIP_FIVE'
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.BACK, FocusArea.LEG],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        # 46. Deadlift - Dumbbell
        ExerciseDefinition(
            id='exercise-69',
            title='E_D_DEADLIFT_DUMBBELL_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/deadlift_dumbbell.png'],
            preparation_steps=[
                'E_D_DEADLIFT_DUMBBELL_PREP_ONE',
                'E_D_DEADLIFT_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_DEADLIFT_DUMBBELL_EXEC_ONE',
                'E_D_DEADLIFT_DUMBBELL_EXEC_TWO',
                'E_D_DEADLIFT_DUMBBELL_EXEC_THREE',
                'E_D_DEADLIFT_DUMBBELL_EXEC_FOUR'
            ],
            key_tips=[
                'E_D_DEADLIFT_DUMBBELL_TIP_ONE',
                'E_D_DEADLIFT_DUMBBELL_TIP_TWO',
                'E_D_DEADLIFT_DUMBBELL_TIP_THREE',
                'E_D_DEADLIFT_DUMBBELL_TIP_FOUR',
                'E_D_DEADLIFT_DUMBBELL_TIP_FIVE'
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.BACK, FocusArea.LEG],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 47. Deadlift - Kettlebell
        
        # 48. Deadlift - Smith Machine
        ExerciseDefinition(
            id='exercise-71',
            title='E_D_DEADLIFT_SMITH_MACHINE_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/deadlift_smith_machine.png'],
            preparation_steps=[
                'E_D_DEADLIFT_SMITH_MACHINE_PREP_ONE',
                'E_D_DEADLIFT_SMITH_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_DEADLIFT_SMITH_MACHINE_EXEC_ONE',
                'E_D_DEADLIFT_SMITH_MACHINE_EXEC_TWO',
                'E_D_DEADLIFT_SMITH_MACHINE_EXEC_THREE',
                'E_D_DEADLIFT_SMITH_MACHINE_EXEC_FOUR'
            ],
            key_tips=[
                'E_D_DEADLIFT_SMITH_MACHINE_TIP_ONE',
                'E_D_DEADLIFT_SMITH_MACHINE_TIP_TWO',
                'E_D_DEADLIFT_SMITH_MACHINE_TIP_THREE',
                'E_D_DEADLIFT_SMITH_MACHINE_TIP_FOUR',
                'E_D_DEADLIFT_SMITH_MACHINE_TIP_FIVE'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.BUTTOCKS, FocusArea.LEG],
            equipment=ExerciseEquipment.SMITH_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 49. Decline Bench Fly: Cable
        ExerciseDefinition(
            id='exercise-72',
            title='E_D_DECLINE_BENCH_FLY_CABLE_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/decline_bench_fly_cable.png'],
            preparation_steps=[
                'E_D_DECLINE_BENCH_FLY_CABLE_PREP_ONE',
                'E_D_DECLINE_BENCH_FLY_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_DECLINE_BENCH_FLY_CABLE_EXEC_ONE',
                'E_D_DECLINE_BENCH_FLY_CABLE_EXEC_TWO',
                'E_D_DECLINE_BENCH_FLY_CABLE_EXEC_THREE'
            ],
            key_tips=[
                'E_D_DECLINE_BENCH_FLY_CABLE_TIP_ONE',
                'E_D_DECLINE_BENCH_FLY_CABLE_TIP_TWO',
                'E_D_DECLINE_BENCH_FLY_CABLE_TIP_THREE'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 50. Decline Bench Fly: Dumbbell
        ExerciseDefinition(
            id='exercise-73',
            title='E_D_DECLINE_BENCH_FLY_DUMBBELL_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/decline_bench_fly_dumbbell.png'],
            preparation_steps=[
                'E_D_DECLINE_BENCH_FLY_DUMBBELL_PREP_ONE',
                'E_D_DECLINE_BENCH_FLY_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_DECLINE_BENCH_FLY_DUMBBELL_EXEC_ONE',
                'E_D_DECLINE_BENCH_FLY_DUMBBELL_EXEC_TWO',
                'E_D_DECLINE_BENCH_FLY_DUMBBELL_EXEC_THREE'
            ],
            key_tips=[
                'E_D_DECLINE_BENCH_FLY_DUMBBELL_TIP_ONE',
                'E_D_DECLINE_BENCH_FLY_DUMBBELL_TIP_TWO',
                'E_D_DECLINE_BENCH_FLY_DUMBBELL_TIP_THREE'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 51. Decline Bench Press: Barbell
        ExerciseDefinition(
            id='exercise-74',
            title='E_D_DECLINE_BENCH_PRESS_BARBELL_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/decline_bench_press_barbell.png'],
            preparation_steps=[
                'E_D_DECLINE_BENCH_PRESS_BARBELL_PREP_ONE',
                'E_D_DECLINE_BENCH_PRESS_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_DECLINE_BENCH_PRESS_BARBELL_EXEC_ONE',
                'E_D_DECLINE_BENCH_PRESS_BARBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_DECLINE_BENCH_PRESS_BARBELL_TIP_ONE',
                'E_D_DECLINE_BENCH_PRESS_BARBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.ARM, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        # 52. Decline Bench Press (Wide Grip)- Barbell
        ExerciseDefinition(
            id='exercise-75',
            title='E_D_DECLINE_BENCH_PRESS_WIDE_GRIP_BARBELL_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/decline_bench_press_wide_grip_barbell.png'],
            preparation_steps=[
                'E_D_DECLINE_BENCH_PRESS_WIDE_GRIP_BARBELL_PREP_ONE',
                'E_D_DECLINE_BENCH_PRESS_WIDE_GRIP_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_DECLINE_BENCH_PRESS_WIDE_GRIP_BARBELL_EXEC_ONE',
                'E_D_DECLINE_BENCH_PRESS_WIDE_GRIP_BARBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_DECLINE_BENCH_PRESS_WIDE_GRIP_BARBELL_TIP_ONE',
                'E_D_DECLINE_BENCH_PRESS_WIDE_GRIP_BARBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.ARM, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        # 53. Decline Bench Press: Cable
        ExerciseDefinition(
            id='exercise-76',
            title='E_D_DECLINE_BENCH_PRESS_CABLE_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/decline_bench_press_cable.png'],
            preparation_steps=[
                'E_D_DECLINE_BENCH_PRESS_CABLE_PREP_ONE',
                'E_D_DECLINE_BENCH_PRESS_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_DECLINE_BENCH_PRESS_CABLE_EXEC_ONE',
                'E_D_DECLINE_BENCH_PRESS_CABLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_DECLINE_BENCH_PRESS_CABLE_TIP_ONE',
                'E_D_DECLINE_BENCH_PRESS_CABLE_TIP_TWO'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.ARM, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 54. Decline Bench Press: Dumbbell
        ExerciseDefinition(
            id='exercise-77',
            title='E_D_DECLINE_BENCH_PRESS_DUMBBELL_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/decline_bench_press_dumbbell.png'],
            preparation_steps=[
                'E_D_DECLINE_BENCH_PRESS_DUMBBELL_PREP_ONE',
                'E_D_DECLINE_BENCH_PRESS_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_DECLINE_BENCH_PRESS_DUMBBELL_EXEC_ONE',
                'E_D_DECLINE_BENCH_PRESS_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_DECLINE_BENCH_PRESS_DUMBBELL_TIP_ONE',
                'E_D_DECLINE_BENCH_PRESS_DUMBBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.ARM, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 55. Decline Bench Press: Smith Machine
        ExerciseDefinition(
            id='exercise-78',
            title='E_D_DECLINE_BENCH_PRESS_SMITH_MACHINE_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/decline_bench_press_smith_machine.png'],
            preparation_steps=[
                'E_D_DECLINE_BENCH_PRESS_SMITH_MACHINE_PREP_ONE',
                'E_D_DECLINE_BENCH_PRESS_SMITH_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_DECLINE_BENCH_PRESS_SMITH_MACHINE_EXEC_ONE',
                'E_D_DECLINE_BENCH_PRESS_SMITH_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_DECLINE_BENCH_PRESS_SMITH_MACHINE_TIP_ONE',
                'E_D_DECLINE_BENCH_PRESS_SMITH_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.SMITH_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 56. Decline Bench Pullover Barbell
        ExerciseDefinition(
            id='exercise-79',
            title='E_D_DECLINE_BENCH_PULLOVER_BARBELL_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/decline_bench_pullover_barbell.png'],
            preparation_steps=[
                'E_D_DECLINE_BENCH_PULLOVER_BARBELL_PREP_ONE',
                'E_D_DECLINE_BENCH_PULLOVER_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_DECLINE_BENCH_PULLOVER_BARBELL_EXEC_ONE',
                'E_D_DECLINE_BENCH_PULLOVER_BARBELL_EXEC_TWO',
                'E_D_DECLINE_BENCH_PULLOVER_BARBELL_EXEC_THREE',
                'E_D_DECLINE_BENCH_PULLOVER_BARBELL_EXEC_FOUR'
            ],
            key_tips=[
                'E_D_DECLINE_BENCH_PULLOVER_BARBELL_TIP_ONE',
                'E_D_DECLINE_BENCH_PULLOVER_BARBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        # 57. Decline Bent Arm Pullover - Barbell
        ExerciseDefinition(
            id='exercise-80',
            title='E_D_DECLINE_BENT_ARM_PULLOVER_BARBELL_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/decline_bent_arm_pullover_barbell.png'],
            preparation_steps=[
                'E_D_DECLINE_BENT_ARM_PULLOVER_BARBELL_PREP_ONE',
                'E_D_DECLINE_BENT_ARM_PULLOVER_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_DECLINE_BENT_ARM_PULLOVER_BARBELL_EXEC_ONE',
                'E_D_DECLINE_BENT_ARM_PULLOVER_BARBELL_EXEC_TWO',
                'E_D_DECLINE_BENT_ARM_PULLOVER_BARBELL_EXEC_THREE',
                'E_D_DECLINE_BENT_ARM_PULLOVER_BARBELL_EXEC_FOUR'
            ],
            key_tips=[
                'E_D_DECLINE_BENT_ARM_PULLOVER_BARBELL_TIP_ONE',
                'E_D_DECLINE_BENT_ARM_PULLOVER_BARBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.ARM, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        # 58. Decline Crunch
        ExerciseDefinition(
            id='exercise-81',
            title='E_D_DECLINE_CRUNCH_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/decline_crunch.png'],
            preparation_steps=[
                'E_D_DECLINE_CRUNCH_PREP_ONE',
                'E_D_DECLINE_CRUNCH_PREP_TWO'
            ],
            execution_steps=[
                'E_D_DECLINE_CRUNCH_EXEC_ONE',
                'E_D_DECLINE_CRUNCH_EXEC_TWO'
            ],
            key_tips=[
                'E_D_DECLINE_CRUNCH_TIP_ONE',
                'E_D_DECLINE_CRUNCH_TIP_TWO',
                'E_D_DECLINE_CRUNCH_TIP_THREE'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 59. Decline Push Up
        ExerciseDefinition(
            id='exercise-82',
            title='E_D_DECLINE_PUSH_UP_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/decline_push_up.png'],
            preparation_steps=[
                'E_D_DECLINE_PUSH_UP_PREP_ONE',
                'E_D_DECLINE_PUSH_UP_PREP_TWO',
                'E_D_DECLINE_PUSH_UP_PREP_THREE'
            ],
            execution_steps=[
                'E_D_DECLINE_PUSH_UP_EXEC_ONE',
                'E_D_DECLINE_PUSH_UP_EXEC_TWO'
            ],
            key_tips=[
                'E_D_DECLINE_PUSH_UP_TIP_ONE',
                'E_D_DECLINE_PUSH_UP_TIP_TWO',
                'E_D_DECLINE_PUSH_UP_TIP_THREE'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.ARM],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 60. Decline Reverse Crunch
        ExerciseDefinition(
            id='exercise-83',
            title='E_D_DECLINE_REVERSE_CRUNCH_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/decline_reverse_crunch.png'],
            preparation_steps=[
                'E_D_DECLINE_REVERSE_CRUNCH_PREP_ONE',
                'E_D_DECLINE_REVERSE_CRUNCH_PREP_TWO'
            ],
            execution_steps=[
                'E_D_DECLINE_REVERSE_CRUNCH_EXEC_ONE',
                'E_D_DECLINE_REVERSE_CRUNCH_EXEC_TWO'
            ],
            key_tips=[
                'E_D_DECLINE_REVERSE_CRUNCH_TIP_ONE',
                'E_D_DECLINE_REVERSE_CRUNCH_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 61. Diamond Push-up
        ExerciseDefinition(
            id='exercise-84',
            title='E_D_DIAMOND_PUSHUP_TITLE',
            video_urls=[],
            cover_image_url=['regular_directory/exercises/images/diamond_push_up.png'],
            preparation_steps=[
                'E_D_DIAMOND_PUSHUP_PREP_ONE',
                'E_D_DIAMOND_PUSHUP_PREP_TWO'
            ],
            execution_steps=[
                'E_D_DIAMOND_PUSHUP_EXEC_ONE',
                'E_D_DIAMOND_PUSHUP_EXEC_TWO'
            ],
            key_tips=[
                'E_D_DIAMOND_PUSHUP_TIP_ONE',
                'E_D_DIAMOND_PUSHUP_TIP_TWO',
                'E_D_DIAMOND_PUSHUP_TIP_THREE'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.ARM],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
ExerciseDefinition(
			id='exercise-85',
			title= "E_D_DONKEY_KICK_TITLE",
			video_urls=['regular_directory/exercises/videos/donkey_kick.mp4'],
			cover_image_url=['regular_directory/exercises/images/donkey_kick.png'],
			preparation_steps=[
				'E_D_DONKEY_KICK_PREP_ONE'
			],
			execution_steps=[
				'E_D_DONKEY_KICK_EXEC_ONE',
				'E_D_DONKEY_KICK_EXEC_TWO',
				'E_D_DONKEY_KICK_EXEC_THREE',
				'E_D_DONKEY_KICK_EXEC_FOUR'
			],
			key_tips=[
				'E_D_DONKEY_KICK_TIP_ONE',
				'E_D_DONKEY_KICK_TIP_TWO',
				'E_D_DONKEY_KICK_TIP_THREE',
				'E_D_DONKEY_KICK_TIP_FOUR'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
			equipment=ExerciseEquipment.BODY_WEIGHT,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-86',
			title= "E_D_DONKEY_KICK_MACHINE_TITLE",
			video_urls=['regular_directory/exercises/videos/donkey_kick_machine.mp4'],
			cover_image_url=['regular_directory/exercises/images/donkey_kick_machine.png'],
			preparation_steps=[
				'E_D_DONKEY_KICK_MACHINE_PREP_ONE'
			],
			execution_steps=[
				'E_D_DONKEY_KICK_MACHINE_EXEC_ONE',
				'E_D_DONKEY_KICK_MACHINE_EXEC_TWO',
				'E_D_DONKEY_KICK_MACHINE_EXEC_THREE',
				'E_D_DONKEY_KICK_MACHINE_EXEC_FOUR'
			],
			key_tips=[
				'E_D_DONKEY_KICK_MACHINE_TIP_ONE',
				'E_D_DONKEY_KICK_MACHINE_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
			equipment=ExerciseEquipment.WEIGHT_MACHINE,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-87',
			title= "E_D_DOWN_UP_TWIST_BAND_TITLE",
			video_urls=['regular_directory/exercises/videos/down_up_twist_band.mp4'],
			cover_image_url=['regular_directory/exercises/images/down_up_twist_band.png'],
			preparation_steps=[
				'E_D_DOWN_UP_TWIST_BAND_PREP_ONE',
				'E_D_DOWN_UP_TWIST_BAND_PREP_TWO'
			],
			execution_steps=[
				'E_D_DOWN_UP_TWIST_BAND_EXEC_ONE',
				'E_D_DOWN_UP_TWIST_BAND_EXEC_TWO',
				'E_D_DOWN_UP_TWIST_BAND_EXEC_THREE'
			],
			key_tips=[
				'E_D_DOWN_UP_TWIST_BAND_TIP_ONE',
				'E_D_DOWN_UP_TWIST_BAND_TIP_TWO'
			],
			focus_areas=[FocusArea.ABDOMEN, FocusArea.ARM, FocusArea.SHOULDER],
			equipment=ExerciseEquipment.BAND,
			metric_type=ExerciseMetricType.TIME_BASED
		),
		ExerciseDefinition(
			id='exercise-88',
			title= "E_D_DOWN_UP_TWIST_CABLE_TITLE",
			video_urls=['regular_directory/exercises/videos/down_up_twist_cable.mp4'],
			cover_image_url=['regular_directory/exercises/images/down_up_twist_cable.png'],
			preparation_steps=[
				'E_D_DOWN_UP_TWIST_CABLE_PREP_ONE',
				'E_D_DOWN_UP_TWIST_CABLE_PREP_TWO'
			],
			execution_steps=[
				'E_D_DOWN_UP_TWIST_CABLE_EXEC_ONE',
				'E_D_DOWN_UP_TWIST_CABLE_EXEC_TWO',
				'E_D_DOWN_UP_TWIST_CABLE_EXEC_THREE'
			],
			key_tips=[
				'E_D_DOWN_UP_TWIST_CABLE_TIP_ONE',
				'E_D_DOWN_UP_TWIST_CABLE_TIP_TWO'
			],
			focus_areas=[FocusArea.ABDOMEN, FocusArea.ARM, FocusArea.SHOULDER],
			equipment=ExerciseEquipment.CABLE_MACHINE,
			metric_type=ExerciseMetricType.TIME_BASED
		),
		ExerciseDefinition(
			id='exercise-89',
			title= "E_D_DRAG_CURL_BARBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/drag_curl_barbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/drag_curl_barbell.png'],
			preparation_steps=[
				'E_D_DRAG_CURL_BARBELL_PREP_ONE',
				'E_D_DRAG_CURL_BARBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_DRAG_CURL_BARBELL_EXEC_ONE',
				'E_D_DRAG_CURL_BARBELL_EXEC_TWO'
			],
			key_tips=[
				'E_D_DRAG_CURL_BARBELL_TIP_ONE',
				'E_D_DRAG_CURL_BARBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.ARM],
			equipment=ExerciseEquipment.BARBELL,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-90',
			title= "E_D_DRAG_CURL_CABLE_TITLE",
			video_urls=['regular_directory/exercises/videos/drag_curl_cable.mp4'],
			cover_image_url=['regular_directory/exercises/images/drag_curl_cable.png'],
			preparation_steps=[
				'E_D_DRAG_CURL_CABLE_PREP_ONE',
				'E_D_DRAG_CURL_CABLE_PREP_TWO'
			],
			execution_steps=[
				'E_D_DRAG_CURL_CABLE_EXEC_ONE',
				'E_D_DRAG_CURL_CABLE_EXEC_TWO'
			],
			key_tips=[
				'E_D_DRAG_CURL_CABLE_TIP_ONE',
				'E_D_DRAG_CURL_CABLE_TIP_TWO'
			],
			focus_areas=[FocusArea.ARM],
			equipment=ExerciseEquipment.CABLE_MACHINE,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-91',
			title= "E_D_DRAG_CURL_DUMBBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/drag_curl_dumbbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/drag_curl_dumbbell.png'],
			preparation_steps=[
				'E_D_DRAG_CURL_DUMBBELL_PREP_ONE',
				'E_D_DRAG_CURL_DUMBBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_DRAG_CURL_DUMBBELL_EXEC_ONE',
				'E_D_DRAG_CURL_DUMBBELL_EXEC_TWO'
			],
			key_tips=[
				'E_D_DRAG_CURL_DUMBBELL_TIP_ONE',
				'E_D_DRAG_CURL_DUMBBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.ARM],
			equipment=ExerciseEquipment.DUMBBELL,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-92',
			title= "E_D_DUMBBELL_SWING_TITLE",
			video_urls=['regular_directory/exercises/videos/dumbbell_swing.mp4'],
			cover_image_url=['regular_directory/exercises/images/dumbbell_swing.png'],
			preparation_steps=[
				'E_D_DUMBBELL_SWING_PREP_ONE',
				'E_D_DUMBBELL_SWING_PREP_TWO'
			],
			execution_steps=[
				'E_D_DUMBBELL_SWING_EXEC_ONE',
				'E_D_DUMBBELL_SWING_EXEC_TWO',
				'E_D_DUMBBELL_SWING_EXEC_THREE'
			],
			key_tips=[
				'E_D_DUMBBELL_SWING_TIP_ONE',
				'E_D_DUMBBELL_SWING_TIP_TWO',
				'E_D_DUMBBELL_SWING_TIP_THREE'
			],
			focus_areas=[FocusArea.LEG, FocusArea.SHOULDER, FocusArea.BACK],
			equipment=ExerciseEquipment.DUMBBELL,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-93',
			title= "E_D_ELBOW_ARM_CIRCLES_TITLE",
			video_urls=['regular_directory/exercises/videos/elbow_arm_circles.mp4'],
			cover_image_url=['regular_directory/exercises/images/elbow_arm_circles.png'],
			preparation_steps=[
				'E_D_ELBOW_ARM_CIRCLES_PREP_ONE'
			],
			execution_steps=[
				'E_D_ELBOW_ARM_CIRCLES_EXEC_ONE',
				'E_D_ELBOW_ARM_CIRCLES_EXEC_TWO',
				'E_D_ELBOW_ARM_CIRCLES_EXEC_THREE'
			],
			key_tips=[
				'E_D_ELBOW_ARM_CIRCLES_TIP_ONE',
				'E_D_ELBOW_ARM_CIRCLES_TIP_TWO'
			],
			focus_areas=[FocusArea.ARM, FocusArea.SHOULDER],
			equipment=ExerciseEquipment.BODY_WEIGHT,
			metric_type=ExerciseMetricType.TIME_BASED
		),
		ExerciseDefinition(
			id='exercise-94',
			title= "E_D_EXTERNAL_ROTATION_BAND_TITLE",
			video_urls=['regular_directory/exercises/videos/external_rotation_band.mp4'],
			cover_image_url=['regular_directory/exercises/images/external_rotation_band.png'],
			preparation_steps=[
				'E_D_EXTERNAL_ROTATION_BAND_PREP_ONE',
				'E_D_EXTERNAL_ROTATION_BAND_PREP_TWO'
			],
			execution_steps=[
				'E_D_EXTERNAL_ROTATION_BAND_EXEC_ONE',
				'E_D_EXTERNAL_ROTATION_BAND_EXEC_TWO',
				'E_D_EXTERNAL_ROTATION_BAND_EXEC_THREE'
			],
			key_tips=[
				'E_D_EXTERNAL_ROTATION_BAND_TIP_ONE',
				'E_D_EXTERNAL_ROTATION_BAND_TIP_TWO'
			],
			focus_areas=[FocusArea.BACK, FocusArea.SHOULDER],
			equipment=ExerciseEquipment.BAND,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-95',
			title= "E_D_EXTERNAL_ROTATION_CABLE_TITLE",
			video_urls=['regular_directory/exercises/videos/external_rotation_cable.mp4'],
			cover_image_url=['regular_directory/exercises/images/external_rotation_cable.png'],
			preparation_steps=[
				'E_D_EXTERNAL_ROTATION_CABLE_PREP_ONE',
				'E_D_EXTERNAL_ROTATION_CABLE_PREP_TWO'
			],
			execution_steps=[
				'E_D_EXTERNAL_ROTATION_CABLE_EXEC_ONE',
				'E_D_EXTERNAL_ROTATION_CABLE_EXEC_TWO',
				'E_D_EXTERNAL_ROTATION_CABLE_EXEC_THREE'
			],
			key_tips=[
				'E_D_EXTERNAL_ROTATION_CABLE_TIP_ONE',
				'E_D_EXTERNAL_ROTATION_CABLE_TIP_TWO'
			],
			focus_areas=[FocusArea.BACK, FocusArea.SHOULDER],
			equipment=ExerciseEquipment.CABLE_MACHINE,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-96',
			title= "E_D_EXTERNAL_ROTATION_DUMBBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/external_rotation_dumbbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/external_rotation_dumbbell.png'],
			preparation_steps=[
				'E_D_EXTERNAL_ROTATION_DUMBBELL_PREP_ONE',
				'E_D_EXTERNAL_ROTATION_DUMBBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_EXTERNAL_ROTATION_DUMBBELL_EXEC_ONE',
				'E_D_EXTERNAL_ROTATION_DUMBBELL_EXEC_TWO',
				'E_D_EXTERNAL_ROTATION_DUMBBELL_EXEC_THREE'
			],
			key_tips=[
				'E_D_EXTERNAL_ROTATION_DUMBBELL_TIP_ONE',
				'E_D_EXTERNAL_ROTATION_DUMBBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.BACK, FocusArea.SHOULDER],
			equipment=ExerciseEquipment.DUMBBELL,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-97',
			title= "E_D_FACE_PULL_BAND_TITLE",
			video_urls=['regular_directory/exercises/videos/face_pull_band.mp4'],
			cover_image_url=['regular_directory/exercises/images/face_pull_band.png'],
			preparation_steps=[
				'E_D_FACE_PULL_BAND_PREP_ONE',
				'E_D_FACE_PULL_BAND_PREP_TWO'
			],
			execution_steps=[
				'E_D_FACE_PULL_BAND_EXEC_ONE',
				'E_D_FACE_PULL_BAND_EXEC_TWO'
			],
			key_tips=[
				'E_D_FACE_PULL_BAND_TIP_ONE',
				'E_D_FACE_PULL_BAND_TIP_TWO'
			],
			focus_areas=[FocusArea.BACK, FocusArea.SHOULDER],
			equipment=ExerciseEquipment.BAND,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-98',
			title= "E_D_FACE_PULL_CABLE_TITLE",
			video_urls=['regular_directory/exercises/videos/face_pull_cable.mp4'],
			cover_image_url=['regular_directory/exercises/images/face_pull_cable.png'],
			preparation_steps=[
				'E_D_FACE_PULL_CABLE_PREP_ONE',
				'E_D_FACE_PULL_CABLE_PREP_TWO'
			],
			execution_steps=[
				'E_D_FACE_PULL_CABLE_EXEC_ONE',
				'E_D_FACE_PULL_CABLE_EXEC_TWO'
			],
			key_tips=[
				'E_D_FACE_PULL_CABLE_TIP_ONE',
				'E_D_FACE_PULL_CABLE_TIP_TWO'
			],
			focus_areas=[FocusArea.BACK, FocusArea.SHOULDER],
			equipment=ExerciseEquipment.CABLE_MACHINE,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
	
		
		ExerciseDefinition(
			id='exercise-101',
			title= "E_D_FIRE_HYDRANT_TITLE",
			video_urls=['regular_directory/exercises/videos/fire_hydrant.mp4'],
			cover_image_url=['regular_directory/exercises/images/fire_hydrant.png'],
			preparation_steps=[
				'E_D_FIRE_HYDRANT_PREP_ONE'
			],
			execution_steps=[
				'E_D_FIRE_HYDRANT_EXEC_ONE',
				'E_D_FIRE_HYDRANT_EXEC_TWO',
				'E_D_FIRE_HYDRANT_EXEC_THREE',
				'E_D_FIRE_HYDRANT_EXEC_FOUR'
			],
			key_tips=[
				'E_D_FIRE_HYDRANT_TIP_ONE',
				'E_D_FIRE_HYDRANT_TIP_TWO',
				'E_D_FIRE_HYDRANT_TIP_THREE'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
			equipment=ExerciseEquipment.BODY_WEIGHT,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-102',
			title= "E_D_FLAT_AROUND_THE_WORLD_DUMBBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/flat_around_the_world_dumbbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/flat_around_the_world_dumbbell.png'],
			preparation_steps=[
				'E_D_FLAT_AROUND_THE_WORLD_DUMBBELL_PREP_ONE',
				'E_D_FLAT_AROUND_THE_WORLD_DUMBBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_FLAT_AROUND_THE_WORLD_DUMBBELL_EXEC_ONE',
				'E_D_FLAT_AROUND_THE_WORLD_DUMBBELL_EXEC_TWO'
			],
			key_tips=[
				'E_D_FLAT_AROUND_THE_WORLD_DUMBBELL_TIP_ONE',
				'E_D_FLAT_AROUND_THE_WORLD_DUMBBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER],
			equipment=ExerciseEquipment.DUMBBELL,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		
		ExerciseDefinition(
			id='exercise-104',
			title= "E_D_FLOOR_PRESS_BARBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/floor_press_barbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/floor_press_barbell.png'],
			preparation_steps=[
				'E_D_FLOOR_PRESS_BARBELL_PREP_ONE',
				'E_D_FLOOR_PRESS_BARBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_FLOOR_PRESS_BARBELL_EXEC_ONE',
				'E_D_FLOOR_PRESS_BARBELL_EXEC_TWO'
			],
			key_tips=[
				'E_D_FLOOR_PRESS_BARBELL_TIP_ONE',
				'E_D_FLOOR_PRESS_BARBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
			equipment=ExerciseEquipment.BARBELL,
			metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
		),
		ExerciseDefinition(
			id='exercise-105',
			title= "E_D_FRONT_RAISE_BAND_TITLE",
			video_urls=['regular_directory/exercises/videos/front_raise_band.mp4'],
			cover_image_url=['regular_directory/exercises/images/front_raise_band.png'],
			preparation_steps=[
				'E_D_FRONT_RAISE_BAND_PREP_ONE',
				'E_D_FRONT_RAISE_BAND_PREP_TWO'
			],
			execution_steps=[
				'E_D_FRONT_RAISE_BAND_EXEC_ONE',
				'E_D_FRONT_RAISE_BAND_EXEC_TWO'
			],
			key_tips=[
				'E_D_FRONT_RAISE_BAND_TIP_ONE',
				'E_D_FRONT_RAISE_BAND_TIP_TWO'
			],
			focus_areas=[FocusArea.SHOULDER],
			equipment=ExerciseEquipment.BAND,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-106',
			title= "E_D_FRONT_RAISE_BARBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/front_raise_barbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/front_raise_barbell.png'],
			preparation_steps=[
				'E_D_FRONT_RAISE_BARBELL_PREP_ONE',
				'E_D_FRONT_RAISE_BARBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_FRONT_RAISE_BARBELL_EXEC_ONE',
				'E_D_FRONT_RAISE_BARBELL_EXEC_TWO'
			],
			key_tips=[
				'E_D_FRONT_RAISE_BARBELL_TIP_ONE',
				'E_D_FRONT_RAISE_BARBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.SHOULDER],
			equipment=ExerciseEquipment.BARBELL,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-107',
			title= "E_D_FRONT_RAISE_CABLE_TITLE",
			video_urls=['regular_directory/exercises/videos/front_raise_cable.mp4'],
			cover_image_url=['regular_directory/exercises/images/front_raise_cable.png'],
			preparation_steps=[
				'E_D_FRONT_RAISE_CABLE_PREP_ONE',
				'E_D_FRONT_RAISE_CABLE_PREP_TWO'
			],
			execution_steps=[
				'E_D_FRONT_RAISE_CABLE_EXEC_ONE',
				'E_D_FRONT_RAISE_CABLE_EXEC_TWO'
			],
			key_tips=[
				'E_D_FRONT_RAISE_CABLE_TIP_ONE',
				'E_D_FRONT_RAISE_CABLE_TIP_TWO'
			],
			focus_areas=[FocusArea.SHOULDER],
			equipment=ExerciseEquipment.CABLE_MACHINE,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-108',
			title= "E_D_FRONT_RAISE_DUMBBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/front_raise_dumbbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/front_raise_dumbbell.png'],
			preparation_steps=[
				'E_D_FRONT_RAISE_DUMBBELL_PREP_ONE',
				'E_D_FRONT_RAISE_DUMBBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_FRONT_RAISE_DUMBBELL_EXEC_ONE',
				'E_D_FRONT_RAISE_DUMBBELL_EXEC_TWO'
			],
			key_tips=[
				'E_D_FRONT_RAISE_DUMBBELL_TIP_ONE',
				'E_D_FRONT_RAISE_DUMBBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.SHOULDER],
			equipment=ExerciseEquipment.DUMBBELL,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-109',
			title= "E_D_FRONT_RAISE_PLATE_TITLE",
			video_urls=['regular_directory/exercises/videos/front_raise_plate.mp4'],
			cover_image_url=['regular_directory/exercises/images/front_raise_plate.png'],
			preparation_steps=[
				'E_D_FRONT_RAISE_PLATE_PREP_ONE',
				'E_D_FRONT_RAISE_PLATE_PREP_TWO'
			],
			execution_steps=[
				'E_D_FRONT_RAISE_PLATE_EXEC_ONE',
				'E_D_FRONT_RAISE_PLATE_EXEC_TWO'
			],
			key_tips=[
				'E_D_FRONT_RAISE_PLATE_TIP_ONE',
				'E_D_FRONT_RAISE_PLATE_TIP_TWO'
			],
			focus_areas=[FocusArea.SHOULDER],
			equipment=ExerciseEquipment.WEIGHT_MACHINE,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-110',
			title= "E_D_FRONT_RAISE_BODYWEIGHT_TITLE",
			video_urls=['regular_directory/exercises/videos/front_raise.mp4'],
			cover_image_url=['regular_directory/exercises/images/front_raise.png'],
			preparation_steps=[
				'E_D_FRONT_RAISE_BODYWEIGHT_PREP_ONE',
				'E_D_FRONT_RAISE_BODYWEIGHT_PREP_TWO'
			],
			execution_steps=[
				'E_D_FRONT_RAISE_BODYWEIGHT_EXEC_ONE',
				'E_D_FRONT_RAISE_BODYWEIGHT_EXEC_TWO'
			],
			key_tips=[
				'E_D_FRONT_RAISE_BODYWEIGHT_TIP_ONE',
				'E_D_FRONT_RAISE_BODYWEIGHT_TIP_TWO'
			],
			focus_areas=[FocusArea.SHOULDER],
			equipment=ExerciseEquipment.BODY_WEIGHT,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-111',
			title= "E_D_FRONT_SQUAT_BARBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/front_squat_barbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/front_squat_barbell.png'],
			preparation_steps=[
				'E_D_FRONT_SQUAT_BARBELL_PREP_ONE',
				'E_D_FRONT_SQUAT_BARBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_FRONT_SQUAT_BARBELL_EXEC_ONE',
				'E_D_FRONT_SQUAT_BARBELL_EXEC_TWO'
			],
			key_tips=[
				'E_D_FRONT_SQUAT_BARBELL_TIP_ONE',
				'E_D_FRONT_SQUAT_BARBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG, FocusArea.ABDOMEN, FocusArea.BACK],
			equipment=ExerciseEquipment.BARBELL,
			metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
		),
		ExerciseDefinition(
			id='exercise-112',
			title= "E_D_FRONT_SQUAT_CABLE_TITLE",
			video_urls=['regular_directory/exercises/videos/front_squat_cable.mp4'],
			cover_image_url=['regular_directory/exercises/images/front_squat_cable.png'],
			preparation_steps=[
				'E_D_FRONT_SQUAT_CABLE_PREP_ONE',
				'E_D_FRONT_SQUAT_CABLE_PREP_TWO'
			],
			execution_steps=[
				'E_D_FRONT_SQUAT_CABLE_EXEC_ONE',
				'E_D_FRONT_SQUAT_CABLE_EXEC_TWO'
			],
			key_tips=[
				'E_D_FRONT_SQUAT_CABLE_TIP_ONE',
				'E_D_FRONT_SQUAT_CABLE_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG, FocusArea.ABDOMEN, FocusArea.BACK],
			equipment=ExerciseEquipment.CABLE_MACHINE,
			metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
		),
		ExerciseDefinition(
			id='exercise-113',
			title= "E_D_FRONT_SQUAT_KETTLEBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/front_squat_kettlebell.mp4'],
			cover_image_url=['regular_directory/exercises/images/front_squat_kettlebell.png'],
			preparation_steps=[
				'E_D_FRONT_SQUAT_KETTLEBELL_PREP_ONE',
				'E_D_FRONT_SQUAT_KETTLEBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_FRONT_SQUAT_KETTLEBELL_EXEC_ONE',
				'E_D_FRONT_SQUAT_KETTLEBELL_EXEC_TWO'
			],
			key_tips=[
				'E_D_FRONT_SQUAT_KETTLEBELL_TIP_ONE',
				'E_D_FRONT_SQUAT_KETTLEBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG, FocusArea.ABDOMEN, FocusArea.BACK],
			equipment=ExerciseEquipment.KETTLEBELL,
			metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
		),
		ExerciseDefinition(
			id='exercise-114',
			title= "E_D_FRONT_SQUAT_SMITH_MACHINE_TITLE",
			video_urls=['regular_directory/exercises/videos/front_squat_smith_machine.mp4'],
			cover_image_url=['regular_directory/exercises/images/front_squat_smith_machine.png'],
			preparation_steps=[
				'E_D_FRONT_SQUAT_SMITH_MACHINE_PREP_ONE',
				'E_D_FRONT_SQUAT_SMITH_MACHINE_PREP_TWO'
			],
			execution_steps=[
				'E_D_FRONT_SQUAT_SMITH_MACHINE_EXEC_ONE',
				'E_D_FRONT_SQUAT_SMITH_MACHINE_EXEC_TWO'
			],
			key_tips=[
				'E_D_FRONT_SQUAT_SMITH_MACHINE_TIP_ONE',
				'E_D_FRONT_SQUAT_SMITH_MACHINE_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG, FocusArea.ABDOMEN, FocusArea.BACK],
			equipment=ExerciseEquipment.SMITH_MACHINE,
			metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
		),
		ExerciseDefinition(
			id='exercise-115',
			title= "E_D_FRONT_SQUAT_DUMBBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/front_squat_dumbbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/front_squat_dumbbell.png'],
			preparation_steps=[
				'E_D_FRONT_SQUAT_DUMBBELL_PREP_ONE',
				'E_D_FRONT_SQUAT_DUMBBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_FRONT_SQUAT_DUMBBELL_EXEC_ONE',
				'E_D_FRONT_SQUAT_DUMBBELL_EXEC_TWO'
			],
			key_tips=[
				'E_D_FRONT_SQUAT_DUMBBELL_TIP_ONE',
				'E_D_FRONT_SQUAT_DUMBBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG, FocusArea.ABDOMEN, FocusArea.BACK],
			equipment=ExerciseEquipment.DUMBBELL,
			metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
		),
		ExerciseDefinition(
			id='exercise-116',
			title= "E_D_GLUTE_BRIDGE_DUMBBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/glute_bridge_dumbbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/glute_bridge_dumbbell.png'],
			preparation_steps=[
				'E_D_GLUTE_BRIDGE_DUMBBELL_PREP_ONE',
				'E_D_GLUTE_BRIDGE_DUMBBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_GLUTE_BRIDGE_DUMBBELL_EXEC_ONE',
				'E_D_GLUTE_BRIDGE_DUMBBELL_EXEC_TWO',
				'E_D_GLUTE_BRIDGE_DUMBBELL_EXEC_THREE'
			],
			key_tips=[
				'E_D_GLUTE_BRIDGE_DUMBBELL_TIP_ONE',
				'E_D_GLUTE_BRIDGE_DUMBBELL_TIP_TWO',
				'E_D_GLUTE_BRIDGE_DUMBBELL_TIP_THREE'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
			equipment=ExerciseEquipment.DUMBBELL,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-117',
			title= "E_D_GLUTE_BRIDGE_ABDUCTION_TITLE",
			video_urls=['regular_directory/exercises/videos/glute_bridge_abduction.mp4'],
			cover_image_url=['regular_directory/exercises/images/glute_bridge_abduction.png'],
			preparation_steps=[
				'E_D_GLUTE_BRIDGE_ABDUCTION_PREP_ONE',
				'E_D_GLUTE_BRIDGE_ABDUCTION_PREP_TWO'
			],
			execution_steps=[
				'E_D_GLUTE_BRIDGE_ABDUCTION_EXEC_ONE',
				'E_D_GLUTE_BRIDGE_ABDUCTION_EXEC_TWO',
				'E_D_GLUTE_BRIDGE_ABDUCTION_EXEC_THREE'
			],
			key_tips=[
				'E_D_GLUTE_BRIDGE_ABDUCTION_TIP_ONE',
				'E_D_GLUTE_BRIDGE_ABDUCTION_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
			equipment=ExerciseEquipment.BODY_WEIGHT,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-118',
			title= "E_D_GLUTE_BRIDGE_BARBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/glute_bridge_barbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/glute_bridge_barbell.png'],
			preparation_steps=[
				'E_D_GLUTE_BRIDGE_BARBELL_PREP_ONE',
				'E_D_GLUTE_BRIDGE_BARBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_GLUTE_BRIDGE_BARBELL_EXEC_ONE',
				'E_D_GLUTE_BRIDGE_BARBELL_EXEC_TWO',
				'E_D_GLUTE_BRIDGE_BARBELL_EXEC_THREE'
			],
			key_tips=[
				'E_D_GLUTE_BRIDGE_BARBELL_TIP_ONE',
				'E_D_GLUTE_BRIDGE_BARBELL_TIP_TWO',
				'E_D_GLUTE_BRIDGE_BARBELL_TIP_THREE'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
			equipment=ExerciseEquipment.BARBELL,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-119',
			title= "E_D_GLUTE_BRIDGE_FEET_ON_BENCH_BARBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/glute_bridge_feet_on_bench_barbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/glute_bridge_feet_on_bench_barbell.png'],
			preparation_steps=[
				'E_D_GLUTE_BRIDGE_FEET_ON_BENCH_BARBELL_PREP_ONE',
				'E_D_GLUTE_BRIDGE_FEET_ON_BENCH_BARBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_GLUTE_BRIDGE_FEET_ON_BENCH_BARBELL_EXEC_ONE',
				'E_D_GLUTE_BRIDGE_FEET_ON_BENCH_BARBELL_EXEC_TWO',
				'E_D_GLUTE_BRIDGE_FEET_ON_BENCH_BARBELL_EXEC_THREE'
			],
			key_tips=[
				'E_D_GLUTE_BRIDGE_FEET_ON_BENCH_BARBELL_TIP_ONE',
				'E_D_GLUTE_BRIDGE_FEET_ON_BENCH_BARBELL_TIP_TWO',
				'E_D_GLUTE_BRIDGE_FEET_ON_BENCH_BARBELL_TIP_THREE'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
			equipment=ExerciseEquipment.BARBELL,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-120',
			title= "E_D_GLUTE_BRIDGE_FEET_ON_BENCH_TITLE",
			video_urls=['regular_directory/exercises/videos/glute_bridge_feet_on_bench.mp4'],
			cover_image_url=['regular_directory/exercises/images/glute_bridge_feet_on_bench.png'],
			preparation_steps=[
				'E_D_GLUTE_BRIDGE_FEET_ON_BENCH_PREP_ONE',
				'E_D_GLUTE_BRIDGE_FEET_ON_BENCH_PREP_TWO'
			],
			execution_steps=[
				'E_D_GLUTE_BRIDGE_FEET_ON_BENCH_EXEC_ONE',
				'E_D_GLUTE_BRIDGE_FEET_ON_BENCH_EXEC_TWO',
				'E_D_GLUTE_BRIDGE_FEET_ON_BENCH_EXEC_THREE'
			],
			key_tips=[
				'E_D_GLUTE_BRIDGE_FEET_ON_BENCH_TIP_ONE',
				'E_D_GLUTE_BRIDGE_FEET_ON_BENCH_TIP_TWO',
				'E_D_GLUTE_BRIDGE_FEET_ON_BENCH_TIP_THREE'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
			equipment=ExerciseEquipment.BODY_WEIGHT,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-121',
			title= "E_D_GLUTE_BRIDGE_BODYWEIGHT_TITLE",
			video_urls=['regular_directory/exercises/videos/glute_bridge.mp4'],
			cover_image_url=['regular_directory/exercises/images/glute_bridge.png'],
			preparation_steps=[
				'E_D_GLUTE_BRIDGE_BODYWEIGHT_PREP_ONE'
			],
			execution_steps=[
				'E_D_GLUTE_BRIDGE_BODYWEIGHT_EXEC_ONE',
				'E_D_GLUTE_BRIDGE_BODYWEIGHT_EXEC_TWO',
				'E_D_GLUTE_BRIDGE_BODYWEIGHT_EXEC_THREE'
			],
			key_tips=[
				'E_D_GLUTE_BRIDGE_BODYWEIGHT_TIP_ONE',
				'E_D_GLUTE_BRIDGE_BODYWEIGHT_TIP_TWO',
				'E_D_GLUTE_BRIDGE_BODYWEIGHT_TIP_THREE'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
			equipment=ExerciseEquipment.BODY_WEIGHT,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-122',
			title= "E_D_GLUTE_FROG_BRIDGE_TITLE",
			video_urls=['regular_directory/exercises/videos/glute_frog_bridge.mp4'],
			cover_image_url=['regular_directory/exercises/images/glute_frog_bridge.png'],
			preparation_steps=[
				'E_D_GLUTE_FROG_BRIDGE_PREP_ONE'
			],
			execution_steps=[
				'E_D_GLUTE_FROG_BRIDGE_EXEC_ONE',
				'E_D_GLUTE_FROG_BRIDGE_EXEC_TWO',
				'E_D_GLUTE_FROG_BRIDGE_EXEC_THREE'
			],
			key_tips=[
				'E_D_GLUTE_FROG_BRIDGE_TIP_ONE',
				'E_D_GLUTE_FROG_BRIDGE_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
			equipment=ExerciseEquipment.BODY_WEIGHT,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-123',
			title= "E_D_GLUTE_HAM_RAISE_TITLE",
			video_urls=['regular_directory/exercises/videos/glute_ham_raise.mp4'],
			cover_image_url=['regular_directory/exercises/images/glute_ham_raise.png'],
			preparation_steps=[
				'E_D_GLUTE_HAM_RAISE_PREP_ONE',
				'E_D_GLUTE_HAM_RAISE_PREP_TWO'
			],
			execution_steps=[
				'E_D_GLUTE_HAM_RAISE_EXEC_ONE',
				'E_D_GLUTE_HAM_RAISE_EXEC_TWO'
			],
			key_tips=[
				'E_D_GLUTE_HAM_RAISE_TIP_ONE',
				'E_D_GLUTE_HAM_RAISE_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BACK],
			equipment=ExerciseEquipment.WEIGHT_MACHINE,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-124',
			title= "E_D_GLUTE_KICKBACK_BAND_TITLE",
			video_urls=['regular_directory/exercises/videos/glute_kickback_band.mp4'],
			cover_image_url=['regular_directory/exercises/images/glute_kickback_band.png'],
			preparation_steps=[
				'E_D_GLUTE_KICKBACK_BAND_PREP_ONE',
				'E_D_GLUTE_KICKBACK_BAND_PREP_TWO'
			],
			execution_steps=[
				'E_D_GLUTE_KICKBACK_BAND_EXEC_ONE',
				'E_D_GLUTE_KICKBACK_BAND_EXEC_TWO',
				'E_D_GLUTE_KICKBACK_BAND_EXEC_THREE',
				'E_D_GLUTE_KICKBACK_BAND_EXEC_FOUR'
			],
			key_tips=[
				'E_D_GLUTE_KICKBACK_BAND_TIP_ONE',
				'E_D_GLUTE_KICKBACK_BAND_TIP_TWO',
				'E_D_GLUTE_KICKBACK_BAND_TIP_THREE'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
			equipment=ExerciseEquipment.BAND,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-125',
			title= "E_D_GLUTE_KICKBACK_TITLE",
			video_urls=['regular_directory/exercises/videos/glute_kickback.mp4'],
			cover_image_url=['regular_directory/exercises/images/glute_kickback.png'],
			preparation_steps=[
				'E_D_GLUTE_KICKBACK_PREP_ONE'
			],
			execution_steps=[
				'E_D_GLUTE_KICKBACK_EXEC_ONE',
				'E_D_GLUTE_KICKBACK_EXEC_TWO',
				'E_D_GLUTE_KICKBACK_EXEC_THREE',
				'E_D_GLUTE_KICKBACK_EXEC_FOUR'
			],
			key_tips=[
				'E_D_GLUTE_KICKBACK_TIP_ONE',
				'E_D_GLUTE_KICKBACK_TIP_TWO',
				'E_D_GLUTE_KICKBACK_TIP_THREE'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
			equipment=ExerciseEquipment.BODY_WEIGHT,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-126',
			title= "E_D_GOOD_MORNING_BAND_TITLE",
			video_urls=['regular_directory/exercises/videos/good_morning_band.mp4'],
			cover_image_url=['regular_directory/exercises/images/good_morning_band.png'],
			preparation_steps=[
				'E_D_GOOD_MORNING_BAND_PREP_ONE',
				'E_D_GOOD_MORNING_BAND_PREP_TWO'
			],
			execution_steps=[
				'E_D_GOOD_MORNING_BAND_EXEC_ONE',
				'E_D_GOOD_MORNING_BAND_EXEC_TWO'
			],
			key_tips=[
				'E_D_GOOD_MORNING_BAND_TIP_ONE',
				'E_D_GOOD_MORNING_BAND_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BACK],
			equipment=ExerciseEquipment.BAND,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-127',
			title= "E_D_GOOD_MORNING_BARBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/good_morning_barbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/good_morning_barbell.png'],
			preparation_steps=[
				'E_D_GOOD_MORNING_BARBELL_PREP_ONE',
				'E_D_GOOD_MORNING_BARBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_GOOD_MORNING_BARBELL_EXEC_ONE',
				'E_D_GOOD_MORNING_BARBELL_EXEC_TWO'
			],
			key_tips=[
				'E_D_GOOD_MORNING_BARBELL_TIP_ONE',
				'E_D_GOOD_MORNING_BARBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BACK],
			equipment=ExerciseEquipment.BARBELL,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-128',
			title= "E_D_GOOD_MORNING_SMITH_MACHINE_TITLE",
			video_urls=['regular_directory/exercises/videos/good_morning_smith_machine.mp4'],
			cover_image_url=['regular_directory/exercises/images/good_morning_smith_machine.png'],
			preparation_steps=[
				'E_D_GOOD_MORNING_SMITH_MACHINE_PREP_ONE',
				'E_D_GOOD_MORNING_SMITH_MACHINE_PREP_TWO'
			],
			execution_steps=[
				'E_D_GOOD_MORNING_SMITH_MACHINE_EXEC_ONE',
				'E_D_GOOD_MORNING_SMITH_MACHINE_EXEC_TWO'
			],
			key_tips=[
				'E_D_GOOD_MORNING_SMITH_MACHINE_TIP_ONE',
				'E_D_GOOD_MORNING_SMITH_MACHINE_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BACK],
			equipment=ExerciseEquipment.SMITH_MACHINE,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-129',
			title= "E_D_GORILLA_CHIN_CRUNCH_TITLE",
			video_urls=['regular_directory/exercises/videos/gorilla_chin_crunch.mp4'],
			cover_image_url=['regular_directory/exercises/images/gorilla_chin_crunch.png'],
			preparation_steps=[
				'E_D_GORILLA_CHIN_CRUNCH_PREP_ONE',
				'E_D_GORILLA_CHIN_CRUNCH_PREP_TWO'
			],
			execution_steps=[
				'E_D_GORILLA_CHIN_CRUNCH_EXEC_ONE',
				'E_D_GORILLA_CHIN_CRUNCH_EXEC_TWO',
				'E_D_GORILLA_CHIN_CRUNCH_EXEC_THREE'
			],
			key_tips=[
				'E_D_GORILLA_CHIN_CRUNCH_TIP_ONE',
				'E_D_GORILLA_CHIN_CRUNCH_TIP_TWO'
			],
			focus_areas=[FocusArea.ARM, FocusArea.BACK, FocusArea.ABDOMEN],
			equipment=ExerciseEquipment.BODY_WEIGHT,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-130',
			title= "E_D_HACK_SQUAT_BARBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/hack_squat_barbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/hack_squat_barbell.png'],
			preparation_steps=[
				'E_D_HACK_SQUAT_BARBELL_PREP_ONE',
				'E_D_HACK_SQUAT_BARBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_HACK_SQUAT_BARBELL_EXEC_ONE',
				'E_D_HACK_SQUAT_BARBELL_EXEC_TWO'
			],
			key_tips=[
				'E_D_HACK_SQUAT_BARBELL_TIP_ONE',
				'E_D_HACK_SQUAT_BARBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG],
			equipment=ExerciseEquipment.BARBELL,
			metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
		),
		ExerciseDefinition(
			id='exercise-131',
			title= "E_D_HACK_SQUAT_MACHINE_TITLE",
			video_urls=['regular_directory/exercises/videos/hack_squat_machine.mp4'],
			cover_image_url=['regular_directory/exercises/images/hack_squat_machine.png'],
			preparation_steps=[
				'E_D_HACK_SQUAT_MACHINE_PREP_ONE',
				'E_D_HACK_SQUAT_MACHINE_PREP_TWO'
			],
			execution_steps=[
				'E_D_HACK_SQUAT_MACHINE_EXEC_ONE',
				'E_D_HACK_SQUAT_MACHINE_EXEC_TWO'
			],
			key_tips=[
				'E_D_HACK_SQUAT_MACHINE_TIP_ONE',
				'E_D_HACK_SQUAT_MACHINE_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG],
			equipment=ExerciseEquipment.WEIGHT_MACHINE,
			metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
		),
		ExerciseDefinition(
			id='exercise-132',
			title= "E_D_HAMMER_CURL_BAND_TITLE",
			video_urls=['regular_directory/exercises/videos/hammer_curl_band.mp4'],
			cover_image_url=['regular_directory/exercises/images/hammer_curl_band.png'],
			preparation_steps=[
				'E_D_HAMMER_CURL_BAND_PREP_ONE',
				'E_D_HAMMER_CURL_BAND_PREP_TWO'
			],
			execution_steps=[
				'E_D_HAMMER_CURL_BAND_EXEC_ONE',
				'E_D_HAMMER_CURL_BAND_EXEC_TWO'
			],
			key_tips=[
				'E_D_HAMMER_CURL_BAND_TIP_ONE',
				'E_D_HAMMER_CURL_BAND_TIP_TWO'
			],
			focus_areas=[FocusArea.ARM],
			equipment=ExerciseEquipment.BAND,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-133',
			title= "E_D_HAMMER_CURL_CABLE_TITLE",
			video_urls=['regular_directory/exercises/videos/hammer_curl_cable.mp4'],
			cover_image_url=['regular_directory/exercises/images/hammer_curl_cable.png'],
			preparation_steps=[
				'E_D_HAMMER_CURL_CABLE_PREP_ONE',
				'E_D_HAMMER_CURL_CABLE_PREP_TWO'
			],
			execution_steps=[
				'E_D_HAMMER_CURL_CABLE_EXEC_ONE',
				'E_D_HAMMER_CURL_CABLE_EXEC_TWO'
			],
			key_tips=[
				'E_D_HAMMER_CURL_CABLE_TIP_ONE',
				'E_D_HAMMER_CURL_CABLE_TIP_TWO'
			],
			focus_areas=[FocusArea.ARM],
			equipment=ExerciseEquipment.CABLE_MACHINE,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-134',
			title= "E_D_HAMMER_CURL_DUMBBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/hammer_curl_dumbbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/hammer_curl_dumbbell.png'],
			preparation_steps=[
				'E_D_HAMMER_CURL_DUMBBELL_PREP_ONE',
				'E_D_HAMMER_CURL_DUMBBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_HAMMER_CURL_DUMBBELL_EXEC_ONE',
				'E_D_HAMMER_CURL_DUMBBELL_EXEC_TWO'
			],
			key_tips=[
				'E_D_HAMMER_CURL_DUMBBELL_TIP_ONE',
				'E_D_HAMMER_CURL_DUMBBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.ARM],
			equipment=ExerciseEquipment.DUMBBELL,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-135',
			title= "E_D_HANG_CLEAN_BARBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/hang_clean_barbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/hang_clean_barbell.png'],
			preparation_steps=[
				'E_D_HANG_CLEAN_BARBELL_PREP_ONE',
				'E_D_HANG_CLEAN_BARBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_HANG_CLEAN_BARBELL_EXEC_ONE',
				'E_D_HANG_CLEAN_BARBELL_EXEC_TWO',
				'E_D_HANG_CLEAN_BARBELL_EXEC_THREE'
			],
			key_tips=[
				'E_D_HANG_CLEAN_BARBELL_TIP_ONE',
				'E_D_HANG_CLEAN_BARBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.FULL_BODY],
			equipment=ExerciseEquipment.BARBELL,
			metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
		),
		ExerciseDefinition(
			id='exercise-136',
			title= "E_D_HANG_SNATCH_BARBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/hang_snatch_barbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/hang_snatch_barbell.png'],
			preparation_steps=[
				'E_D_HANG_SNATCH_BARBELL_PREP_ONE',
				'E_D_HANG_SNATCH_BARBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_HANG_SNATCH_BARBELL_EXEC_ONE',
				'E_D_HANG_SNATCH_BARBELL_EXEC_TWO',
				'E_D_HANG_SNATCH_BARBELL_EXEC_THREE'
			],
			key_tips=[
				'E_D_HANG_SNATCH_BARBELL_TIP_ONE',
				'E_D_HANG_SNATCH_BARBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.FULL_BODY],
			equipment=ExerciseEquipment.BARBELL,
			metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
		),
		ExerciseDefinition(
			id='exercise-137',
			title= "E_D_HANGING_KNEE_RAISE_TITLE",
			video_urls=['regular_directory/exercises/videos/hanging_knee_raise.mp4'],
			cover_image_url=['regular_directory/exercises/images/hanging_knee_raise.png'],
			preparation_steps=[
				'E_D_HANGING_KNEE_RAISE_PREP_ONE'
			],
			execution_steps=[
				'E_D_HANGING_KNEE_RAISE_EXEC_ONE',
				'E_D_HANGING_KNEE_RAISE_EXEC_TWO'
			],
			key_tips=[
				'E_D_HANGING_KNEE_RAISE_TIP_ONE',
				'E_D_HANGING_KNEE_RAISE_TIP_TWO'
			],
			focus_areas=[FocusArea.ABDOMEN, FocusArea.ARM],
			equipment=ExerciseEquipment.BODY_WEIGHT,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-138',
			title= "E_D_HANGING_LEG_RAISE_TWIST_TITLE",
			video_urls=['regular_directory/exercises/videos/hanging_leg_raise_twist.mp4'],
			cover_image_url=['regular_directory/exercises/images/hanging_leg_raise_twist.png'],
			preparation_steps=[
				'E_D_HANGING_LEG_RAISE_TWIST_PREP_ONE'
			],
			execution_steps=[
				'E_D_HANGING_LEG_RAISE_TWIST_EXEC_ONE',
				'E_D_HANGING_LEG_RAISE_TWIST_EXEC_TWO'
			],
			key_tips=[
				'E_D_HANGING_LEG_RAISE_TWIST_TIP_ONE',
				'E_D_HANGING_LEG_RAISE_TWIST_TIP_TWO'
			],
			focus_areas=[FocusArea.ABDOMEN, FocusArea.ARM],
			equipment=ExerciseEquipment.BODY_WEIGHT,
			metric_type=ExerciseMetricType.TIME_BASED
		),
		ExerciseDefinition(
			id='exercise-139',
			title= "E_D_HANGING_LEG_RAISE_TITLE",
			video_urls=['regular_directory/exercises/videos/hanging_leg_raise.mp4'],
			cover_image_url=['regular_directory/exercises/images/hanging_leg_raise.png'],
			preparation_steps=[
				'E_D_HANGING_LEG_RAISE_PREP_ONE'
			],
			execution_steps=[
				'E_D_HANGING_LEG_RAISE_EXEC_ONE',
				'E_D_HANGING_LEG_RAISE_EXEC_TWO'
			],
			key_tips=[
				'E_D_HANGING_LEG_RAISE_TIP_ONE',
				'E_D_HANGING_LEG_RAISE_TIP_TWO'
			],
			focus_areas=[FocusArea.ABDOMEN, FocusArea.ARM],
			equipment=ExerciseEquipment.BODY_WEIGHT,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-140',
			title= "E_D_HEEL_TOUCH_TITLE",
			video_urls=['regular_directory/exercises/videos/heel_touch.mp4'],
			cover_image_url=['regular_directory/exercises/images/heel_touch.png'],
			preparation_steps=[
				'E_D_HEEL_TOUCH_PREP_ONE',
				'E_D_HEEL_TOUCH_PREP_TWO'
			],
			execution_steps=[
				'E_D_HEEL_TOUCH_EXEC_ONE',
				'E_D_HEEL_TOUCH_EXEC_TWO',
				'E_D_HEEL_TOUCH_EXEC_THREE'
			],
			key_tips=[
				'E_D_HEEL_TOUCH_TIP_ONE',
				'E_D_HEEL_TOUCH_TIP_TWO'
			],
			focus_areas=[FocusArea.ABDOMEN],
			equipment=ExerciseEquipment.BODY_WEIGHT,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-141',
			title= "E_D_HIGH_KNEE_SKIPS_TITLE",
			video_urls=['regular_directory/exercises/videos/high_knee_skips.mp4'],
			cover_image_url=['regular_directory/exercises/images/high_knee_skips.png'],
			preparation_steps=[
				'E_D_HIGH_KNEE_SKIPS_PREP_ONE'
			],
			execution_steps=[
				'E_D_HIGH_KNEE_SKIPS_EXEC_ONE',
				'E_D_HIGH_KNEE_SKIPS_EXEC_TWO'
			],
			key_tips=[
				'E_D_HIGH_KNEE_SKIPS_TIP_ONE',
				'E_D_HIGH_KNEE_SKIPS_TIP_TWO'
			],
			focus_areas=[FocusArea.FULL_BODY],
			equipment=ExerciseEquipment.BODY_WEIGHT,
			metric_type=ExerciseMetricType.TIME_BASED
		),
		ExerciseDefinition(
			id='exercise-142',
			title= "E_D_HIP_ABDUCTOR_BAND_TITLE",
			video_urls=['regular_directory/exercises/videos/hip_abductor_band.mp4'],
			cover_image_url=['regular_directory/exercises/images/hip_abductor_band.png'],
			preparation_steps=[
				'E_D_HIP_ABDUCTOR_BAND_PREP_ONE',
				'E_D_HIP_ABDUCTOR_BAND_PREP_TWO'
			],
			execution_steps=[
				'E_D_HIP_ABDUCTOR_BAND_EXEC_ONE',
				'E_D_HIP_ABDUCTOR_BAND_EXEC_TWO',
				'E_D_HIP_ABDUCTOR_BAND_EXEC_THREE',
				'E_D_HIP_ABDUCTOR_BAND_EXEC_FOUR'
			],
			key_tips=[
				'E_D_HIP_ABDUCTOR_BAND_TIP_ONE',
				'E_D_HIP_ABDUCTOR_BAND_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
			equipment=ExerciseEquipment.BAND,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-143',
			title= "E_D_HIP_ABDUCTOR_CABLE_TITLE",
			video_urls=['regular_directory/exercises/videos/hip_abductor_cable.mp4'],
			cover_image_url=['regular_directory/exercises/images/hip_abductor_cable.png'],
			preparation_steps=[
				'E_D_HIP_ABDUCTOR_CABLE_PREP_ONE',
				'E_D_HIP_ABDUCTOR_CABLE_PREP_TWO'
			],
			execution_steps=[
				'E_D_HIP_ABDUCTOR_CABLE_EXEC_ONE',
				'E_D_HIP_ABDUCTOR_CABLE_EXEC_TWO',
				'E_D_HIP_ABDUCTOR_CABLE_EXEC_THREE',
				'E_D_HIP_ABDUCTOR_CABLE_EXEC_FOUR'
			],
			key_tips=[
				'E_D_HIP_ABDUCTOR_CABLE_TIP_ONE',
				'E_D_HIP_ABDUCTOR_CABLE_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
			equipment=ExerciseEquipment.CABLE_MACHINE,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-144',
			title= "E_D_HIP_ADDUCTOR_MACHINE_TITLE",
			video_urls=['regular_directory/exercises/videos/hip_adductor_machine.mp4'],
			cover_image_url=['regular_directory/exercises/images/hip_adductor_machine.png'],
			preparation_steps=[
				'E_D_HIP_ADDUCTOR_MACHINE_PREP_ONE',
				'E_D_HIP_ADDUCTOR_MACHINE_PREP_TWO'
			],
			execution_steps=[
				'E_D_HIP_ADDUCTOR_MACHINE_EXEC_ONE',
				'E_D_HIP_ADDUCTOR_MACHINE_EXEC_TWO'
			],
			key_tips=[
				'E_D_HIP_ADDUCTOR_MACHINE_TIP_ONE',
				'E_D_HIP_ADDUCTOR_MACHINE_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG],
			equipment=ExerciseEquipment.WEIGHT_MACHINE,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-145',
			title= "E_D_HIP_EXTENSION_MACHINE_TITLE",
			video_urls=['regular_directory/exercises/videos/hip_extension_machine.mp4'],
			cover_image_url=['regular_directory/exercises/images/hip_extension_machine.png'],
			preparation_steps=[
				'E_D_HIP_EXTENSION_MACHINE_PREP_ONE',
				'E_D_HIP_EXTENSION_MACHINE_PREP_TWO'
			],
			execution_steps=[
				'E_D_HIP_EXTENSION_MACHINE_EXEC_ONE',
				'E_D_HIP_EXTENSION_MACHINE_EXEC_TWO'
			],
			key_tips=[
				'E_D_HIP_EXTENSION_MACHINE_TIP_ONE',
				'E_D_HIP_EXTENSION_MACHINE_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
			equipment=ExerciseEquipment.WEIGHT_MACHINE,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-146',
			title= "E_D_HIP_FLEXION_BAND_TITLE",
			video_urls=['regular_directory/exercises/videos/hip_flexion_band.mp4'],
			cover_image_url=['regular_directory/exercises/images/hip_flexion_band.png'],
			preparation_steps=[
				'E_D_HIP_FLEXION_BAND_PREP_ONE',
				'E_D_HIP_FLEXION_BAND_PREP_TWO'
			],
			execution_steps=[
				'E_D_HIP_FLEXION_BAND_EXEC_ONE',
				'E_D_HIP_FLEXION_BAND_EXEC_TWO',
				'E_D_HIP_FLEXION_BAND_EXEC_THREE',
				'E_D_HIP_FLEXION_BAND_EXEC_FOUR'
			],
			key_tips=[
				'E_D_HIP_FLEXION_BAND_TIP_ONE',
				'E_D_HIP_FLEXION_BAND_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG],
			equipment=ExerciseEquipment.BAND,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-147',
			title= "E_D_HIP_FLEXION_MACHINE_TITLE",
			video_urls=['regular_directory/exercises/videos/hip_flexion_machine.mp4'],
			cover_image_url=['regular_directory/exercises/images/hip_flexion_machine.png'],
			preparation_steps=[
				'E_D_HIP_FLEXION_MACHINE_PREP_ONE',
				'E_D_HIP_FLEXION_MACHINE_PREP_TWO'
			],
			execution_steps=[
				'E_D_HIP_FLEXION_MACHINE_EXEC_ONE',
				'E_D_HIP_FLEXION_MACHINE_EXEC_TWO'
			],
			key_tips=[
				'E_D_HIP_FLEXION_MACHINE_TIP_ONE',
				'E_D_HIP_FLEXION_MACHINE_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG],
			equipment=ExerciseEquipment.WEIGHT_MACHINE,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		
		ExerciseDefinition(
			id='exercise-149',
			title= "E_D_HIP_FROG_EXTENSION_TITLE",
			video_urls=['regular_directory/exercises/videos/hip_frog_extension.mp4'],
			cover_image_url=['regular_directory/exercises/images/hip_frog_extension.png'],
			preparation_steps=[
				'E_D_HIP_FROG_EXTENSION_PREP_ONE',
				'E_D_HIP_FROG_EXTENSION_PREP_TWO'
			],
			execution_steps=[
				'E_D_HIP_FROG_EXTENSION_EXEC_ONE',
				'E_D_HIP_FROG_EXTENSION_EXEC_TWO'
			],
			key_tips=[
				'E_D_HIP_FROG_EXTENSION_TIP_ONE',
				'E_D_HIP_FROG_EXTENSION_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
			equipment=ExerciseEquipment.BODY_WEIGHT,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-150',
			title= "E_D_HIP_THRUST_BARBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/hip_thrust_barbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/hip_thrust_barbell.png'],
			preparation_steps=[
				'E_D_HIP_THRUST_BARBELL_PREP_ONE',
				'E_D_HIP_THRUST_BARBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_HIP_THRUST_BARBELL_EXEC_ONE',
				'E_D_HIP_THRUST_BARBELL_EXEC_TWO',
				'E_D_HIP_THRUST_BARBELL_EXEC_THREE'
			],
			key_tips=[
				'E_D_HIP_THRUST_BARBELL_TIP_ONE',
				'E_D_HIP_THRUST_BARBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
			equipment=ExerciseEquipment.BARBELL,
			metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
		),
		ExerciseDefinition(
			id='exercise-151',
			title= "E_D_HIP_THRUST_CABLE_TITLE",
			video_urls=['regular_directory/exercises/videos/hip_thrust_cable.mp4'],
			cover_image_url=['regular_directory/exercises/images/hip_thrust_cable.png'],
			preparation_steps=[
				'E_D_HIP_THRUST_CABLE_PREP_ONE',
				'E_D_HIP_THRUST_CABLE_PREP_TWO'
			],
			execution_steps=[
				'E_D_HIP_THRUST_CABLE_EXEC_ONE',
				'E_D_HIP_THRUST_CABLE_EXEC_TWO',
				'E_D_HIP_THRUST_CABLE_EXEC_THREE'
			],
			key_tips=[
				'E_D_HIP_THRUST_CABLE_TIP_ONE',
				'E_D_HIP_THRUST_CABLE_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
			equipment=ExerciseEquipment.CABLE_MACHINE,
			metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
		),
		
		ExerciseDefinition(
			id='exercise-153',
			title= "E_D_HIP_THRUST_TITLE",
			video_urls=['regular_directory/exercises/videos/hip_thrust.mp4'],
			cover_image_url=['regular_directory/exercises/images/hip_thrust.png'],
			preparation_steps=[
				'E_D_HIP_THRUST_PREP_ONE',
				'E_D_HIP_THRUST_PREP_TWO'
			],
			execution_steps=[
				'E_D_HIP_THRUST_EXEC_ONE',
				'E_D_HIP_THRUST_EXEC_TWO',
				'E_D_HIP_THRUST_EXEC_THREE'
			],
			key_tips=[
				'E_D_HIP_THRUST_TIP_ONE',
				'E_D_HIP_THRUST_TIP_TWO'
			],
			focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
			equipment=ExerciseEquipment.BODY_WEIGHT,
			metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
		),
		
		ExerciseDefinition(
			id='exercise-155',
			title= "E_D_INCLINE_BENCH_FLY_CABLE_TITLE",
			video_urls=['regular_directory/exercises/videos/incline_bench_fly_cable.mp4'],
			cover_image_url=['regular_directory/exercises/images/incline_bench_fly_cable.png'],
			preparation_steps=[
				'E_D_INCLINE_BENCH_FLY_CABLE_PREP_ONE',
				'E_D_INCLINE_BENCH_FLY_CABLE_PREP_TWO'
			],
			execution_steps=[
				'E_D_INCLINE_BENCH_FLY_CABLE_EXEC_ONE',
				'E_D_INCLINE_BENCH_FLY_CABLE_EXEC_TWO'
			],
			key_tips=[
				'E_D_INCLINE_BENCH_FLY_CABLE_TIP_ONE',
				'E_D_INCLINE_BENCH_FLY_CABLE_TIP_TWO'
			],
			focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER],
			equipment=ExerciseEquipment.CABLE_MACHINE,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-156',
			title= "E_D_INCLINE_BENCH_FLY_DUMBBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/incline_bench_fly_dumbbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/incline_bench_fly_dumbbell.png'],
			preparation_steps=[
				'E_D_INCLINE_BENCH_FLY_DUMBBELL_PREP_ONE',
				'E_D_INCLINE_BENCH_FLY_DUMBBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_INCLINE_BENCH_FLY_DUMBBELL_EXEC_ONE',
				'E_D_INCLINE_BENCH_FLY_DUMBBELL_EXEC_TWO'
			],
			key_tips=[
				'E_D_INCLINE_BENCH_FLY_DUMBBELL_TIP_ONE',
				'E_D_INCLINE_BENCH_FLY_DUMBBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER],
			equipment=ExerciseEquipment.DUMBBELL,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-157',
			title= "E_D_INCLINE_BENCH_PRESS_BARBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/incline_bench_press_barbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/incline_bench_press_barbell.png'],
			preparation_steps=[
				'E_D_INCLINE_BENCH_PRESS_BARBELL_PREP_ONE',
				'E_D_INCLINE_BENCH_PRESS_BARBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_INCLINE_BENCH_PRESS_BARBELL_EXEC_ONE',
				'E_D_INCLINE_BENCH_PRESS_BARBELL_EXEC_TWO'
			],
			key_tips=[
				'E_D_INCLINE_BENCH_PRESS_BARBELL_TIP_ONE',
				'E_D_INCLINE_BENCH_PRESS_BARBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
			equipment=ExerciseEquipment.BARBELL,
			metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
		),
		ExerciseDefinition(
			id='exercise-158',
			title= "E_D_INCLINE_BENCH_PRESS_CABLE_TITLE",
			video_urls=['regular_directory/exercises/videos/incline_bench_press_cable.mp4'],
			cover_image_url=['regular_directory/exercises/images/incline_bench_press_cable.png'],
			preparation_steps=[
				'E_D_INCLINE_BENCH_PRESS_CABLE_PREP_ONE',
				'E_D_INCLINE_BENCH_PRESS_CABLE_PREP_TWO'
			],
			execution_steps=[
				'E_D_INCLINE_BENCH_PRESS_CABLE_EXEC_ONE',
				'E_D_INCLINE_BENCH_PRESS_CABLE_EXEC_TWO'
			],
			key_tips=[
				'E_D_INCLINE_BENCH_PRESS_CABLE_TIP_ONE',
				'E_D_INCLINE_BENCH_PRESS_CABLE_TIP_TWO'
			],
			focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
			equipment=ExerciseEquipment.CABLE_MACHINE,
			metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
		),
		ExerciseDefinition(
			id='exercise-159',
			title= "E_D_INCLINE_BENCH_PRESS_CLOSE_GRIP_BARBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/incline_bench_press_close_grip_barbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/incline_bench_press_close_grip_barbell.png'],
			preparation_steps=[
				'E_D_INCLINE_BENCH_PRESS_CLOSE_GRIP_BARBELL_PREP_ONE',
				'E_D_INCLINE_BENCH_PRESS_CLOSE_GRIP_BARBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_INCLINE_BENCH_PRESS_CLOSE_GRIP_BARBELL_EXEC_ONE',
				'E_D_INCLINE_BENCH_PRESS_CLOSE_GRIP_BARBELL_EXEC_TWO'
			],
			key_tips=[
				'E_D_INCLINE_BENCH_PRESS_CLOSE_GRIP_BARBELL_TIP_ONE',
				'E_D_INCLINE_BENCH_PRESS_CLOSE_GRIP_BARBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
			equipment=ExerciseEquipment.BARBELL,
			metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
		),
		ExerciseDefinition(
			id='exercise-160',
			title= "E_D_INCLINE_BENCH_PRESS_DUMBBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/incline_bench_press_dumbbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/incline_bench_press_dumbbell.png'],
			preparation_steps=[
				'E_D_INCLINE_BENCH_PRESS_DUMBBELL_PREP_ONE',
				'E_D_INCLINE_BENCH_PRESS_DUMBBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_INCLINE_BENCH_PRESS_DUMBBELL_EXEC_ONE',
				'E_D_INCLINE_BENCH_PRESS_DUMBBELL_EXEC_TWO'
			],
			key_tips=[
				'E_D_INCLINE_BENCH_PRESS_DUMBBELL_TIP_ONE',
				'E_D_INCLINE_BENCH_PRESS_DUMBBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
			equipment=ExerciseEquipment.DUMBBELL,
			metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
		),
		ExerciseDefinition(
			id='exercise-162',
			title= "E_D_INCLINE_BICEP_CURL_DUMBBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/incline_bicep_curl_dumbbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/incline_bicep_curl_dumbbell.png'],
			preparation_steps=[
				'E_D_INCLINE_BICEP_CURL_DUMBBELL_PREP_ONE',
				'E_D_INCLINE_BICEP_CURL_DUMBBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_INCLINE_BICEP_CURL_DUMBBELL_EXEC_ONE',
				'E_D_INCLINE_BICEP_CURL_DUMBBELL_EXEC_TWO'
			],
			key_tips=[
				'E_D_INCLINE_BICEP_CURL_DUMBBELL_TIP_ONE',
				'E_D_INCLINE_BICEP_CURL_DUMBBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.ARM],
			equipment=ExerciseEquipment.DUMBBELL,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		
		ExerciseDefinition(
			id='exercise-164',
			title= "E_D_INCLINE_PUSH_UP_TITLE",
			video_urls=['regular_directory/exercises/videos/incline_push_up.mp4'],
			cover_image_url=['regular_directory/exercises/images/incline_push_up.png'],
			preparation_steps=[
				'E_D_INCLINE_PUSH_UP_PREP_ONE',
				'E_D_INCLINE_PUSH_UP_PREP_TWO'
			],
			execution_steps=[
				'E_D_INCLINE_PUSH_UP_EXEC_ONE',
				'E_D_INCLINE_PUSH_UP_EXEC_TWO'
			],
			key_tips=[
				'E_D_INCLINE_PUSH_UP_TIP_ONE',
				'E_D_INCLINE_PUSH_UP_TIP_TWO'
			],
			focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
			equipment=ExerciseEquipment.BODY_WEIGHT,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-165',
			title= "E_D_INCLINE_REVERSE_FLY_DUMBBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/incline_reverse_fly_dumbbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/incline_reverse_fly_dumbbell.png'],
			preparation_steps=[
				'E_D_INCLINE_REVERSE_FLY_DUMBBELL_PREP_ONE',
				'E_D_INCLINE_REVERSE_FLY_DUMBBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_INCLINE_REVERSE_FLY_DUMBBELL_EXEC_ONE',
				'E_D_INCLINE_REVERSE_FLY_DUMBBELL_EXEC_TWO'
			],
			key_tips=[
				'E_D_INCLINE_REVERSE_FLY_DUMBBELL_TIP_ONE',
				'E_D_INCLINE_REVERSE_FLY_DUMBBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.BACK, FocusArea.SHOULDER],
			equipment=ExerciseEquipment.DUMBBELL,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-166',
			title= "E_D_INCLINE_ROW_BARBELL_TITLE",
			video_urls=['regular_directory/exercises/videos/incline_row_barbell.mp4'],
			cover_image_url=['regular_directory/exercises/images/incline_row_barbell.png'],
			preparation_steps=[
				'E_D_INCLINE_ROW_BARBELL_PREP_ONE',
				'E_D_INCLINE_ROW_BARBELL_PREP_TWO'
			],
			execution_steps=[
				'E_D_INCLINE_ROW_BARBELL_EXEC_ONE',
				'E_D_INCLINE_ROW_BARBELL_EXEC_TWO'
			],
			key_tips=[
				'E_D_INCLINE_ROW_BARBELL_TIP_ONE',
				'E_D_INCLINE_ROW_BARBELL_TIP_TWO'
			],
			focus_areas=[FocusArea.BACK, FocusArea.ARM],
			equipment=ExerciseEquipment.BARBELL,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-167',
			title= "E_D_INCLINE_ROW_CABLE_TITLE",
			video_urls=['regular_directory/exercises/videos/incline_row_cable.mp4'],
			cover_image_url=['regular_directory/exercises/images/incline_row_cable.png'],
			preparation_steps=[
				'E_D_INCLINE_ROW_CABLE_PREP_ONE',
				'E_D_INCLINE_ROW_CABLE_PREP_TWO'
			],
			execution_steps=[
				'E_D_INCLINE_ROW_CABLE_EXEC_ONE',
				'E_D_INCLINE_ROW_CABLE_EXEC_TWO'
			],
			key_tips=[
				'E_D_INCLINE_ROW_CABLE_TIP_ONE',
				'E_D_INCLINE_ROW_CABLE_TIP_TWO'
			],
			focus_areas=[FocusArea.BACK, FocusArea.ARM],
			equipment=ExerciseEquipment.CABLE_MACHINE,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
		ExerciseDefinition(
			id='exercise-168',
			title= "E_D_INTERNAL_ROTATION_BAND_TITLE",
			video_urls=['regular_directory/exercises/videos/internal_rotation_band.mp4'],
			cover_image_url=['regular_directory/exercises/images/internal_rotation_band.png'],
			preparation_steps=[
				'E_D_INTERNAL_ROTATION_BAND_PREP_ONE'
			],
			execution_steps=[
				'E_D_INTERNAL_ROTATION_BAND_EXEC_ONE',
				'E_D_INTERNAL_ROTATION_BAND_EXEC_TWO',
				'E_D_INTERNAL_ROTATION_BAND_EXEC_THREE'
			],
			key_tips=[
				'E_D_INTERNAL_ROTATION_BAND_TIP_ONE',
				'E_D_INTERNAL_ROTATION_BAND_TIP_TWO'
			],
			focus_areas=[FocusArea.BACK, FocusArea.SHOULDER],
			equipment=ExerciseEquipment.BAND,
			metric_type=ExerciseMetricType.REPS_ONLY
		),
  # 1. Internal Rotation: Band
        ExerciseDefinition(
            id='exercise-169',
            title="E_D_INTERNAL_ROTATION_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/internal_rotation_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/Internal Rotation Band.png'],
            preparation_steps=[
                'E_D_INTERNAL_ROTATION_BAND_PREP_ONE',
                'E_D_INTERNAL_ROTATION_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_INTERNAL_ROTATION_BAND_EXEC_ONE',
                'E_D_INTERNAL_ROTATION_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_INTERNAL_ROTATION_BAND_TIP_ONE'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 2. Internal Rotation: Cable
        ExerciseDefinition(
            id='exercise-170',
            title="E_D_INTERNAL_ROTATION_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/internal_rotation_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/Internal Rotation Cable.png'],
            preparation_steps=[
                'E_D_INTERNAL_ROTATION_CABLE_PREP_ONE',
                'E_D_INTERNAL_ROTATION_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_INTERNAL_ROTATION_CABLE_EXEC_ONE',
                'E_D_INTERNAL_ROTATION_CABLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_INTERNAL_ROTATION_CABLE_TIP_ONE'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 3. Inverted Row
        ExerciseDefinition(
            id='exercise-171',
            title="E_D_INVERTED_ROW_TITLE",
            video_urls=['regular_directory/exercises/videos/inverted_row.mp4'],
            cover_image_url=['regular_directory/exercises/images/Inverted Row.png'],
            preparation_steps=[
                'E_D_INVERTED_ROW_PREP_ONE',
                'E_D_INVERTED_ROW_PREP_TWO'
            ],
            execution_steps=[
                'E_D_INVERTED_ROW_EXEC_ONE',
                'E_D_INVERTED_ROW_EXEC_TWO'
            ],
            key_tips=[
                'E_D_INVERTED_ROW_TIP_ONE'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 4. Inverted Row Reverse Grip
        ExerciseDefinition(
            id='exercise-172',
            title="E_D_INVERTED_ROW_REVERSE_GRIP_TITLE",
            video_urls=['regular_directory/exercises/videos/inverted_row_reverse_grip.mp4'],
            cover_image_url=['regular_directory/exercises/images/Inverted Row Reverse Grip.png'],
            preparation_steps=[
                'E_D_INVERTED_ROW_REVERSE_GRIP_PREP_ONE',
                'E_D_INVERTED_ROW_REVERSE_GRIP_PREP_TWO'
            ],
            execution_steps=[
                'E_D_INVERTED_ROW_REVERSE_GRIP_EXEC_ONE',
                'E_D_INVERTED_ROW_REVERSE_GRIP_EXEC_TWO'
            ],
            key_tips=[
                'E_D_INVERTED_ROW_REVERSE_GRIP_TIP_ONE'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 5. Jump Squat
        ExerciseDefinition(
            id='exercise-173',
            title="E_D_JUMP_SQUAT_TITLE",
            video_urls=['regular_directory/exercises/videos/jump_squat.mp4'],
            cover_image_url=['regular_directory/exercises/images/Jump Squat.png'],
            preparation_steps=[
                'E_D_JUMP_SQUAT_PREP_ONE',
                'E_D_JUMP_SQUAT_PREP_TWO',
                'E_D_JUMP_SQUAT_PREP_THREE'
            ],
            execution_steps=[
                'E_D_JUMP_SQUAT_EXEC_ONE',
                'E_D_JUMP_SQUAT_EXEC_TWO'
            ],
            key_tips=[
                'E_D_JUMP_SQUAT_TIP_ONE',
                'E_D_JUMP_SQUAT_TIP_TWO',
                'E_D_JUMP_SQUAT_TIP_THREE'
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 6. Jump Squat: Barbell
        ExerciseDefinition(
            id='exercise-174',
            title="E_D_JUMP_SQUAT_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/jump_squat_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/Jump Squat Barbell.png'],
            preparation_steps=[
                'E_D_JUMP_SQUAT_BARBELL_PREP_ONE',
                'E_D_JUMP_SQUAT_BARBELL_PREP_TWO',
                'E_D_JUMP_SQUAT_BARBELL_PREP_THREE'
            ],
            execution_steps=[
                'E_D_JUMP_SQUAT_BARBELL_EXEC_ONE',
                'E_D_JUMP_SQUAT_BARBELL_EXEC_TWO',
                'E_D_JUMP_SQUAT_BARBELL_EXEC_THREE'
            ],
            key_tips=[
                'E_D_JUMP_SQUAT_BARBELL_TIP_ONE',
                'E_D_JUMP_SQUAT_BARBELL_TIP_TWO',
                'E_D_JUMP_SQUAT_BARBELL_TIP_THREE'
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        # 7. Jump Squat- Dumbbell
        ExerciseDefinition(
            id='exercise-175',
            title="E_D_JUMP_SQUAT_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/jump_squat_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/Jump Squat- Dumbbell.png'],
            preparation_steps=[
                'E_D_JUMP_SQUAT_DUMBBELL_PREP_ONE',
                'E_D_JUMP_SQUAT_DUMBBELL_PREP_TWO',
                'E_D_JUMP_SQUAT_DUMBBELL_PREP_THREE'
            ],
            execution_steps=[
                'E_D_JUMP_SQUAT_DUMBBELL_EXEC_ONE',
                'E_D_JUMP_SQUAT_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_JUMP_SQUAT_DUMBBELL_TIP_ONE',
                'E_D_JUMP_SQUAT_DUMBBELL_TIP_TWO',
                'E_D_JUMP_SQUAT_DUMBBELL_TIP_THREE'
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        # 8. Jumping Jack
        ExerciseDefinition(
            id='exercise-176',
            title="E_D_JUMPING_JACK_TITLE",
            video_urls=['regular_directory/exercises/videos/jumping_jack.mp4'],
            cover_image_url=['regular_directory/exercises/images/Jumping Jack.png'],
            preparation_steps=[
                'E_D_JUMPING_JACK_PREP_ONE'
            ],
            execution_steps=[
                'E_D_JUMPING_JACK_EXEC_ONE',
                'E_D_JUMPING_JACK_EXEC_TWO'
            ],
            key_tips=[
                'E_D_JUMPING_JACK_TIP_ONE',
                'E_D_JUMPING_JACK_TIP_TWO',
                'E_D_JUMPING_JACK_TIP_THREE'
            ],
            focus_areas=[FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.TIME_BASED
        ),
        # 9. Kettlebell Swing
        ExerciseDefinition(
            id='exercise-177',
            title="E_D_KETTLEBELL_SWING_TITLE",
            video_urls=['regular_directory/exercises/videos/kettlebell_swing.mp4'],
            cover_image_url=['regular_directory/exercises/images/Kettlebell Swing.png'],
            preparation_steps=[
                'E_D_KETTLEBELL_SWING_PREP_ONE',
                'E_D_KETTLEBELL_SWING_PREP_TWO'
            ],
            execution_steps=[
                'E_D_KETTLEBELL_SWING_EXEC_ONE',
                'E_D_KETTLEBELL_SWING_EXEC_TWO'
            ],
            key_tips=[
                'E_D_KETTLEBELL_SWING_TIP_ONE',
                'E_D_KETTLEBELL_SWING_TIP_TWO',
                'E_D_KETTLEBELL_SWING_TIP_THREE'
            ],
            focus_areas=[FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.KETTLEBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 10. Knee Push-up
        ExerciseDefinition(
            id='exercise-178',
            title="E_D_KNEE_PUSH_UP_TITLE",
            video_urls=['regular_directory/exercises/videos/knee_push_up.mp4'],
            cover_image_url=['regular_directory/exercises/images/Knee Push-up.png'],
            preparation_steps=[
                'E_D_KNEE_PUSH_UP_PREP_ONE',
                'E_D_KNEE_PUSH_UP_PREP_TWO'
            ],
            execution_steps=[
                'E_D_KNEE_PUSH_UP_EXEC_ONE',
                'E_D_KNEE_PUSH_UP_EXEC_TWO'
            ],
            key_tips=[
                'E_D_KNEE_PUSH_UP_TIP_ONE',
                'E_D_KNEE_PUSH_UP_TIP_TWO',
                'E_D_KNEE_PUSH_UP_TIP_THREE'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.ARM, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 11. Knee Raise
        ExerciseDefinition(
            id='exercise-179',
            title="E_D_KNEE_RAISE_TITLE",
            video_urls=['regular_directory/exercises/videos/knee_raise.mp4'],
            cover_image_url=['regular_directory/exercises/images/Knee Raise.png'],
            preparation_steps=[
                'E_D_KNEE_RAISE_PREP_ONE',
                'E_D_KNEE_RAISE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_KNEE_RAISE_EXEC_ONE',
                'E_D_KNEE_RAISE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_KNEE_RAISE_TIP_ONE',
                'E_D_KNEE_RAISE_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN, FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 12. Knee Raise Twist
        ExerciseDefinition(
            id='exercise-180',
            title="E_D_KNEE_RAISE_TWIST_TITLE",
            video_urls=['regular_directory/exercises/videos/knee_raise_twist.mp4'],
            cover_image_url=['regular_directory/exercises/images/Knee Raise Twist.png'],
            preparation_steps=[
                'E_D_KNEE_RAISE_TWIST_PREP_ONE',
                'E_D_KNEE_RAISE_TWIST_PREP_TWO'
            ],
            execution_steps=[
                'E_D_KNEE_RAISE_TWIST_EXEC_ONE',
                'E_D_KNEE_RAISE_TWIST_EXEC_TWO',
                'E_D_KNEE_RAISE_TWIST_EXEC_THREE'
            ],
            key_tips=[
                'E_D_KNEE_RAISE_TWIST_TIP_ONE',
                'E_D_KNEE_RAISE_TWIST_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN, FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 13. Kneeling Crunch: Band
        ExerciseDefinition(
            id='exercise-181',
            title="E_D_KNEELING_CRUNCH_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/kneeling_crunch_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/Kneeling Crunch Band.png'],
            preparation_steps=[
                'E_D_KNEELING_CRUNCH_BAND_PREP_ONE',
                'E_D_KNEELING_CRUNCH_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_KNEELING_CRUNCH_BAND_EXEC_ONE',
                'E_D_KNEELING_CRUNCH_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_KNEELING_CRUNCH_BAND_TIP_ONE',
                'E_D_KNEELING_CRUNCH_BAND_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # 14. Kneeling Crunch: Cable
        ExerciseDefinition(
            id='exercise-182',
            title="E_D_KNEELING_CRUNCH_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/kneeling_crunch_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/Kneeling Crunch Cable.png'],
            preparation_steps=[
                'E_D_KNEELING_CRUNCH_CABLE_PREP_ONE',
                'E_D_KNEELING_CRUNCH_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_KNEELING_CRUNCH_CABLE_EXEC_ONE',
                'E_D_KNEELING_CRUNCH_CABLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_KNEELING_CRUNCH_CABLE_TIP_ONE',
                'E_D_KNEELING_CRUNCH_CABLE_TIP_TWO',
                'E_D_KNEELING_CRUNCH_CABLE_TIP_THREE'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        # 15. Kneeling Plank
        ExerciseDefinition(
            id='exercise-183',
            title="E_D_KNEELING_PLANK_TITLE",
            video_urls=['regular_directory/exercises/videos/kneeling_plank.mp4'],
            cover_image_url=['regular_directory/exercises/images/Kneeling Plank.png'],
            preparation_steps=[
                'E_D_KNEELING_PLANK_PREP_ONE'
            ],
            execution_steps=[
                'E_D_KNEELING_PLANK_EXEC_ONE',
                'E_D_KNEELING_PLANK_EXEC_TWO',
                'E_D_KNEELING_PLANK_EXEC_THREE'
            ],
            key_tips=[
                'E_D_KNEELING_PLANK_TIP_ONE',
                'E_D_KNEELING_PLANK_TIP_TWO',
                'E_D_KNEELING_PLANK_TIP_THREE'
            ],
            focus_areas=[FocusArea.ABDOMEN, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.TIME_BASED
        ),
        # 16. Kneeling Pull-down: Band
        ExerciseDefinition(
            id='exercise-184',
            title="E_D_KNEELING_PULL_DOWN_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/kneeling_pull_down_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/Kneeling Pull-down Band.png'],
            preparation_steps=[
                'E_D_KNEELING_PULL_DOWN_BAND_PREP_ONE',
                'E_D_KNEELING_PULL_DOWN_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_KNEELING_PULL_DOWN_BAND_EXEC_ONE',
                'E_D_KNEELING_PULL_DOWN_BAND_EXEC_TWO' # Inferred step based on pattern
            ],
            key_tips=[
                'E_D_KNEELING_PULL_DOWN_BAND_TIP_ONE',
                'E_D_KNEELING_PULL_DOWN_BAND_TIP_TWO',
                'E_D_KNEELING_PULL_DOWN_BAND_TIP_THREE'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
ExerciseDefinition(
            id='exercise-169',
            title= "E_D_INTERNAL_ROTATION_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/internal_rotation_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/internal_rotation_band.png'],
            preparation_steps=[
                'E_D_INTERNAL_ROTATION_BAND_PREP_ONE',
                'E_D_INTERNAL_ROTATION_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_INTERNAL_ROTATION_BAND_EXEC_ONE',
                'E_D_INTERNAL_ROTATION_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_INTERNAL_ROTATION_BAND_TIP_ONE'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 170: Internal Rotation: Cable
        ExerciseDefinition(
            id='exercise-170',
            title= "E_D_INTERNAL_ROTATION_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/internal_rotation_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/internal_rotation_cable.png'],
            preparation_steps=[
                'E_D_INTERNAL_ROTATION_CABLE_PREP_ONE',
                'E_D_INTERNAL_ROTATION_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_INTERNAL_ROTATION_CABLE_EXEC_ONE',
                'E_D_INTERNAL_ROTATION_CABLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_INTERNAL_ROTATION_CABLE_TIP_ONE'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 171: Inverted Row
        ExerciseDefinition(
            id='exercise-171',
            title= "E_D_INVERTED_ROW_TITLE",
            video_urls=['regular_directory/exercises/videos/inverted_row.mp4'],
            cover_image_url=['regular_directory/exercises/images/inverted_row.png'],
            preparation_steps=[
                'E_D_INVERTED_ROW_PREP_ONE',
                'E_D_INVERTED_ROW_PREP_TWO'
            ],
            execution_steps=[
                'E_D_INVERTED_ROW_EXEC_ONE',
                'E_D_INVERTED_ROW_EXEC_TWO'
            ],
            key_tips=[
                'E_D_INVERTED_ROW_TIP_ONE'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 172: Inverted Row Reverse Grip
        ExerciseDefinition(
            id='exercise-172',
            title= "E_D_INVERTED_ROW_REVERSE_GRIP_TITLE",
            video_urls=['regular_directory/exercises/videos/inverted_row_reverse_grip.mp4'],
            cover_image_url=['regular_directory/exercises/images/inverted_row_reverse_grip.png'],
            preparation_steps=[
                'E_D_INVERTED_ROW_REVERSE_GRIP_PREP_ONE',
                'E_D_INVERTED_ROW_REVERSE_GRIP_PREP_TWO'
            ],
            execution_steps=[
                'E_D_INVERTED_ROW_REVERSE_GRIP_EXEC_ONE',
                'E_D_INVERTED_ROW_REVERSE_GRIP_EXEC_TWO'
            ],
            key_tips=[
                'E_D_INVERTED_ROW_REVERSE_GRIP_TIP_ONE'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 173: Jump Squat
        ExerciseDefinition(
            id='exercise-173',
            title= "E_D_JUMP_SQUAT_TITLE",
            video_urls=['regular_directory/exercises/videos/jump_squat.mp4'],
            cover_image_url=['regular_directory/exercises/images/jump_squat.png'],
            preparation_steps=[
                'E_D_JUMP_SQUAT_PREP_ONE',
                'E_D_JUMP_SQUAT_PREP_TWO',
                'E_D_JUMP_SQUAT_PREP_THREE'
            ],
            execution_steps=[
                'E_D_JUMP_SQUAT_EXEC_ONE',
                'E_D_JUMP_SQUAT_EXEC_TWO'
            ],
            key_tips=[
                'E_D_JUMP_SQUAT_TIP_ONE',
                'E_D_JUMP_SQUAT_TIP_TWO',
                'E_D_JUMP_SQUAT_TIP_THREE'
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 174: Jump Squat: Barbell
        ExerciseDefinition(
            id='exercise-174',
            title= "E_D_JUMP_SQUAT_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/jump_squat_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/jump_squat_barbell.png'],
            preparation_steps=[
                'E_D_JUMP_SQUAT_BARBELL_PREP_ONE',
                'E_D_JUMP_SQUAT_BARBELL_PREP_TWO',
                'E_D_JUMP_SQUAT_BARBELL_PREP_THREE'
            ],
            execution_steps=[
                'E_D_JUMP_SQUAT_BARBELL_EXEC_ONE',
                'E_D_JUMP_SQUAT_BARBELL_EXEC_TWO',
                'E_D_JUMP_SQUAT_BARBELL_EXEC_THREE'
            ],
            key_tips=[
                'E_D_JUMP_SQUAT_BARBELL_TIP_ONE',
                'E_D_JUMP_SQUAT_BARBELL_TIP_TWO',
                'E_D_JUMP_SQUAT_BARBELL_TIP_THREE'
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 175: Jump Squat- Dumbbell
        ExerciseDefinition(
            id='exercise-175',
            title= "E_D_JUMP_SQUAT_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/jump_squat_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/jump_squat_dumbbell.png'],
            preparation_steps=[
                'E_D_JUMP_SQUAT_DUMBBELL_PREP_ONE',
                'E_D_JUMP_SQUAT_DUMBBELL_PREP_TWO',
                'E_D_JUMP_SQUAT_DUMBBELL_PREP_THREE'
            ],
            execution_steps=[
                'E_D_JUMP_SQUAT_DUMBBELL_EXEC_ONE',
                'E_D_JUMP_SQUAT_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_JUMP_SQUAT_DUMBBELL_TIP_ONE',
                'E_D_JUMP_SQUAT_DUMBBELL_TIP_TWO',
                'E_D_JUMP_SQUAT_DUMBBELL_TIP_THREE'
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 176: Jumping Jack
        ExerciseDefinition(
            id='exercise-176',
            title= "E_D_JUMPING_JACK_TITLE",
            video_urls=['regular_directory/exercises/videos/jumping_jack.mp4'],
            cover_image_url=['regular_directory/exercises/images/jumping_jack.png'],
            preparation_steps=[
                'E_D_JUMPING_JACK_PREP_ONE'
            ],
            execution_steps=[
                'E_D_JUMPING_JACK_EXEC_ONE',
                'E_D_JUMPING_JACK_EXEC_TWO'
            ],
            key_tips=[
                'E_D_JUMPING_JACK_TIP_ONE',
                'E_D_JUMPING_JACK_TIP_TWO',
                'E_D_JUMPING_JACK_TIP_THREE'
            ],
            focus_areas=[FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.TIME_BASED # Conditioning/Cardio
        ),
        # Exercise 177: Kettlebell Swing
        ExerciseDefinition(
            id='exercise-177',
            title= "E_D_KETTLEBELL_SWING_TITLE",
            video_urls=['regular_directory/exercises/videos/kettlebell_swing.mp4'],
            cover_image_url=['regular_directory/exercises/images/kettlebell_swing.png'],
            preparation_steps=[
                'E_D_KETTLEBELL_SWING_PREP_ONE',
                'E_D_KETTLEBELL_SWING_PREP_TWO'
            ],
            execution_steps=[
                'E_D_KETTLEBELL_SWING_EXEC_ONE',
                'E_D_KETTLEBELL_SWING_EXEC_TWO'
            ],
            key_tips=[
                'E_D_KETTLEBELL_SWING_TIP_ONE',
                'E_D_KETTLEBELL_SWING_TIP_TWO',
                'E_D_KETTLEBELL_SWING_TIP_THREE'
            ],
            focus_areas=[FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.KETTLEBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 178: Knee Push-up
        ExerciseDefinition(
            id='exercise-178',
            title= "E_D_KNEE_PUSH_UP_TITLE",
            video_urls=['regular_directory/exercises/videos/knee_push_up.mp4'],
            cover_image_url=['regular_directory/exercises/images/knee_push_up.png'],
            preparation_steps=[
                'E_D_KNEE_PUSH_UP_PREP_ONE',
                'E_D_KNEE_PUSH_UP_PREP_TWO'
            ],
            execution_steps=[
                'E_D_KNEE_PUSH_UP_EXEC_ONE',
                'E_D_KNEE_PUSH_UP_EXEC_TWO'
            ],
            key_tips=[
                'E_D_KNEE_PUSH_UP_TIP_ONE',
                'E_D_KNEE_PUSH_UP_TIP_TWO',
                'E_D_KNEE_PUSH_UP_TIP_THREE'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.ARM, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 179: Knee Raise
        ExerciseDefinition(
            id='exercise-179',
            title= "E_D_KNEE_RAISE_TITLE",
            video_urls=['regular_directory/exercises/videos/knee_raise.mp4'],
            cover_image_url=['regular_directory/exercises/images/knee_raise.png'],
            preparation_steps=[
                'E_D_KNEE_RAISE_PREP_ONE',
                'E_D_KNEE_RAISE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_KNEE_RAISE_EXEC_ONE',
                'E_D_KNEE_RAISE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_KNEE_RAISE_TIP_ONE',
                'E_D_KNEE_RAISE_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN, FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 180: Knee Raise Twist
        ExerciseDefinition(
            id='exercise-180',
            title= "E_D_KNEE_RAISE_TWIST_TITLE",
            video_urls=['regular_directory/exercises/videos/knee_raise_twist.mp4'],
            cover_image_url=['regular_directory/exercises/images/knee_raise_twist.png'],
            preparation_steps=[
                'E_D_KNEE_RAISE_TWIST_PREP_ONE',
                'E_D_KNEE_RAISE_TWIST_PREP_TWO'
            ],
            execution_steps=[
                'E_D_KNEE_RAISE_TWIST_EXEC_ONE',
                'E_D_KNEE_RAISE_TWIST_EXEC_TWO',
                'E_D_KNEE_RAISE_TWIST_EXEC_THREE'
            ],
            key_tips=[
                'E_D_KNEE_RAISE_TWIST_TIP_ONE',
                'E_D_KNEE_RAISE_TWIST_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN, FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 181: Kneeling Crunch: Band
        ExerciseDefinition(
            id='exercise-181',
            title= "E_D_KNEELING_CRUNCH_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/kneeling_crunch_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/kneeling_crunch_band.png'],
            preparation_steps=[
                'E_D_KNEELING_CRUNCH_BAND_PREP_ONE',
                'E_D_KNEELING_CRUNCH_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_KNEELING_CRUNCH_BAND_EXEC_ONE',
                'E_D_KNEELING_CRUNCH_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_KNEELING_CRUNCH_BAND_TIP_ONE',
                'E_D_KNEELING_CRUNCH_BAND_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 182: Kneeling Crunch: Cable
        ExerciseDefinition(
            id='exercise-182',
            title= "E_D_KNEELING_CRUNCH_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/kneeling_crunch_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/kneeling_crunch_cable.png'],
            preparation_steps=[
                'E_D_KNEELING_CRUNCH_CABLE_PREP_ONE',
                'E_D_KNEELING_CRUNCH_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_KNEELING_CRUNCH_CABLE_EXEC_ONE',
                'E_D_KNEELING_CRUNCH_CABLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_KNEELING_CRUNCH_CABLE_TIP_ONE',
                'E_D_KNEELING_CRUNCH_CABLE_TIP_TWO',
                'E_D_KNEELING_CRUNCH_CABLE_TIP_THREE'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 183: Kneeling Plank
        ExerciseDefinition(
            id='exercise-183',
            title= "E_D_KNEELING_PLANK_TITLE",
            video_urls=['regular_directory/exercises/videos/kneeling_plank.mp4'],
            cover_image_url=['regular_directory/exercises/images/kneeling_plank.png'],
            preparation_steps=[
                'E_D_KNEELING_PLANK_PREP_ONE'
            ],
            execution_steps=[
                'E_D_KNEELING_PLANK_EXEC_ONE',
                'E_D_KNEELING_PLANK_EXEC_TWO',
                'E_D_KNEELING_PLANK_EXEC_THREE'
            ],
            key_tips=[
                'E_D_KNEELING_PLANK_TIP_ONE',
                'E_D_KNEELING_PLANK_TIP_TWO',
                'E_D_KNEELING_PLANK_TIP_THREE'
            ],
            focus_areas=[FocusArea.ABDOMEN, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.TIME_BASED # Time-based (hold position)
        ),
# Exercise 169: Internal Rotation: Band
        ExerciseDefinition(
            id='exercise-169',
            title= "E_D_INTERNAL_ROTATION_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/internal_rotation_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/internal_rotation_band.png'],
            preparation_steps=[
                'E_D_INTERNAL_ROTATION_BAND_PREP_ONE',
                'E_D_INTERNAL_ROTATION_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_INTERNAL_ROTATION_BAND_EXEC_ONE',
                'E_D_INTERNAL_ROTATION_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_INTERNAL_ROTATION_BAND_TIP_ONE'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 170: Internal Rotation: Cable
        ExerciseDefinition(
            id='exercise-170',
            title= "E_D_INTERNAL_ROTATION_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/internal_rotation_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/internal_rotation_cable.png'],
            preparation_steps=[
                'E_D_INTERNAL_ROTATION_CABLE_PREP_ONE',
                'E_D_INTERNAL_ROTATION_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_INTERNAL_ROTATION_CABLE_EXEC_ONE',
                'E_D_INTERNAL_ROTATION_CABLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_INTERNAL_ROTATION_CABLE_TIP_ONE'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 171: Inverted Row
        ExerciseDefinition(
            id='exercise-171',
            title= "E_D_INVERTED_ROW_TITLE",
            video_urls=['regular_directory/exercises/videos/inverted_row.mp4'],
            cover_image_url=['regular_directory/exercises/images/inverted_row.png'],
            preparation_steps=[
                'E_D_INVERTED_ROW_PREP_ONE',
                'E_D_INVERTED_ROW_PREP_TWO'
            ],
            execution_steps=[
                'E_D_INVERTED_ROW_EXEC_ONE',
                'E_D_INVERTED_ROW_EXEC_TWO'
            ],
            key_tips=[
                'E_D_INVERTED_ROW_TIP_ONE'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 172: Inverted Row Reverse Grip
        ExerciseDefinition(
            id='exercise-172',
            title= "E_D_INVERTED_ROW_REVERSE_GRIP_TITLE",
            video_urls=['regular_directory/exercises/videos/inverted_row_reverse_grip.mp4'],
            cover_image_url=['regular_directory/exercises/images/inverted_row_reverse_grip.png'],
            preparation_steps=[
                'E_D_INVERTED_ROW_REVERSE_GRIP_PREP_ONE',
                'E_D_INVERTED_ROW_REVERSE_GRIP_PREP_TWO'
            ],
            execution_steps=[
                'E_D_INVERTED_ROW_REVERSE_GRIP_EXEC_ONE',
                'E_D_INVERTED_ROW_REVERSE_GRIP_EXEC_TWO'
            ],
            key_tips=[
                'E_D_INVERTED_ROW_REVERSE_GRIP_TIP_ONE'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 173: Jump Squat
        ExerciseDefinition(
            id='exercise-173',
            title= "E_D_JUMP_SQUAT_TITLE",
            video_urls=['regular_directory/exercises/videos/jump_squat.mp4'],
            cover_image_url=['regular_directory/exercises/images/jump_squat.png'],
            preparation_steps=[
                'E_D_JUMP_SQUAT_PREP_ONE',
                'E_D_JUMP_SQUAT_PREP_TWO',
                'E_D_JUMP_SQUAT_PREP_THREE'
            ],
            execution_steps=[
                'E_D_JUMP_SQUAT_EXEC_ONE',
                'E_D_JUMP_SQUAT_EXEC_TWO'
            ],
            key_tips=[
                'E_D_JUMP_SQUAT_TIP_ONE',
                'E_D_JUMP_SQUAT_TIP_TWO',
                'E_D_JUMP_SQUAT_TIP_THREE'
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 174: Jump Squat: Barbell
        ExerciseDefinition(
            id='exercise-174',
            title= "E_D_JUMP_SQUAT_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/jump_squat_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/jump_squat_barbell.png'],
            preparation_steps=[
                'E_D_JUMP_SQUAT_BARBELL_PREP_ONE',
                'E_D_JUMP_SQUAT_BARBELL_PREP_TWO',
                'E_D_JUMP_SQUAT_BARBELL_PREP_THREE'
            ],
            execution_steps=[
                'E_D_JUMP_SQUAT_BARBELL_EXEC_ONE',
                'E_D_JUMP_SQUAT_BARBELL_EXEC_TWO',
                'E_D_JUMP_SQUAT_BARBELL_EXEC_THREE'
            ],
            key_tips=[
                'E_D_JUMP_SQUAT_BARBELL_TIP_ONE',
                'E_D_JUMP_SQUAT_BARBELL_TIP_TWO',
                'E_D_JUMP_SQUAT_BARBELL_TIP_THREE'
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 175: Jump Squat- Dumbbell
        ExerciseDefinition(
            id='exercise-175',
            title= "E_D_JUMP_SQUAT_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/jump_squat_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/jump_squat_dumbbell.png'],
            preparation_steps=[
                'E_D_JUMP_SQUAT_DUMBBELL_PREP_ONE',
                'E_D_JUMP_SQUAT_DUMBBELL_PREP_TWO',
                'E_D_JUMP_SQUAT_DUMBBELL_PREP_THREE'
            ],
            execution_steps=[
                'E_D_JUMP_SQUAT_DUMBBELL_EXEC_ONE',
                'E_D_JUMP_SQUAT_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_JUMP_SQUAT_DUMBBELL_TIP_ONE',
                'E_D_JUMP_SQUAT_DUMBBELL_TIP_TWO',
                'E_D_JUMP_SQUAT_DUMBBELL_TIP_THREE'
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 176: Jumping Jack
        ExerciseDefinition(
            id='exercise-176',
            title= "E_D_JUMPING_JACK_TITLE",
            video_urls=['regular_directory/exercises/videos/jumping_jack.mp4'],
            cover_image_url=['regular_directory/exercises/images/jumping_jack.png'],
            preparation_steps=[
                'E_D_JUMPING_JACK_PREP_ONE'
            ],
            execution_steps=[
                'E_D_JUMPING_JACK_EXEC_ONE',
                'E_D_JUMPING_JACK_EXEC_TWO'
            ],
            key_tips=[
                'E_D_JUMPING_JACK_TIP_ONE',
                'E_D_JUMPING_JACK_TIP_TWO',
                'E_D_JUMPING_JACK_TIP_THREE'
            ],
            focus_areas=[FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.TIME_BASED # Conditioning/Cardio
        ),
        # Exercise 177: Kettlebell Swing
        ExerciseDefinition(
            id='exercise-177',
            title= "E_D_KETTLEBELL_SWING_TITLE",
            video_urls=['regular_directory/exercises/videos/kettlebell_swing.mp4'],
            cover_image_url=['regular_directory/exercises/images/kettlebell_swing.png'],
            preparation_steps=[
                'E_D_KETTLEBELL_SWING_PREP_ONE',
                'E_D_KETTLEBELL_SWING_PREP_TWO'
            ],
            execution_steps=[
                'E_D_KETTLEBELL_SWING_EXEC_ONE',
                'E_D_KETTLEBELL_SWING_EXEC_TWO'
            ],
            key_tips=[
                'E_D_KETTLEBELL_SWING_TIP_ONE',
                'E_D_KETTLEBELL_SWING_TIP_TWO',
                'E_D_KETTLEBELL_SWING_TIP_THREE'
            ],
            focus_areas=[FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.KETTLEBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 178: Knee Push-up
        ExerciseDefinition(
            id='exercise-178',
            title= "E_D_KNEE_PUSH_UP_TITLE",
            video_urls=['regular_directory/exercises/videos/knee_push_up.mp4'],
            cover_image_url=['regular_directory/exercises/images/knee_push_up.png'],
            preparation_steps=[
                'E_D_KNEE_PUSH_UP_PREP_ONE',
                'E_D_KNEE_PUSH_UP_PREP_TWO'
            ],
            execution_steps=[
                'E_D_KNEE_PUSH_UP_EXEC_ONE',
                'E_D_KNEE_PUSH_UP_EXEC_TWO'
            ],
            key_tips=[
                'E_D_KNEE_PUSH_UP_TIP_ONE',
                'E_D_KNEE_PUSH_UP_TIP_TWO',
                'E_D_KNEE_PUSH_UP_TIP_THREE'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.ARM, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 179: Knee Raise
        ExerciseDefinition(
            id='exercise-179',
            title= "E_D_KNEE_RAISE_TITLE",
            video_urls=['regular_directory/exercises/videos/knee_raise.mp4'],
            cover_image_url=['regular_directory/exercises/images/knee_raise.png'],
            preparation_steps=[
                'E_D_KNEE_RAISE_PREP_ONE',
                'E_D_KNEE_RAISE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_KNEE_RAISE_EXEC_ONE',
                'E_D_KNEE_RAISE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_KNEE_RAISE_TIP_ONE',
                'E_D_KNEE_RAISE_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN, FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 180: Knee Raise Twist
        ExerciseDefinition(
            id='exercise-180',
            title= "E_D_KNEE_RAISE_TWIST_TITLE",
            video_urls=['regular_directory/exercises/videos/knee_raise_twist.mp4'],
            cover_image_url=['regular_directory/exercises/images/knee_raise_twist.png'],
            preparation_steps=[
                'E_D_KNEE_RAISE_TWIST_PREP_ONE',
                'E_D_KNEE_RAISE_TWIST_PREP_TWO'
            ],
            execution_steps=[
                'E_D_KNEE_RAISE_TWIST_EXEC_ONE',
                'E_D_KNEE_RAISE_TWIST_EXEC_TWO',
                'E_D_KNEE_RAISE_TWIST_EXEC_THREE'
            ],
            key_tips=[
                'E_D_KNEE_RAISE_TWIST_TIP_ONE',
                'E_D_KNEE_RAISE_TWIST_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN, FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 181: Kneeling Crunch: Band
        ExerciseDefinition(
            id='exercise-181',
            title= "E_D_KNEELING_CRUNCH_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/kneeling_crunch_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/kneeling_crunch_band.png'],
            preparation_steps=[
                'E_D_KNEELING_CRUNCH_BAND_PREP_ONE',
                'E_D_KNEELING_CRUNCH_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_KNEELING_CRUNCH_BAND_EXEC_ONE',
                'E_D_KNEELING_CRUNCH_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_KNEELING_CRUNCH_BAND_TIP_ONE',
                'E_D_KNEELING_CRUNCH_BAND_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 182: Kneeling Crunch: Cable
        ExerciseDefinition(
            id='exercise-182',
            title= "E_D_KNEELING_CRUNCH_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/kneeling_crunch_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/kneeling_crunch_cable.png'],
            preparation_steps=[
                'E_D_KNEELING_CRUNCH_CABLE_PREP_ONE',
                'E_D_KNEELING_CRUNCH_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_KNEELING_CRUNCH_CABLE_EXEC_ONE',
                'E_D_KNEELING_CRUNCH_CABLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_KNEELING_CRUNCH_CABLE_TIP_ONE',
                'E_D_KNEELING_CRUNCH_CABLE_TIP_TWO',
                'E_D_KNEELING_CRUNCH_CABLE_TIP_THREE'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 183: Kneeling Plank
        ExerciseDefinition(
            id='exercise-183',
            title= "E_D_KNEELING_PLANK_TITLE",
            video_urls=['regular_directory/exercises/videos/kneeling_plank.mp4'],
            cover_image_url=['regular_directory/exercises/images/kneeling_plank.png'],
            preparation_steps=[
                'E_D_KNEELING_PLANK_PREP_ONE'
            ],
            execution_steps=[
                'E_D_KNEELING_PLANK_EXEC_ONE',
                'E_D_KNEELING_PLANK_EXEC_TWO',
                'E_D_KNEELING_PLANK_EXEC_THREE'
            ],
            key_tips=[
                'E_D_KNEELING_PLANK_TIP_ONE',
                'E_D_KNEELING_PLANK_TIP_TWO',
                'E_D_KNEELING_PLANK_TIP_THREE'
            ],
            focus_areas=[FocusArea.ABDOMEN, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.TIME_BASED # Time-based (hold position)
        ),
        # --- Remaining 138 Exercises (184 to 321) ---
        
        # Exercise 184: Kneeling Pull-down: Band
        ExerciseDefinition(
            id='exercise-184',
            title= "E_D_KNEELING_PULL_DOWN_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/kneeling_pull_down_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/kneeling_pull_down_band.png'],
            preparation_steps=[
                'E_D_KNEELING_PULL_DOWN_BAND_PREP_ONE',
                'E_D_KNEELING_PULL_DOWN_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_KNEELING_PULL_DOWN_BAND_EXEC_ONE',
                'E_D_KNEELING_PULL_DOWN_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_KNEELING_PULL_DOWN_BAND_TIP_ONE'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 185: Kneeling Torso Rotation: Machine
        ExerciseDefinition(
            id='exercise-185',
            title= "E_D_KNEELING_TORSO_ROTATION_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/kneeling_torso_rotation_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/kneeling_torso_rotation_machine.png'],
            preparation_steps=[
                'E_D_KNEELING_TORSO_ROTATION_MACHINE_PREP_ONE',
                'E_D_KNEELING_TORSO_ROTATION_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_KNEELING_TORSO_ROTATION_MACHINE_EXEC_ONE',
                'E_D_KNEELING_TORSO_ROTATION_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_KNEELING_TORSO_ROTATION_MACHINE_TIP_ONE',
                'E_D_KNEELING_TORSO_ROTATION_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 186: Kneeling Triceps Extension
        ExerciseDefinition(
            id='exercise-186',
            title= "E_D_KNEELING_TRICEPS_EXTENSION_TITLE",
            video_urls=['regular_directory/exercises/videos/kneeling_triceps_extension.mp4'],
            cover_image_url=['regular_directory/exercises/images/kneeling_triceps_extension.png'],
            preparation_steps=[
                'E_D_KNEELING_TRICEPS_EXTENSION_PREP_ONE',
                'E_D_KNEELING_TRICEPS_EXTENSION_PREP_TWO'
            ],
            execution_steps=[
                'E_D_KNEELING_TRICEPS_EXTENSION_EXEC_ONE',
                'E_D_KNEELING_TRICEPS_EXTENSION_EXEC_TWO'
            ],
            key_tips=[
                'E_D_KNEELING_TRICEPS_EXTENSION_TIP_ONE',
                'E_D_KNEELING_TRICEPS_EXTENSION_TIP_TWO'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 187: Lat Pulldown (Close Grip): Band
        ExerciseDefinition(
            id='exercise-187',
            title= "E_D_LAT_PULLDOWN_CLOSE_GRIP_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/lat_pulldown_close_grip_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/lat_pulldown_close_grip_band.png'],
            preparation_steps=[
                'E_D_LAT_PULLDOWN_CLOSE_GRIP_BAND_PREP_ONE',
                'E_D_LAT_PULLDOWN_CLOSE_GRIP_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LAT_PULLDOWN_CLOSE_GRIP_BAND_EXEC_ONE',
                'E_D_LAT_PULLDOWN_CLOSE_GRIP_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LAT_PULLDOWN_CLOSE_GRIP_BAND_TIP_ONE',
                'E_D_LAT_PULLDOWN_CLOSE_GRIP_BAND_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 188: Lat Pulldown (Close Grip): Cable
        ExerciseDefinition(
            id='exercise-188',
            title= "E_D_LAT_PULLDOWN_CLOSE_GRIP_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/lat_pulldown_close_grip_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/lat_pulldown_close_grip_cable.png'],
            preparation_steps=[
                'E_D_LAT_PULLDOWN_CLOSE_GRIP_CABLE_PREP_ONE',
                'E_D_LAT_PULLDOWN_CLOSE_GRIP_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LAT_PULLDOWN_CLOSE_GRIP_CABLE_EXEC_ONE',
                'E_D_LAT_PULLDOWN_CLOSE_GRIP_CABLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LAT_PULLDOWN_CLOSE_GRIP_CABLE_TIP_ONE',
                'E_D_LAT_PULLDOWN_CLOSE_GRIP_CABLE_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 189: Lat Pulldown (Reverse Grip): Band
        ExerciseDefinition(
            id='exercise-189',
            title= "E_D_LAT_PULLDOWN_REVERSE_GRIP_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/lat_pulldown_reverse_grip_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/lat_pulldown_reverse_grip_band.png'],
            preparation_steps=[
                'E_D_LAT_PULLDOWN_REVERSE_GRIP_BAND_PREP_ONE',
                'E_D_LAT_PULLDOWN_REVERSE_GRIP_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LAT_PULLDOWN_REVERSE_GRIP_BAND_EXEC_ONE',
                'E_D_LAT_PULLDOWN_REVERSE_GRIP_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LAT_PULLDOWN_REVERSE_GRIP_BAND_TIP_ONE',
                'E_D_LAT_PULLDOWN_REVERSE_GRIP_BAND_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 190: Lat Pulldown (Reverse Grip): Cable
        ExerciseDefinition(
            id='exercise-190',
            title= "E_D_LAT_PULLDOWN_REVERSE_GRIP_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/lat_pulldown_reverse_grip_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/lat_pulldown_reverse_grip_cable.png'],
            preparation_steps=[
                'E_D_LAT_PULLDOWN_REVERSE_GRIP_CABLE_PREP_ONE',
                'E_D_LAT_PULLDOWN_REVERSE_GRIP_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LAT_PULLDOWN_REVERSE_GRIP_CABLE_EXEC_ONE',
                'E_D_LAT_PULLDOWN_REVERSE_GRIP_CABLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LAT_PULLDOWN_REVERSE_GRIP_CABLE_TIP_ONE',
                'E_D_LAT_PULLDOWN_REVERSE_GRIP_CABLE_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 191: Lat Pulldown (Straight Arm): Band
        ExerciseDefinition(
            id='exercise-191',
            title= "E_D_LAT_PULLDOWN_STRAIGHT_ARM_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/lat_pulldown_straight_arm_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/lat_pulldown_straight_arm_band.png'],
            preparation_steps=[
                'E_D_LAT_PULLDOWN_STRAIGHT_ARM_BAND_PREP_ONE',
                'E_D_LAT_PULLDOWN_STRAIGHT_ARM_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LAT_PULLDOWN_STRAIGHT_ARM_BAND_EXEC_ONE',
                'E_D_LAT_PULLDOWN_STRAIGHT_ARM_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LAT_PULLDOWN_STRAIGHT_ARM_BAND_TIP_ONE',
                'E_D_LAT_PULLDOWN_STRAIGHT_ARM_BAND_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 192: Lat Pulldown (Straight Arm): Cable
        ExerciseDefinition(
            id='exercise-192',
            title= "E_D_LAT_PULLDOWN_STRAIGHT_ARM_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/lat_pulldown_straight_arm_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/lat_pulldown_straight_arm_cable.png'],
            preparation_steps=[
                'E_D_LAT_PULLDOWN_STRAIGHT_ARM_CABLE_PREP_ONE',
                'E_D_LAT_PULLDOWN_STRAIGHT_ARM_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LAT_PULLDOWN_STRAIGHT_ARM_CABLE_EXEC_ONE',
                'E_D_LAT_PULLDOWN_STRAIGHT_ARM_CABLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LAT_PULLDOWN_STRAIGHT_ARM_CABLE_TIP_ONE',
                'E_D_LAT_PULLDOWN_STRAIGHT_ARM_CABLE_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 193: Lat Pulldown (Wide Grip): Cable
        ExerciseDefinition(
            id='exercise-193',
            title= "E_D_LAT_PULLDOWN_WIDE_GRIP_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/lat_pulldown_wide_grip_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/lat_pulldown_wide_grip_cable.png'],
            preparation_steps=[
                'E_D_LAT_PULLDOWN_WIDE_GRIP_CABLE_PREP_ONE',
                'E_D_LAT_PULLDOWN_WIDE_GRIP_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LAT_PULLDOWN_WIDE_GRIP_CABLE_EXEC_ONE',
                'E_D_LAT_PULLDOWN_WIDE_GRIP_CABLE_EXEC_TWO',
                'E_D_LAT_PULLDOWN_WIDE_GRIP_CABLE_EXEC_THREE'
            ],
            key_tips=[
                'E_D_LAT_PULLDOWN_WIDE_GRIP_CABLE_TIP_ONE',
                'E_D_LAT_PULLDOWN_WIDE_GRIP_CABLE_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 194: Lat Pulldown: Cable
        ExerciseDefinition(
            id='exercise-194',
            title= "E_D_LAT_PULLDOWN_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/lat_pulldown_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/lat_pulldown_cable.png'],
            preparation_steps=[
                'E_D_LAT_PULLDOWN_CABLE_PREP_ONE',
                'E_D_LAT_PULLDOWN_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LAT_PULLDOWN_CABLE_EXEC_ONE',
                'E_D_LAT_PULLDOWN_CABLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LAT_PULLDOWN_CABLE_TIP_ONE',
                'E_D_LAT_PULLDOWN_CABLE_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 195: Lat Pulldown: Machine
        ExerciseDefinition(
            id='exercise-195',
            title= "E_D_LAT_PULLDOWN_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/lat_pulldown_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/lat_pulldown_machine.png'],
            preparation_steps=[
                'E_D_LAT_PULLDOWN_MACHINE_PREP_ONE',
                'E_D_LAT_PULLDOWN_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LAT_PULLDOWN_MACHINE_EXEC_ONE',
                'E_D_LAT_PULLDOWN_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LAT_PULLDOWN_MACHINE_TIP_ONE',
                'E_D_LAT_PULLDOWN_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 196: Lat Pulldown With Twist: Band
        ExerciseDefinition(
            id='exercise-196',
            title= "E_D_LAT_PULLDOWN_WITH_TWIST_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/lat_pulldown_with_twist_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/lat_pulldown_with_twist_band.png'],
            preparation_steps=[
                'E_D_LAT_PULLDOWN_WITH_TWIST_BAND_PREP_ONE',
                'E_D_LAT_PULLDOWN_WITH_TWIST_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LAT_PULLDOWN_WITH_TWIST_BAND_EXEC_ONE',
                'E_D_LAT_PULLDOWN_WITH_TWIST_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LAT_PULLDOWN_WITH_TWIST_BAND_TIP_ONE'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 197: Lateral Bench Jump
        ExerciseDefinition(
            id='exercise-197',
            title= "E_D_LATERAL_BENCH_JUMP_TITLE",
            video_urls=['regular_directory/exercises/videos/lateral_bench_jump.mp4'],
            cover_image_url=['regular_directory/exercises/images/lateral_bench_jump.png'],
            preparation_steps=[
                'E_D_LATERAL_BENCH_JUMP_PREP_ONE',
                'E_D_LATERAL_BENCH_JUMP_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LATERAL_BENCH_JUMP_EXEC_ONE',
                'E_D_LATERAL_BENCH_JUMP_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LATERAL_BENCH_JUMP_TIP_ONE',
                'E_D_LATERAL_BENCH_JUMP_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG, FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 198: Lateral Raise - Machine
        ExerciseDefinition(
            id='exercise-198',
            title= "E_D_LATERAL_RAISE_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/lateral_raise_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/lateral_raise_machine.png'],
            preparation_steps=[
                'E_D_LATERAL_RAISE_MACHINE_PREP_ONE',
                'E_D_LATERAL_RAISE_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LATERAL_RAISE_MACHINE_EXEC_ONE',
                'E_D_LATERAL_RAISE_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LATERAL_RAISE_MACHINE_TIP_ONE',
                'E_D_LATERAL_RAISE_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.SHOULDER],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 199: Lateral Raise: Band
        ExerciseDefinition(
            id='exercise-199',
            title= "E_D_LATERAL_RAISE_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/lateral_raise_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/lateral_raise_band.png'],
            preparation_steps=[
                'E_D_LATERAL_RAISE_BAND_PREP_ONE',
                'E_D_LATERAL_RAISE_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LATERAL_RAISE_BAND_EXEC_ONE',
                'E_D_LATERAL_RAISE_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LATERAL_RAISE_BAND_TIP_ONE',
                'E_D_LATERAL_RAISE_BAND_TIP_TWO'
            ],
            focus_areas=[FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 200: Lateral Raise: Cable
        ExerciseDefinition(
            id='exercise-200',
            title= "E_D_LATERAL_RAISE_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/lateral_raise_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/lateral_raise_cable.png'],
            preparation_steps=[
                'E_D_LATERAL_RAISE_CABLE_PREP_ONE',
                'E_D_LATERAL_RAISE_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LATERAL_RAISE_CABLE_EXEC_ONE',
                'E_D_LATERAL_RAISE_CABLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LATERAL_RAISE_CABLE_TIP_ONE',
                'E_D_LATERAL_RAISE_CABLE_TIP_TWO'
            ],
            focus_areas=[FocusArea.SHOULDER],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 201: Lateral Raise: Dumbbell
        ExerciseDefinition(
            id='exercise-201',
            title= "E_D_LATERAL_RAISE_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/lateral_raise_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/lateral_raise_dumbbell.png'],
            preparation_steps=[
                'E_D_LATERAL_RAISE_DUMBBELL_PREP_ONE',
                'E_D_LATERAL_RAISE_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LATERAL_RAISE_DUMBBELL_EXEC_ONE',
                'E_D_LATERAL_RAISE_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LATERAL_RAISE_DUMBBELL_TIP_ONE',
                'E_D_LATERAL_RAISE_DUMBBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.SHOULDER],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 202: Lateral Raise: Kettlebell
        ExerciseDefinition(
            id='exercise-202',
            title= "E_D_LATERAL_RAISE_KETTLEBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/lateral_raise_kettlebell.mp4'],
            cover_image_url=['regular_directory/exercises/images/lateral_raise_kettlebell.png'],
            preparation_steps=[
                'E_D_LATERAL_RAISE_KETTLEBELL_PREP_ONE',
                'E_D_LATERAL_RAISE_KETTLEBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LATERAL_RAISE_KETTLEBELL_EXEC_ONE',
                'E_D_LATERAL_RAISE_KETTLEBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LATERAL_RAISE_KETTLEBELL_TIP_ONE',
                'E_D_LATERAL_RAISE_KETTLEBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.SHOULDER],
            equipment=ExerciseEquipment.KETTLEBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 203: Lateral Raise
        ExerciseDefinition(
            id='exercise-203',
            title= "E_D_LATERAL_RAISE_TITLE",
            video_urls=['regular_directory/exercises/videos/lateral_raise.mp4'],
            cover_image_url=['regular_directory/exercises/images/lateral_raise.png'],
            preparation_steps=[
                'E_D_LATERAL_RAISE_PREP_ONE',
                'E_D_LATERAL_RAISE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LATERAL_RAISE_EXEC_ONE',
                'E_D_LATERAL_RAISE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LATERAL_RAISE_TIP_ONE',
                'E_D_LATERAL_RAISE_TIP_TWO'
            ],
            focus_areas=[FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 204: Lateral Step-up: Smith Machine
        ExerciseDefinition(
            id='exercise-204',
            title= "E_D_LATERAL_STEP_UP_SMITH_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/lateral_step_up_smith_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/lateral_step_up_smith_machine.png'],
            preparation_steps=[
                'E_D_LATERAL_STEP_UP_SMITH_MACHINE_PREP_ONE',
                'E_D_LATERAL_STEP_UP_SMITH_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LATERAL_STEP_UP_SMITH_MACHINE_EXEC_ONE',
                'E_D_LATERAL_STEP_UP_SMITH_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LATERAL_STEP_UP_SMITH_MACHINE_TIP_ONE'
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.SMITH_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 205: Leg Bicep Curl
        ExerciseDefinition(
            id='exercise-205',
            title= "E_D_LEG_BICEP_CURL_TITLE",
            video_urls=['regular_directory/exercises/videos/leg_bicep_curl.mp4'],
            cover_image_url=['regular_directory/exercises/images/leg_bicep_curl.png'],
            preparation_steps=[
                'E_D_LEG_BICEP_CURL_PREP_ONE',
                'E_D_LEG_BICEP_CURL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LEG_BICEP_CURL_EXEC_ONE',
                'E_D_LEG_BICEP_CURL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LEG_BICEP_CURL_TIP_ONE',
                'E_D_LEG_BICEP_CURL_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 206: Leg Extension: Band
        ExerciseDefinition(
            id='exercise-206',
            title= "E_D_LEG_EXTENSION_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/leg_extension_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/leg_extension_band.png'],
            preparation_steps=[
                'E_D_LEG_EXTENSION_BAND_PREP_ONE',
                'E_D_LEG_EXTENSION_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LEG_EXTENSION_BAND_EXEC_ONE',
                'E_D_LEG_EXTENSION_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LEG_EXTENSION_BAND_TIP_ONE',
                'E_D_LEG_EXTENSION_BAND_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 207: Leg Extension: Machine
        
        # Exercise 208: Leg Press: Machine
        ExerciseDefinition(
            id='exercise-208',
            title= "E_D_LEG_PRESS_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/leg_press_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/leg_press_machine.png'],
            preparation_steps=[
                'E_D_LEG_PRESS_MACHINE_PREP_ONE',
                'E_D_LEG_PRESS_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LEG_PRESS_MACHINE_EXEC_ONE',
                'E_D_LEG_PRESS_MACHINE_EXEC_TWO',
                'E_D_LEG_PRESS_MACHINE_EXEC_THREE'
            ],
            key_tips=[
                'E_D_LEG_PRESS_MACHINE_TIP_ONE',
                'E_D_LEG_PRESS_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 209: Leg Press: Smith Machine
        
        # Exercise 210: Long Arm Crunch
        ExerciseDefinition(
            id='exercise-210',
            title= "E_D_LONG_ARM_CRUNCH_TITLE",
            video_urls=['regular_directory/exercises/videos/long_arm_crunch.mp4'],
            cover_image_url=['regular_directory/exercises/images/long_arm_crunch.png'],
            preparation_steps=[
                'E_D_LONG_ARM_CRUNCH_PREP_ONE',
                'E_D_LONG_ARM_CRUNCH_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LONG_ARM_CRUNCH_EXEC_ONE',
                'E_D_LONG_ARM_CRUNCH_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LONG_ARM_CRUNCH_TIP_ONE',
                'E_D_LONG_ARM_CRUNCH_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 211: Lunge: Barbell
        ExerciseDefinition(
            id='exercise-211',
            title= "E_D_LUNGE_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/lunge_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/lunge_barbell.png'],
            preparation_steps=[
                'E_D_LUNGE_BARBELL_PREP_ONE',
                'E_D_LUNGE_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LUNGE_BARBELL_EXEC_ONE',
                'E_D_LUNGE_BARBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LUNGE_BARBELL_TIP_ONE',
                'E_D_LUNGE_BARBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 212: Lunge: Cable
        ExerciseDefinition(
            id='exercise-212',
            title= "E_D_LUNGE_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/lunge_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/lunge_cable.png'],
            preparation_steps=[
                'E_D_LUNGE_CABLE_PREP_ONE',
                'E_D_LUNGE_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LUNGE_CABLE_EXEC_ONE',
                'E_D_LUNGE_CABLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LUNGE_CABLE_TIP_ONE',
                'E_D_LUNGE_CABLE_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 213: Lunge: Dumbbell
        ExerciseDefinition(
            id='exercise-213',
            title= "E_D_LUNGE_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/lunge_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/lunge_dumbbell.png'],
            preparation_steps=[
                'E_D_LUNGE_DUMBBELL_PREP_ONE',
                'E_D_LUNGE_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LUNGE_DUMBBELL_EXEC_ONE',
                'E_D_LUNGE_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LUNGE_DUMBBELL_TIP_ONE',
                'E_D_LUNGE_DUMBBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 214: Lunge: Kettlebell
        ExerciseDefinition(
            id='exercise-214',
            title= "E_D_LUNGE_KETTLEBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/lunge_kettlebell.mp4'],
            cover_image_url=['regular_directory/exercises/images/lunge_kettlebell.png'],
            preparation_steps=[
                'E_D_LUNGE_KETTLEBELL_PREP_ONE',
                'E_D_LUNGE_KETTLEBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LUNGE_KETTLEBELL_EXEC_ONE',
                'E_D_LUNGE_KETTLEBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LUNGE_KETTLEBELL_TIP_ONE',
                'E_D_LUNGE_KETTLEBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.KETTLEBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 215: Lunge
        ExerciseDefinition(
            id='exercise-215',
            title= "E_D_LUNGE_TITLE",
            video_urls=['regular_directory/exercises/videos/lunge.mp4'],
            cover_image_url=['regular_directory/exercises/images/lunge.png'],
            preparation_steps=[
                'E_D_LUNGE_PREP_ONE',
                'E_D_LUNGE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LUNGE_EXEC_ONE',
                'E_D_LUNGE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LUNGE_TIP_ONE',
                'E_D_LUNGE_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 216: Lying Hip Adductor
        ExerciseDefinition(
            id='exercise-216',
            title= "E_D_LYING_HIP_ADDUCTOR_TITLE",
            video_urls=['regular_directory/exercises/videos/lying_hip_adductor.mp4'],
            cover_image_url=['regular_directory/exercises/images/lying_hip_adductor.png'],
            preparation_steps=[
                'E_D_LYING_HIP_ADDUCTOR_PREP_ONE'
            ],
            execution_steps=[
                'E_D_LYING_HIP_ADDUCTOR_EXEC_ONE',
                'E_D_LYING_HIP_ADDUCTOR_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LYING_HIP_ADDUCTOR_TIP_ONE',
                'E_D_LYING_HIP_ADDUCTOR_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 217: Lying Hip Raise: Smith Machine
        
        # Exercise 218: Lying Knee Raise
        ExerciseDefinition(
            id='exercise-218',
            title= "E_D_LYING_KNEE_RAISE_TITLE",
            video_urls=['regular_directory/exercises/videos/lying_knee_raise.mp4'],
            cover_image_url=['regular_directory/exercises/images/lying_knee_raise.png'],
            preparation_steps=[
                'E_D_LYING_KNEE_RAISE_PREP_ONE'
            ],
            execution_steps=[
                'E_D_LYING_KNEE_RAISE_EXEC_ONE',
                'E_D_LYING_KNEE_RAISE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LYING_KNEE_RAISE_TIP_ONE',
                'E_D_LYING_KNEE_RAISE_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 219: Lying Leg Curl: Band
        ExerciseDefinition(
            id='exercise-219',
            title= "E_D_LYING_LEG_CURL_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/lying_leg_curl_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/lying_leg_curl_band.png'],
            preparation_steps=[
                'E_D_LYING_LEG_CURL_BAND_PREP_ONE',
                'E_D_LYING_LEG_CURL_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LYING_LEG_CURL_BAND_EXEC_ONE',
                'E_D_LYING_LEG_CURL_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LYING_LEG_CURL_BAND_TIP_ONE',
                'E_D_LYING_LEG_CURL_BAND_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 220: Lying Leg Curl- Dumbbell
        ExerciseDefinition(
            id='exercise-220',
            title= "E_D_LYING_LEG_CURL_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/lying_leg_curl_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/lying_leg_curl_dumbbell.png'],
            preparation_steps=[
                'E_D_LYING_LEG_CURL_DUMBBELL_PREP_ONE',
                'E_D_LYING_LEG_CURL_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LYING_LEG_CURL_DUMBBELL_EXEC_ONE',
                'E_D_LYING_LEG_CURL_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LYING_LEG_CURL_DUMBBELL_TIP_ONE',
                'E_D_LYING_LEG_CURL_DUMBBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 221: Lying Leg Curl- Machine
        ExerciseDefinition(
            id='exercise-221',
            title= "E_D_LYING_LEG_CURL_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/lying_leg_curl_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/lying_leg_curl_machine.png'],
            preparation_steps=[
                'E_D_LYING_LEG_CURL_MACHINE_PREP_ONE',
                'E_D_LYING_LEG_CURL_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LYING_LEG_CURL_MACHINE_EXEC_ONE',
                'E_D_LYING_LEG_CURL_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LYING_LEG_CURL_MACHINE_TIP_ONE',
                'E_D_LYING_LEG_CURL_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 222: Lying Leg Raise
        ExerciseDefinition(
            id='exercise-222',
            title= "E_D_LYING_LEG_RAISE_TITLE",
            video_urls=['regular_directory/exercises/videos/lying_leg_raise.mp4'],
            cover_image_url=['regular_directory/exercises/images/lying_leg_raise.png'],
            preparation_steps=[
                'E_D_LYING_LEG_RAISE_PREP_ONE',
                'E_D_LYING_LEG_RAISE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LYING_LEG_RAISE_EXEC_ONE',
                'E_D_LYING_LEG_RAISE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LYING_LEG_RAISE_TIP_ONE',
                'E_D_LYING_LEG_RAISE_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 223: Lying Reverse Fly
        ExerciseDefinition(
            id='exercise-223',
            title= "E_D_LYING_REVERSE_FLY_TITLE",
            video_urls=['regular_directory/exercises/videos/lying_reverse_fly.mp4'],
            cover_image_url=['regular_directory/exercises/images/lying_reverse_fly.png'],
            preparation_steps=[
                'E_D_LYING_REVERSE_FLY_PREP_ONE',
                'E_D_LYING_REVERSE_FLY_PREP_TWO'
            ],
            execution_steps=[
                'E_D_LYING_REVERSE_FLY_EXEC_ONE',
                'E_D_LYING_REVERSE_FLY_EXEC_TWO'
            ],
            key_tips=[
                'E_D_LYING_REVERSE_FLY_TIP_ONE',
                'E_D_LYING_REVERSE_FLY_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 224: Mountain Climber
        ExerciseDefinition(
            id='exercise-224',
            title= "E_D_MOUNTAIN_CLIMBER_TITLE",
            video_urls=['regular_directory/exercises/videos/mountain_climber.mp4'],
            cover_image_url=['regular_directory/exercises/images/mountain_climber.png'],
            preparation_steps=[
                'E_D_MOUNTAIN_CLIMBER_PREP_ONE'
            ],
            execution_steps=[
                'E_D_MOUNTAIN_CLIMBER_EXEC_ONE',
                'E_D_MOUNTAIN_CLIMBER_EXEC_TWO'
            ],
            key_tips=[
                'E_D_MOUNTAIN_CLIMBER_TIP_ONE',
                'E_D_MOUNTAIN_CLIMBER_TIP_TWO'
            ],
            focus_areas=[FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.TIME_BASED # Conditioning/Cardio
        ),
        # Exercise 225: Muscle Up
        ExerciseDefinition(
            id='exercise-225',
            title= "E_D_MUSCLE_UP_TITLE",
            video_urls=['regular_directory/exercises/videos/muscle_up.mp4'],
            cover_image_url=['regular_directory/exercises/images/muscle_up.png'],
            preparation_steps=[
                'E_D_MUSCLE_UP_PREP_ONE',
                'E_D_MUSCLE_UP_PREP_TWO'
            ],
            execution_steps=[
                'E_D_MUSCLE_UP_EXEC_ONE',
                'E_D_MUSCLE_UP_EXEC_TWO',
                'E_D_MUSCLE_UP_EXEC_THREE'
            ],
            key_tips=[
                'E_D_MUSCLE_UP_TIP_ONE',
                'E_D_MUSCLE_UP_TIP_TWO'
            ],
            focus_areas=[FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 226: Oblique Crunch
        ExerciseDefinition(
            id='exercise-226',
            title= "E_D_OBLIQUE_CRUNCH_TITLE",
            video_urls=['regular_directory/exercises/videos/oblique_crunch.mp4'],
            cover_image_url=['regular_directory/exercises/images/oblique_crunch.png'],
            preparation_steps=[
                'E_D_OBLIQUE_CRUNCH_PREP_ONE',
                'E_D_OBLIQUE_CRUNCH_PREP_TWO'
            ],
            execution_steps=[
                'E_D_OBLIQUE_CRUNCH_EXEC_ONE',
                'E_D_OBLIQUE_CRUNCH_EXEC_TWO'
            ],
            key_tips=[
                'E_D_OBLIQUE_CRUNCH_TIP_ONE',
                'E_D_OBLIQUE_CRUNCH_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 227: Oblique V Up
        ExerciseDefinition(
            id='exercise-227',
            title= "E_D_OBLIQUE_V_UP_TITLE",
            video_urls=['regular_directory/exercises/videos/oblique_v_up.mp4'],
            cover_image_url=['regular_directory/exercises/images/oblique_v_up.png'],
            preparation_steps=[
                'E_D_OBLIQUE_V_UP_PREP_ONE',
                'E_D_OBLIQUE_V_UP_PREP_TWO'
            ],
            execution_steps=[
                'E_D_OBLIQUE_V_UP_EXEC_ONE',
                'E_D_OBLIQUE_V_UP_EXEC_TWO'
            ],
            key_tips=[
                'E_D_OBLIQUE_V_UP_TIP_ONE',
                'E_D_OBLIQUE_V_UP_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 228: Overhead Press (Close Grip): Barbell
        ExerciseDefinition(
            id='exercise-228',
            title= "E_D_OVERHEAD_PRESS_CLOSE_GRIP_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/overhead_press_close_grip_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/overhead_press_close_grip_barbell.png'],
            preparation_steps=[
                'E_D_OVERHEAD_PRESS_CLOSE_GRIP_BARBELL_PREP_ONE',
                'E_D_OVERHEAD_PRESS_CLOSE_GRIP_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_OVERHEAD_PRESS_CLOSE_GRIP_BARBELL_EXEC_ONE',
                'E_D_OVERHEAD_PRESS_CLOSE_GRIP_BARBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_OVERHEAD_PRESS_CLOSE_GRIP_BARBELL_TIP_ONE',
                'E_D_OVERHEAD_PRESS_CLOSE_GRIP_BARBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 229: Overhead Press (Wide Grip): Barbell
        ExerciseDefinition(
            id='exercise-229',
            title= "E_D_OVERHEAD_PRESS_WIDE_GRIP_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/overhead_press_wide_grip_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/overhead_press_wide_grip_barbell.png'],
            preparation_steps=[
                'E_D_OVERHEAD_PRESS_WIDE_GRIP_BARBELL_PREP_ONE',
                'E_D_OVERHEAD_PRESS_WIDE_GRIP_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_OVERHEAD_PRESS_WIDE_GRIP_BARBELL_EXEC_ONE',
                'E_D_OVERHEAD_PRESS_WIDE_GRIP_BARBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_OVERHEAD_PRESS_WIDE_GRIP_BARBELL_TIP_ONE',
                'E_D_OVERHEAD_PRESS_WIDE_GRIP_BARBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 230: Overhead Press: Band
        ExerciseDefinition(
            id='exercise-230',
            title= "E_D_OVERHEAD_PRESS_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/overhead_press_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/overhead_press_band.png'],
            preparation_steps=[
                'E_D_OVERHEAD_PRESS_BAND_PREP_ONE',
                'E_D_OVERHEAD_PRESS_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_OVERHEAD_PRESS_BAND_EXEC_ONE',
                'E_D_OVERHEAD_PRESS_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_OVERHEAD_PRESS_BAND_TIP_ONE',
                'E_D_OVERHEAD_PRESS_BAND_TIP_TWO'
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 231: Overhead Press: Barbell
        ExerciseDefinition(
            id='exercise-231',
            title= "E_D_OVERHEAD_PRESS_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/overhead_press_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/overhead_press_barbell.png'],
            preparation_steps=[
                'E_D_OVERHEAD_PRESS_BARBELL_PREP_ONE',
                'E_D_OVERHEAD_PRESS_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_OVERHEAD_PRESS_BARBELL_EXEC_ONE',
                'E_D_OVERHEAD_PRESS_BARBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_OVERHEAD_PRESS_BARBELL_TIP_ONE',
                'E_D_OVERHEAD_PRESS_BARBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 232: Overhead Press: Cable
        ExerciseDefinition(
            id='exercise-232',
            title= "E_D_OVERHEAD_PRESS_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/overhead_press_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/overhead_press_cable.png'],
            preparation_steps=[
                'E_D_OVERHEAD_PRESS_CABLE_PREP_ONE',
                'E_D_OVERHEAD_PRESS_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_OVERHEAD_PRESS_CABLE_EXEC_ONE',
                'E_D_OVERHEAD_PRESS_CABLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_OVERHEAD_PRESS_CABLE_TIP_ONE',
                'E_D_OVERHEAD_PRESS_CABLE_TIP_TWO'
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 233: Overhead Press: Dumbbell
        ExerciseDefinition(
            id='exercise-233',
            title= "E_D_OVERHEAD_PRESS_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/overhead_press_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/overhead_press_dumbbell.png'],
            preparation_steps=[
                'E_D_OVERHEAD_PRESS_DUMBBELL_PREP_ONE',
                'E_D_OVERHEAD_PRESS_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_OVERHEAD_PRESS_DUMBBELL_EXEC_ONE',
                'E_D_OVERHEAD_PRESS_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_OVERHEAD_PRESS_DUMBBELL_TIP_ONE',
                'E_D_OVERHEAD_PRESS_DUMBBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 234: Overhead Press: Kettlebell
        ExerciseDefinition(
            id='exercise-234',
            title= "E_D_OVERHEAD_PRESS_KETTLEBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/overhead_press_kettlebell.mp4'],
            cover_image_url=['regular_directory/exercises/images/overhead_press_kettlebell.png'],
            preparation_steps=[
                'E_D_OVERHEAD_PRESS_KETTLEBELL_PREP_ONE',
                'E_D_OVERHEAD_PRESS_KETTLEBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_OVERHEAD_PRESS_KETTLEBELL_EXEC_ONE',
                'E_D_OVERHEAD_PRESS_KETTLEBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_OVERHEAD_PRESS_KETTLEBELL_TIP_ONE',
                'E_D_OVERHEAD_PRESS_KETTLEBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.KETTLEBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 235: Overhead Press: Smith Machine
        
        # Exercise 236: Overhead Press
        
        # Exercise 237: Overhead Squat: Barbell
        ExerciseDefinition(
            id='exercise-237',
            title= "E_D_OVERHEAD_SQUAT_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/overhead_squat_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/overhead_squat_barbell.png'],
            preparation_steps=[
                'E_D_OVERHEAD_SQUAT_BARBELL_PREP_ONE',
                'E_D_OVERHEAD_SQUAT_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_OVERHEAD_SQUAT_BARBELL_EXEC_ONE',
                'E_D_OVERHEAD_SQUAT_BARBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_OVERHEAD_SQUAT_BARBELL_TIP_ONE',
                'E_D_OVERHEAD_SQUAT_BARBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG, FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 238: Overhead Triceps Extension: Band
        
        # Exercise 239: Overhead Triceps Extension: Barbell
        
        # Exercise 240: Overhead Triceps Extension: Cable
        
        # Exercise 241: Overhead Triceps Extension: Dumbbell
        
        # Exercise 242: Pec Deck Fly: Machine
        ExerciseDefinition(
            id='exercise-242',
            title= "E_D_PEC_DECK_FLY_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/pec_deck_fly_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/pec_deck_fly_machine.png'],
            preparation_steps=[
                'E_D_PEC_DECK_FLY_MACHINE_PREP_ONE',
                'E_D_PEC_DECK_FLY_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PEC_DECK_FLY_MACHINE_EXEC_ONE',
                'E_D_PEC_DECK_FLY_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PEC_DECK_FLY_MACHINE_TIP_ONE',
                'E_D_PEC_DECK_FLY_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.CHEST],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 243: Pendlay Row: Barbell
        ExerciseDefinition(
            id='exercise-243',
            title= "E_D_PENDLAY_ROW_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/pendlay_row_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/pendlay_row_barbell.png'],
            preparation_steps=[
                'E_D_PENDLAY_ROW_BARBELL_PREP_ONE',
                'E_D_PENDLAY_ROW_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PENDLAY_ROW_BARBELL_EXEC_ONE',
                'E_D_PENDLAY_ROW_BARBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PENDLAY_ROW_BARBELL_TIP_ONE',
                'E_D_PENDLAY_ROW_BARBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        # Exercise 244: Pike Push-up Feet On Bench
        ExerciseDefinition(
            id='exercise-244',
            title= "E_D_PIKE_PUSH_UP_FEET_ON_BENCH_TITLE",
            video_urls=['regular_directory/exercises/videos/pike_push_up_feet_on_bench.mp4'],
            cover_image_url=['regular_directory/exercises/images/pike_push_up_feet_on_bench.png'],
            preparation_steps=[
                'E_D_PIKE_PUSH_UP_FEET_ON_BENCH_PREP_ONE',
                'E_D_PIKE_PUSH_UP_FEET_ON_BENCH_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PIKE_PUSH_UP_FEET_ON_BENCH_EXEC_ONE',
                'E_D_PIKE_PUSH_UP_FEET_ON_BENCH_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PIKE_PUSH_UP_FEET_ON_BENCH_TIP_ONE',
                'E_D_PIKE_PUSH_UP_FEET_ON_BENCH_TIP_TWO'
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.ARM, FocusArea.CHEST],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 245: Pike Push-up
        ExerciseDefinition(
            id='exercise-245',
            title= "E_D_PIKE_PUSH_UP_TITLE",
            video_urls=['regular_directory/exercises/videos/pike_push_up.mp4'],
            cover_image_url=['regular_directory/exercises/images/pike_push_up.png'],
            preparation_steps=[
                'E_D_PIKE_PUSH_UP_PREP_ONE',
                'E_D_PIKE_PUSH_UP_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PIKE_PUSH_UP_EXEC_ONE',
                'E_D_PIKE_PUSH_UP_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PIKE_PUSH_UP_TIP_ONE',
                'E_D_PIKE_PUSH_UP_TIP_TWO'
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.ARM, FocusArea.CHEST],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 246: Pistol Squat
        ExerciseDefinition(
            id='exercise-246',
            title= "E_D_PISTOL_SQUAT_TITLE",
            video_urls=['regular_directory/exercises/videos/pistol_squat.mp4'],
            cover_image_url=['regular_directory/exercises/images/pistol_squat.png'],
            preparation_steps=[
                'E_D_PISTOL_SQUAT_PREP_ONE',
                'E_D_PISTOL_SQUAT_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PISTOL_SQUAT_EXEC_ONE',
                'E_D_PISTOL_SQUAT_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PISTOL_SQUAT_TIP_ONE',
                'E_D_PISTOL_SQUAT_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 247: Plank
        ExerciseDefinition(
            id='exercise-247',
            title= "E_D_PLANK_TITLE",
            video_urls=['regular_directory/exercises/videos/plank.mp4'],
            cover_image_url=['regular_directory/exercises/images/plank.png'],
            preparation_steps=[
                'E_D_PLANK_PREP_ONE',
                'E_D_PLANK_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PLANK_EXEC_ONE',
                'E_D_PLANK_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PLANK_TIP_ONE',
                'E_D_PLANK_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN, FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.TIME_BASED # Time-based (hold position)
        ),
        # Exercise 248: Power Clean: Barbell
        ExerciseDefinition(
            id='exercise-248',
            title= "E_D_POWER_CLEAN_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/power_clean_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/power_clean_barbell.png'],
            preparation_steps=[
                'E_D_POWER_CLEAN_BARBELL_PREP_ONE',
                'E_D_POWER_CLEAN_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_POWER_CLEAN_BARBELL_EXEC_ONE',
                'E_D_POWER_CLEAN_BARBELL_EXEC_TWO',
                'E_D_POWER_CLEAN_BARBELL_EXEC_THREE'
            ],
            key_tips=[
                'E_D_POWER_CLEAN_BARBELL_TIP_ONE',
                'E_D_POWER_CLEAN_BARBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        # Exercise 249: Power Push Away
        ExerciseDefinition(
            id='exercise-249',
            title= "E_D_POWER_PUSH_AWAY_TITLE",
            video_urls=['regular_directory/exercises/videos/power_push_away.mp4'],
            cover_image_url=['regular_directory/exercises/images/power_push_away.png'],
            preparation_steps=[
                'E_D_POWER_PUSH_AWAY_PREP_ONE',
                'E_D_POWER_PUSH_AWAY_PREP_TWO'
            ],
            execution_steps=[
                'E_D_POWER_PUSH_AWAY_EXEC_ONE',
                'E_D_POWER_PUSH_AWAY_EXEC_TWO'
            ],
            key_tips=[
                'E_D_POWER_PUSH_AWAY_TIP_ONE'
            ],
            focus_areas=[FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 250: Power Snatch: Barbell
        ExerciseDefinition(
            id='exercise-250',
            title= "E_D_POWER_SNATCH_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/power_snatch_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/power_snatch_barbell.png'],
            preparation_steps=[
                'E_D_POWER_SNATCH_BARBELL_PREP_ONE',
                'E_D_POWER_SNATCH_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_POWER_SNATCH_BARBELL_EXEC_ONE',
                'E_D_POWER_SNATCH_BARBELL_EXEC_TWO',
                'E_D_POWER_SNATCH_BARBELL_EXEC_THREE'
            ],
            key_tips=[
                'E_D_POWER_SNATCH_BARBELL_TIP_ONE',
                'E_D_POWER_SNATCH_BARBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        # Exercise 251: Prayer Push
        ExerciseDefinition(
            id='exercise-251',
            title= "E_D_PRAYER_PUSH_TITLE",
            video_urls=['regular_directory/exercises/videos/prayer_push.mp4'],
            cover_image_url=['regular_directory/exercises/images/prayer_push.png'],
            preparation_steps=[
                'E_D_PRAYER_PUSH_PREP_ONE'
            ],
            execution_steps=[
                'E_D_PRAYER_PUSH_EXEC_ONE',
                'E_D_PRAYER_PUSH_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PRAYER_PUSH_TIP_ONE',
                'E_D_PRAYER_PUSH_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 252: Preacher Curl: Barbell
        ExerciseDefinition(
            id='exercise-252',
            title= "E_D_PREACHER_CURL_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/preacher_curl_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/preacher_curl_barbell.png'],
            preparation_steps=[
                'E_D_PREACHER_CURL_BARBELL_PREP_ONE',
                'E_D_PREACHER_CURL_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PREACHER_CURL_BARBELL_EXEC_ONE',
                'E_D_PREACHER_CURL_BARBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PREACHER_CURL_BARBELL_TIP_ONE',
                'E_D_PREACHER_CURL_BARBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 253: Preacher Curl: Cable
        ExerciseDefinition(
            id='exercise-253',
            title= "E_D_PREACHER_CURL_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/preacher_curl_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/preacher_curl_cable.png'],
            preparation_steps=[
                'E_D_PREACHER_CURL_CABLE_PREP_ONE',
                'E_D_PREACHER_CURL_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PREACHER_CURL_CABLE_EXEC_ONE',
                'E_D_PREACHER_CURL_CABLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PREACHER_CURL_CABLE_TIP_ONE',
                'E_D_PREACHER_CURL_CABLE_TIP_TWO'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 254: Preacher Curl: Dumbbell
        ExerciseDefinition(
            id='exercise-254',
            title= "E_D_PREACHER_CURL_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/preacher_curl_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/preacher_curl_dumbbell.png'],
            preparation_steps=[
                'E_D_PREACHER_CURL_DUMBBELL_PREP_ONE',
                'E_D_PREACHER_CURL_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PREACHER_CURL_DUMBBELL_EXEC_ONE',
                'E_D_PREACHER_CURL_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PREACHER_CURL_DUMBBELL_TIP_ONE',
                'E_D_PREACHER_CURL_DUMBBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 255: Preacher Curl: Machine
        ExerciseDefinition(
            id='exercise-255',
            title= "E_D_PREACHER_CURL_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/preacher_curl_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/preacher_curl_machine.png'],
            preparation_steps=[
                'E_D_PREACHER_CURL_MACHINE_PREP_ONE',
                'E_D_PREACHER_CURL_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PREACHER_CURL_MACHINE_EXEC_ONE',
                'E_D_PREACHER_CURL_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PREACHER_CURL_MACHINE_TIP_ONE',
                'E_D_PREACHER_CURL_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 256: Prone Flutter Kicks
        ExerciseDefinition(
            id='exercise-256',
            title= "E_D_PRONE_FLUTTER_KICKS_TITLE",
            video_urls=['regular_directory/exercises/videos/prone_flutter_kicks.mp4'],
            cover_image_url=['regular_directory/exercises/images/prone_flutter_kicks.png'],
            preparation_steps=[
                'E_D_PRONE_FLUTTER_KICKS_PREP_ONE'
            ],
            execution_steps=[
                'E_D_PRONE_FLUTTER_KICKS_EXEC_ONE',
                'E_D_PRONE_FLUTTER_KICKS_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PRONE_FLUTTER_KICKS_TIP_ONE',
                'E_D_PRONE_FLUTTER_KICKS_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN, FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 257: Pull Apart: Band
        ExerciseDefinition(
            id='exercise-257',
            title= "E_D_PULL_APART_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/pull_apart_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/pull_apart_band.png'],
            preparation_steps=[
                'E_D_PULL_APART_BAND_PREP_ONE',
                'E_D_PULL_APART_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PULL_APART_BAND_EXEC_ONE',
                'E_D_PULL_APART_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PULL_APART_BAND_TIP_ONE',
                'E_D_PULL_APART_BAND_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 258: Pull Up (Assisted)
        ExerciseDefinition(
            id='exercise-258',
            title= "E_D_PULL_UP_ASSISTED_TITLE",
            video_urls=['regular_directory/exercises/videos/pull_up_assisted.mp4'],
            cover_image_url=['regular_directory/exercises/images/pull_up_assisted.png'],
            preparation_steps=[
                'E_D_PULL_UP_ASSISTED_PREP_ONE',
                'E_D_PULL_UP_ASSISTED_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PULL_UP_ASSISTED_EXEC_ONE',
                'E_D_PULL_UP_ASSISTED_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PULL_UP_ASSISTED_TIP_ONE',
                'E_D_PULL_UP_ASSISTED_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.WEIGHT_MACHINE, # Assuming an assisted machine or a very heavy band (using weight machine as nearest enum)
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 259: Pull Up (Close Grip)
        ExerciseDefinition(
            id='exercise-259',
            title= "E_D_PULL_UP_CLOSE_GRIP_TITLE",
            video_urls=['regular_directory/exercises/videos/pull_up_close_grip.mp4'],
            cover_image_url=['regular_directory/exercises/images/pull_up_close_grip.png'],
            preparation_steps=[
                'E_D_PULL_UP_CLOSE_GRIP_PREP_ONE',
                'E_D_PULL_UP_CLOSE_GRIP_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PULL_UP_CLOSE_GRIP_EXEC_ONE',
                'E_D_PULL_UP_CLOSE_GRIP_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PULL_UP_CLOSE_GRIP_TIP_ONE',
                'E_D_PULL_UP_CLOSE_GRIP_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 260: Pull Up (Reverse Grip)
        ExerciseDefinition(
            id='exercise-260',
            title= "E_D_PULL_UP_REVERSE_GRIP_TITLE",
            video_urls=['regular_directory/exercises/videos/pull_up_reverse_grip.mp4'],
            cover_image_url=['regular_directory/exercises/images/pull_up_reverse_grip.png'],
            preparation_steps=[
                'E_D_PULL_UP_REVERSE_GRIP_PREP_ONE',
                'E_D_PULL_UP_REVERSE_GRIP_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PULL_UP_REVERSE_GRIP_EXEC_ONE',
                'E_D_PULL_UP_REVERSE_GRIP_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PULL_UP_REVERSE_GRIP_TIP_ONE',
                'E_D_PULL_UP_REVERSE_GRIP_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 261: Pull Up (Wide Grip)
        ExerciseDefinition(
            id='exercise-261',
            title= "E_D_PULL_UP_WIDE_GRIP_TITLE",
            video_urls=['regular_directory/exercises/videos/pull_up_wide_grip.mp4'],
            cover_image_url=['regular_directory/exercises/images/pull_up_wide_grip.png'],
            preparation_steps=[
                'E_D_PULL_UP_WIDE_GRIP_PREP_ONE',
                'E_D_PULL_UP_WIDE_GRIP_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PULL_UP_WIDE_GRIP_EXEC_ONE',
                'E_D_PULL_UP_WIDE_GRIP_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PULL_UP_WIDE_GRIP_TIP_ONE',
                'E_D_PULL_UP_WIDE_GRIP_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 262: Pull Up: Band
        ExerciseDefinition(
            id='exercise-262',
            title= "E_D_PULL_UP_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/pull_up_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/pull_up_band.png'],
            preparation_steps=[
                'E_D_PULL_UP_BAND_PREP_ONE',
                'E_D_PULL_UP_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PULL_UP_BAND_EXEC_ONE',
                'E_D_PULL_UP_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PULL_UP_BAND_TIP_ONE',
                'E_D_PULL_UP_BAND_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 263: Pull Up: Plate
        ExerciseDefinition(
            id='exercise-263',
            title= "E_D_PULL_UP_PLATE_TITLE",
            video_urls=['regular_directory/exercises/videos/pull_up_plate.mp4'],
            cover_image_url=['regular_directory/exercises/images/pull_up_plate.png'],
            preparation_steps=[
                'E_D_PULL_UP_PLATE_PREP_ONE',
                'E_D_PULL_UP_PLATE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PULL_UP_PLATE_EXEC_ONE',
                'E_D_PULL_UP_PLATE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PULL_UP_PLATE_TIP_ONE',
                'E_D_PULL_UP_PLATE_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.BODY_WEIGHT, # Plate is just used to add external weight to bodyweight exercise
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 264: Pull Up
        ExerciseDefinition(
            id='exercise-264',
            title= "E_D_PULL_UP_TITLE",
            video_urls=['regular_directory/exercises/videos/pull_up.mp4'],
            cover_image_url=['regular_directory/exercises/images/pull_up.png'],
            preparation_steps=[
                'E_D_PULL_UP_PREP_ONE',
                'E_D_PULL_UP_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PULL_UP_EXEC_ONE',
                'E_D_PULL_UP_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PULL_UP_TIP_ONE',
                'E_D_PULL_UP_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 265: Pullover: Barbell
        ExerciseDefinition(
            id='exercise-265',
            title= "E_D_PULLOVER_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/pullover_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/pullover_barbell.png'],
            preparation_steps=[
                'E_D_PULLOVER_BARBELL_PREP_ONE',
                'E_D_PULLOVER_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PULLOVER_BARBELL_EXEC_ONE',
                'E_D_PULLOVER_BARBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PULLOVER_BARBELL_TIP_ONE',
                'E_D_PULLOVER_BARBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.BACK],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 266: Pullover - Dumbbell
        ExerciseDefinition(
            id='exercise-266',
            title= "E_D_PULLOVER_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/pullover_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/pullover_dumbbell.png'],
            preparation_steps=[
                'E_D_PULLOVER_DUMBBELL_PREP_ONE',
                'E_D_PULLOVER_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PULLOVER_DUMBBELL_EXEC_ONE',
                'E_D_PULLOVER_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PULLOVER_DUMBBELL_TIP_ONE',
                'E_D_PULLOVER_DUMBBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.BACK],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 267: Pullover: Cable
        ExerciseDefinition(
            id='exercise-267',
            title= "E_D_PULLOVER_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/pullover_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/pullover_cable.png'],
            preparation_steps=[
                'E_D_PULLOVER_CABLE_PREP_ONE',
                'E_D_PULLOVER_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PULLOVER_CABLE_EXEC_ONE',
                'E_D_PULLOVER_CABLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PULLOVER_CABLE_TIP_ONE',
                'E_D_PULLOVER_CABLE_TIP_TWO'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.BACK],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 268: Pullover: Machine
        ExerciseDefinition(
            id='exercise-268',
            title= "E_D_PULLOVER_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/pullover_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/pullover_machine.png'],
            preparation_steps=[
                'E_D_PULLOVER_MACHINE_PREP_ONE',
                'E_D_PULLOVER_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PULLOVER_MACHINE_EXEC_ONE',
                'E_D_PULLOVER_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PULLOVER_MACHINE_TIP_ONE',
                'E_D_PULLOVER_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.BACK],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 269: Push Press: Barbell
        ExerciseDefinition(
            id='exercise-269',
            title= "E_D_PUSH_PRESS_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/push_press_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/push_press_barbell.png'],
            preparation_steps=[
                'E_D_PUSH_PRESS_BARBELL_PREP_ONE',
                'E_D_PUSH_PRESS_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PUSH_PRESS_BARBELL_EXEC_ONE',
                'E_D_PUSH_PRESS_BARBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PUSH_PRESS_BARBELL_TIP_ONE',
                'E_D_PUSH_PRESS_BARBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 270: Push-Up: Band
        ExerciseDefinition(
            id='exercise-270',
            title= "E_D_PUSH_UP_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/push_up_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/push_up_band.png'],
            preparation_steps=[
                'E_D_PUSH_UP_BAND_PREP_ONE',
                'E_D_PUSH_UP_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PUSH_UP_BAND_EXEC_ONE',
                'E_D_PUSH_UP_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PUSH_UP_BAND_TIP_ONE',
                'E_D_PUSH_UP_BAND_TIP_TWO'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.ARM, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 271: Push-Up Row: Dumbbell
        ExerciseDefinition(
            id='exercise-271',
            title= "E_D_PUSH_UP_ROW_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/push_up_row_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/push_up_row_dumbbell.png'],
            preparation_steps=[
                'E_D_PUSH_UP_ROW_DUMBBELL_PREP_ONE',
                'E_D_PUSH_UP_ROW_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PUSH_UP_ROW_DUMBBELL_EXEC_ONE',
                'E_D_PUSH_UP_ROW_DUMBBELL_EXEC_TWO',
                'E_D_PUSH_UP_ROW_DUMBBELL_EXEC_THREE'
            ],
            key_tips=[
                'E_D_PUSH_UP_ROW_DUMBBELL_TIP_ONE',
                'E_D_PUSH_UP_ROW_DUMBBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.BACK, FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 272: Push-Up to Side Plank
        ExerciseDefinition(
            id='exercise-272',
            title= "E_D_PUSH_UP_TO_SIDE_PLANK_TITLE",
            video_urls=['regular_directory/exercises/videos/push_up_to_side_plank.mp4'],
            cover_image_url=['regular_directory/exercises/images/push_up_to_side_plank.png'],
            preparation_steps=[
                'E_D_PUSH_UP_TO_SIDE_PLANK_PREP_ONE'
            ],
            execution_steps=[
                'E_D_PUSH_UP_TO_SIDE_PLANK_EXEC_ONE',
                'E_D_PUSH_UP_TO_SIDE_PLANK_EXEC_TWO',
                'E_D_PUSH_UP_TO_SIDE_PLANK_EXEC_THREE'
            ],
            key_tips=[
                'E_D_PUSH_UP_TO_SIDE_PLANK_TIP_ONE',
                'E_D_PUSH_UP_TO_SIDE_PLANK_TIP_TWO'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.ABDOMEN, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 273: Push-Up
        ExerciseDefinition(
            id='exercise-273',
            title= "E_D_PUSH_UP_TITLE",
            video_urls=['regular_directory/exercises/videos/push_up.mp4'],
            cover_image_url=['regular_directory/exercises/images/push_up.png'],
            preparation_steps=[
                'E_D_PUSH_UP_PREP_ONE',
                'E_D_PUSH_UP_PREP_TWO'
            ],
            execution_steps=[
                'E_D_PUSH_UP_EXEC_ONE',
                'E_D_PUSH_UP_EXEC_TWO'
            ],
            key_tips=[
                'E_D_PUSH_UP_TIP_ONE',
                'E_D_PUSH_UP_TIP_TWO'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.ARM, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 274: Rack Pull: Barbell
        ExerciseDefinition(
            id='exercise-274',
            title= "E_D_RACK_PULL_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/rack_pull_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/rack_pull_barbell.png'],
            preparation_steps=[
                'E_D_RACK_PULL_BARBELL_PREP_ONE',
                'E_D_RACK_PULL_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_RACK_PULL_BARBELL_EXEC_ONE',
                'E_D_RACK_PULL_BARBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_RACK_PULL_BARBELL_TIP_ONE',
                'E_D_RACK_PULL_BARBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.LEG, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        # Exercise 275: Renegade Row: Kettlebell
        ExerciseDefinition(
            id='exercise-275',
            title= "E_D_RENEGADE_ROW_KETTLEBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/renegade_row_kettlebell.mp4'],
            cover_image_url=['regular_directory/exercises/images/renegade_row_kettlebell.png'],
            preparation_steps=[
                'E_D_RENEGADE_ROW_KETTLEBELL_PREP_ONE',
                'E_D_RENEGADE_ROW_KETTLEBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_RENEGADE_ROW_KETTLEBELL_EXEC_ONE',
                'E_D_RENEGADE_ROW_KETTLEBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_RENEGADE_ROW_KETTLEBELL_TIP_ONE',
                'E_D_RENEGADE_ROW_KETTLEBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.KETTLEBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 276: Renegade Row: Dumbbell
        ExerciseDefinition(
            id='exercise-276',
            title= "E_D_RENEGADE_ROW_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/renegade_row_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/renegade_row_dumbbell.png'],
            preparation_steps=[
                'E_D_RENEGADE_ROW_DUMBBELL_PREP_ONE',
                'E_D_RENEGADE_ROW_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_RENEGADE_ROW_DUMBBELL_EXEC_ONE',
                'E_D_RENEGADE_ROW_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_RENEGADE_ROW_DUMBBELL_TIP_ONE',
                'E_D_RENEGADE_ROW_DUMBBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 277: Reverse Concentration Curl: Dumbbell
        ExerciseDefinition(
            id='exercise-277',
            title= "E_D_REVERSE_CONCENTRATION_CURL_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/reverse_concentration_curl_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/reverse_concentration_curl_dumbbell.png'],
            preparation_steps=[
                'E_D_REVERSE_CONCENTRATION_CURL_DUMBBELL_PREP_ONE',
                'E_D_REVERSE_CONCENTRATION_CURL_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_REVERSE_CONCENTRATION_CURL_DUMBBELL_EXEC_ONE',
                'E_D_REVERSE_CONCENTRATION_CURL_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_REVERSE_CONCENTRATION_CURL_DUMBBELL_TIP_ONE'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 278: Reverse Crunch: Cable
        ExerciseDefinition(
            id='exercise-278',
            title= "E_D_REVERSE_CRUNCH_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/reverse_crunch_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/reverse_crunch_cable.png'],
            preparation_steps=[
                'E_D_REVERSE_CRUNCH_CABLE_PREP_ONE',
                'E_D_REVERSE_CRUNCH_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_REVERSE_CRUNCH_CABLE_EXEC_ONE',
                'E_D_REVERSE_CRUNCH_CABLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_REVERSE_CRUNCH_CABLE_TIP_ONE',
                'E_D_REVERSE_CRUNCH_CABLE_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 279: Reverse Crunch: Machine
        ExerciseDefinition(
            id='exercise-279',
            title= "E_D_REVERSE_CRUNCH_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/reverse_crunch_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/reverse_crunch_machine.png'],
            preparation_steps=[
                'E_D_REVERSE_CRUNCH_MACHINE_PREP_ONE',
                'E_D_REVERSE_CRUNCH_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_REVERSE_CRUNCH_MACHINE_EXEC_ONE',
                'E_D_REVERSE_CRUNCH_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_REVERSE_CRUNCH_MACHINE_TIP_ONE',
                'E_D_REVERSE_CRUNCH_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 280: Reverse Crunch
        ExerciseDefinition(
            id='exercise-280',
            title= "E_D_REVERSE_CRUNCH_TITLE",
            video_urls=['regular_directory/exercises/videos/reverse_crunch.mp4'],
            cover_image_url=['regular_directory/exercises/images/reverse_crunch.png'],
            preparation_steps=[
                'E_D_REVERSE_CRUNCH_PREP_ONE',
                'E_D_REVERSE_CRUNCH_PREP_TWO'
            ],
            execution_steps=[
                'E_D_REVERSE_CRUNCH_EXEC_ONE',
                'E_D_REVERSE_CRUNCH_EXEC_TWO'
            ],
            key_tips=[
                'E_D_REVERSE_CRUNCH_TIP_ONE',
                'E_D_REVERSE_CRUNCH_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 281: Reverse Curl: Band
        ExerciseDefinition(
            id='exercise-281',
            title= "E_D_REVERSE_CURL_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/reverse_curl_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/reverse_curl_band.png'],
            preparation_steps=[
                'E_D_REVERSE_CURL_BAND_PREP_ONE',
                'E_D_REVERSE_CURL_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_REVERSE_CURL_BAND_EXEC_ONE',
                'E_D_REVERSE_CURL_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_REVERSE_CURL_BAND_TIP_ONE'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 282: Reverse Curl: Barbell
        ExerciseDefinition(
            id='exercise-282',
            title= "E_D_REVERSE_CURL_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/reverse_curl_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/reverse_curl_barbell.png'],
            preparation_steps=[
                'E_D_REVERSE_CURL_BARBELL_PREP_ONE',
                'E_D_REVERSE_CURL_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_REVERSE_CURL_BARBELL_EXEC_ONE',
                'E_D_REVERSE_CURL_BARBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_REVERSE_CURL_BARBELL_TIP_ONE'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 283: Reverse Curl: Cable
        ExerciseDefinition(
            id='exercise-283',
            title= "E_D_REVERSE_CURL_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/reverse_curl_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/reverse_curl_cable.png'],
            preparation_steps=[
                'E_D_REVERSE_CURL_CABLE_PREP_ONE',
                'E_D_REVERSE_CURL_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_REVERSE_CURL_CABLE_EXEC_ONE',
                'E_D_REVERSE_CURL_CABLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_REVERSE_CURL_CABLE_TIP_ONE'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 284: Reverse Curl: Dumbbell
        ExerciseDefinition(
            id='exercise-284',
            title= "E_D_REVERSE_CURL_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/reverse_curl_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/reverse_curl_dumbbell.png'],
            preparation_steps=[
                'E_D_REVERSE_CURL_DUMBBELL_PREP_ONE',
                'E_D_REVERSE_CURL_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_REVERSE_CURL_DUMBBELL_EXEC_ONE',
                'E_D_REVERSE_CURL_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_REVERSE_CURL_DUMBBELL_TIP_ONE'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 285: Reverse Plank
        ExerciseDefinition(
            id='exercise-285',
            title= "E_D_REVERSE_PLANK_TITLE",
            video_urls=['regular_directory/exercises/videos/reverse_plank.mp4'],
            cover_image_url=['regular_directory/exercises/images/reverse_plank.png'],
            preparation_steps=[
                'E_D_REVERSE_PLANK_PREP_ONE',
                'E_D_REVERSE_PLANK_PREP_TWO'
            ],
            execution_steps=[
                'E_D_REVERSE_PLANK_EXEC_ONE',
                'E_D_REVERSE_PLANK_EXEC_TWO'
            ],
            key_tips=[
                'E_D_REVERSE_PLANK_TIP_ONE',
                'E_D_REVERSE_PLANK_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.TIME_BASED # Time-based (hold position)
        ),
        # Exercise 286: Reverse Wrist Curl: Band
        ExerciseDefinition(
            id='exercise-286',
            title= "E_D_REVERSE_WRIST_CURL_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/reverse_wrist_curl_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/reverse_wrist_curl_band.png'],
            preparation_steps=[
                'E_D_REVERSE_WRIST_CURL_BAND_PREP_ONE',
                'E_D_REVERSE_WRIST_CURL_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_REVERSE_WRIST_CURL_BAND_EXEC_ONE',
                'E_D_REVERSE_WRIST_CURL_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_REVERSE_WRIST_CURL_BAND_TIP_ONE'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 287: Reverse Wrist Curl: Barbell
        ExerciseDefinition(
            id='exercise-287',
            title= "E_D_REVERSE_WRIST_CURL_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/reverse_wrist_curl_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/reverse_wrist_curl_barbell.png'],
            preparation_steps=[
                'E_D_REVERSE_WRIST_CURL_BARBELL_PREP_ONE',
                'E_D_REVERSE_WRIST_CURL_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_REVERSE_WRIST_CURL_BARBELL_EXEC_ONE',
                'E_D_REVERSE_WRIST_CURL_BARBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_REVERSE_WRIST_CURL_BARBELL_TIP_ONE'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 288: Reverse Wrist Curl: Cable
        ExerciseDefinition(
            id='exercise-288',
            title= "E_D_REVERSE_WRIST_CURL_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/reverse_wrist_curl_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/reverse_wrist_curl_cable.png'],
            preparation_steps=[
                'E_D_REVERSE_WRIST_CURL_CABLE_PREP_ONE',
                'E_D_REVERSE_WRIST_CURL_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_REVERSE_WRIST_CURL_CABLE_EXEC_ONE',
                'E_D_REVERSE_WRIST_CURL_CABLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_REVERSE_WRIST_CURL_CABLE_TIP_ONE'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 289: Reverse Wrist Curl: Dumbbell
        ExerciseDefinition(
            id='exercise-289',
            title= "E_D_REVERSE_WRIST_CURL_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/reverse_wrist_curl_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/reverse_wrist_curl_dumbbell.png'],
            preparation_steps=[
                'E_D_REVERSE_WRIST_CURL_DUMBBELL_PREP_ONE',
                'E_D_REVERSE_WRIST_CURL_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_REVERSE_WRIST_CURL_DUMBBELL_EXEC_ONE',
                'E_D_REVERSE_WRIST_CURL_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_REVERSE_WRIST_CURL_DUMBBELL_TIP_ONE'
            ],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 290: Romanian Deadlift: Barbell
        ExerciseDefinition(
            id='exercise-290',
            title= "E_D_ROMANIAN_DEADLIFT_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/romanian_deadlift_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/romanian_deadlift_barbell.png'],
            preparation_steps=[
                'E_D_ROMANIAN_DEADLIFT_BARBELL_PREP_ONE',
                'E_D_ROMANIAN_DEADLIFT_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_ROMANIAN_DEADLIFT_BARBELL_EXEC_ONE',
                'E_D_ROMANIAN_DEADLIFT_BARBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_ROMANIAN_DEADLIFT_BARBELL_TIP_ONE',
                'E_D_ROMANIAN_DEADLIFT_BARBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS, FocusArea.BACK],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
        ),
        # Exercise 291: Romanian Deadlift: Dumbbell
        ExerciseDefinition(
            id='exercise-291',
            title= "E_D_ROMANIAN_DEADLIFT_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/romanian_deadlift_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/romanian_deadlift_dumbbell.png'],
            preparation_steps=[
                'E_D_ROMANIAN_DEADLIFT_DUMBBELL_PREP_ONE',
                'E_D_ROMANIAN_DEADLIFT_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_ROMANIAN_DEADLIFT_DUMBBELL_EXEC_ONE',
                'E_D_ROMANIAN_DEADLIFT_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_ROMANIAN_DEADLIFT_DUMBBELL_TIP_ONE',
                'E_D_ROMANIAN_DEADLIFT_DUMBBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS, FocusArea.BACK],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 292: Row in Doorway
        ExerciseDefinition(
            id='exercise-292',
            title= "E_D_ROW_IN_DOORWAY_TITLE",
            video_urls=['regular_directory/exercises/videos/row_in_doorway.mp4'],
            cover_image_url=['regular_directory/exercises/images/row_in_doorway.png'],
            preparation_steps=[
                'E_D_ROW_IN_DOORWAY_PREP_ONE',
                'E_D_ROW_IN_DOORWAY_PREP_TWO'
            ],
            execution_steps=[
                'E_D_ROW_IN_DOORWAY_EXEC_ONE',
                'E_D_ROW_IN_DOORWAY_EXEC_TWO'
            ],
            key_tips=[
                'E_D_ROW_IN_DOORWAY_TIP_ONE',
                'E_D_ROW_IN_DOORWAY_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 293: Russian Twist: Dumbbell
        ExerciseDefinition(
            id='exercise-293',
            title= "E_D_RUSSIAN_TWIST_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/russian_twist_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/russian_twist_dumbbell.png'],
            preparation_steps=[
                'E_D_RUSSIAN_TWIST_DUMBBELL_PREP_ONE',
                'E_D_RUSSIAN_TWIST_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_RUSSIAN_TWIST_DUMBBELL_EXEC_ONE',
                'E_D_RUSSIAN_TWIST_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_RUSSIAN_TWIST_DUMBBELL_TIP_ONE',
                'E_D_RUSSIAN_TWIST_DUMBBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 294: Russian Twist
        ExerciseDefinition(
            id='exercise-294',
            title= "E_D_RUSSIAN_TWIST_TITLE",
            video_urls=['regular_directory/exercises/videos/russian_twist.mp4'],
            cover_image_url=['regular_directory/exercises/images/russian_twist.png'],
            preparation_steps=[
                'E_D_RUSSIAN_TWIST_PREP_ONE',
                'E_D_RUSSIAN_TWIST_PREP_TWO'
            ],
            execution_steps=[
                'E_D_RUSSIAN_TWIST_EXEC_ONE',
                'E_D_RUSSIAN_TWIST_EXEC_TWO'
            ],
            key_tips=[
                'E_D_RUSSIAN_TWIST_TIP_ONE',
                'E_D_RUSSIAN_TWIST_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 295: Seated Calf Press: Machine
        ExerciseDefinition(
            id='exercise-295',
            title= "E_D_SEATED_CALF_PRESS_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_calf_press_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_calf_press_machine.png'],
            preparation_steps=[
                'E_D_SEATED_CALF_PRESS_MACHINE_PREP_ONE',
                'E_D_SEATED_CALF_PRESS_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_CALF_PRESS_MACHINE_EXEC_ONE',
                'E_D_SEATED_CALF_PRESS_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_CALF_PRESS_MACHINE_TIP_ONE',
                'E_D_SEATED_CALF_PRESS_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 296: Seated Calf Raise: Barbell
        ExerciseDefinition(
            id='exercise-296',
            title= "E_D_SEATED_CALF_RAISE_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_calf_raise_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_calf_raise_barbell.png'],
            preparation_steps=[
                'E_D_SEATED_CALF_RAISE_BARBELL_PREP_ONE',
                'E_D_SEATED_CALF_RAISE_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_CALF_RAISE_BARBELL_EXEC_ONE',
                'E_D_SEATED_CALF_RAISE_BARBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_CALF_RAISE_BARBELL_TIP_ONE',
                'E_D_SEATED_CALF_RAISE_BARBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 297: Seated Calf Raise: Dumbbell
        ExerciseDefinition(
            id='exercise-297',
            title= "E_D_SEATED_CALF_RAISE_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_calf_raise_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_calf_raise_dumbbell.png'],
            preparation_steps=[
                'E_D_SEATED_CALF_RAISE_DUMBBELL_PREP_ONE',
                'E_D_SEATED_CALF_RAISE_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_CALF_RAISE_DUMBBELL_EXEC_ONE',
                'E_D_SEATED_CALF_RAISE_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_CALF_RAISE_DUMBBELL_TIP_ONE',
                'E_D_SEATED_CALF_RAISE_DUMBBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 298: Seated Calf Raise: Machine
        ExerciseDefinition(
            id='exercise-298',
            title= "E_D_SEATED_CALF_RAISE_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_calf_raise_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_calf_raise_machine.png'],
            preparation_steps=[
                'E_D_SEATED_CALF_RAISE_MACHINE_PREP_ONE',
                'E_D_SEATED_CALF_RAISE_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_CALF_RAISE_MACHINE_EXEC_ONE',
                'E_D_SEATED_CALF_RAISE_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_CALF_RAISE_MACHINE_TIP_ONE',
                'E_D_SEATED_CALF_RAISE_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 299: Seated Chest Fly: Machine
        ExerciseDefinition(
            id='exercise-299',
            title= "E_D_SEATED_CHEST_FLY_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_chest_fly_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_chest_fly_machine.png'],
            preparation_steps=[
                'E_D_SEATED_CHEST_FLY_MACHINE_PREP_ONE',
                'E_D_SEATED_CHEST_FLY_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_CHEST_FLY_MACHINE_EXEC_ONE',
                'E_D_SEATED_CHEST_FLY_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_CHEST_FLY_MACHINE_TIP_ONE',
                'E_D_SEATED_CHEST_FLY_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.CHEST],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 300: Seated Chest Press: Machine
        ExerciseDefinition(
            id='exercise-300',
            title= "E_D_SEATED_CHEST_PRESS_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_chest_press_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_chest_press_machine.png'],
            preparation_steps=[
                'E_D_SEATED_CHEST_PRESS_MACHINE_PREP_ONE',
                'E_D_SEATED_CHEST_PRESS_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_CHEST_PRESS_MACHINE_EXEC_ONE',
                'E_D_SEATED_CHEST_PRESS_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_CHEST_PRESS_MACHINE_TIP_ONE',
                'E_D_SEATED_CHEST_PRESS_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.CHEST, FocusArea.ARM, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 301: Seated Crunch: Machine
        ExerciseDefinition(
            id='exercise-301',
            title= "E_D_SEATED_CRUNCH_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_crunch_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_crunch_machine.png'],
            preparation_steps=[
                'E_D_SEATED_CRUNCH_MACHINE_PREP_ONE',
                'E_D_SEATED_CRUNCH_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_CRUNCH_MACHINE_EXEC_ONE',
                'E_D_SEATED_CRUNCH_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_CRUNCH_MACHINE_TIP_ONE',
                'E_D_SEATED_CRUNCH_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 302: Seated Hip Abductor: Machine
        ExerciseDefinition(
            id='exercise-302',
            title= "E_D_SEATED_HIP_ABDUCTOR_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_hip_abductor_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_hip_abductor_machine.png'],
            preparation_steps=[
                'E_D_SEATED_HIP_ABDUCTOR_MACHINE_PREP_ONE',
                'E_D_SEATED_HIP_ABDUCTOR_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_HIP_ABDUCTOR_MACHINE_EXEC_ONE',
                'E_D_SEATED_HIP_ABDUCTOR_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_HIP_ABDUCTOR_MACHINE_TIP_ONE',
                'E_D_SEATED_HIP_ABDUCTOR_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 303: Seated Hip Adductor: Machine
        ExerciseDefinition(
            id='exercise-303',
            title= "E_D_SEATED_HIP_ADDUCTOR_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_hip_adductor_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_hip_adductor_machine.png'],
            preparation_steps=[
                'E_D_SEATED_HIP_ADDUCTOR_MACHINE_PREP_ONE',
                'E_D_SEATED_HIP_ADDUCTOR_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_HIP_ADDUCTOR_MACHINE_EXEC_ONE',
                'E_D_SEATED_HIP_ADDUCTOR_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_HIP_ADDUCTOR_MACHINE_TIP_ONE',
                'E_D_SEATED_HIP_ADDUCTOR_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 304: Seated Hip External Rotation: Band
        ExerciseDefinition(
            id='exercise-304',
            title= "E_D_SEATED_HIP_EXTERNAL_ROTATION_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_hip_external_rotation_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_hip_external_rotation_band.png'],
            preparation_steps=[
                'E_D_SEATED_HIP_EXTERNAL_ROTATION_BAND_PREP_ONE',
                'E_D_SEATED_HIP_EXTERNAL_ROTATION_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_HIP_EXTERNAL_ROTATION_BAND_EXEC_ONE',
                'E_D_SEATED_HIP_EXTERNAL_ROTATION_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_HIP_EXTERNAL_ROTATION_BAND_TIP_ONE',
                'E_D_SEATED_HIP_EXTERNAL_ROTATION_BAND_TIP_TWO'
            ],
            focus_areas=[FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 305: Seated Hip Internal Rotation: Band
        ExerciseDefinition(
            id='exercise-305',
            title= "E_D_SEATED_HIP_INTERNAL_ROTATION_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_hip_internal_rotation_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_hip_internal_rotation_band.png'],
            preparation_steps=[
                'E_D_SEATED_HIP_INTERNAL_ROTATION_BAND_PREP_ONE',
                'E_D_SEATED_HIP_INTERNAL_ROTATION_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_HIP_INTERNAL_ROTATION_BAND_EXEC_ONE',
                'E_D_SEATED_HIP_INTERNAL_ROTATION_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_HIP_INTERNAL_ROTATION_BAND_TIP_ONE',
                'E_D_SEATED_HIP_INTERNAL_ROTATION_BAND_TIP_TWO'
            ],
            focus_areas=[FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 306: Seated In-And-Out: Dumbbell
        ExerciseDefinition(
            id='exercise-306',
            title= "E_D_SEATED_IN_AND_OUT_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_in_and_out_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_in_and_out_dumbbell.png'],
            preparation_steps=[
                'E_D_SEATED_IN_AND_OUT_DUMBBELL_PREP_ONE',
                'E_D_SEATED_IN_AND_OUT_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_IN_AND_OUT_DUMBBELL_EXEC_ONE',
                'E_D_SEATED_IN_AND_OUT_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_IN_AND_OUT_DUMBBELL_TIP_ONE',
                'E_D_SEATED_IN_AND_OUT_DUMBBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 307: Seated In-And-Out
        ExerciseDefinition(
            id='exercise-307',
            title= "E_D_SEATED_IN_AND_OUT_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_in_and_out.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_in_and_out.png'],
            preparation_steps=[
                'E_D_SEATED_IN_AND_OUT_PREP_ONE',
                'E_D_SEATED_IN_AND_OUT_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_IN_AND_OUT_EXEC_ONE',
                'E_D_SEATED_IN_AND_OUT_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_IN_AND_OUT_TIP_ONE',
                'E_D_SEATED_IN_AND_OUT_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 308: Seated Leg Curl: Machine
        ExerciseDefinition(
            id='exercise-308',
            title= "E_D_SEATED_LEG_CURL_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_leg_curl_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_leg_curl_machine.png'],
            preparation_steps=[
                'E_D_SEATED_LEG_CURL_MACHINE_PREP_ONE',
                'E_D_SEATED_LEG_CURL_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_LEG_CURL_MACHINE_EXEC_ONE',
                'E_D_SEATED_LEG_CURL_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_LEG_CURL_MACHINE_TIP_ONE',
                'E_D_SEATED_LEG_CURL_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 309: Seated Leg Press: Machine
        ExerciseDefinition(
            id='exercise-309',
            title= "E_D_SEATED_LEG_PRESS_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_leg_press_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_leg_press_machine.png'],
            preparation_steps=[
                'E_D_SEATED_LEG_PRESS_MACHINE_PREP_ONE',
                'E_D_SEATED_LEG_PRESS_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_LEG_PRESS_MACHINE_EXEC_ONE',
                'E_D_SEATED_LEG_PRESS_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_LEG_PRESS_MACHINE_TIP_ONE',
                'E_D_SEATED_LEG_PRESS_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 310: Seated Overhead Press: Barbell
        ExerciseDefinition(
            id='exercise-310',
            title= "E_D_SEATED_OVERHEAD_PRESS_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_overhead_press_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_overhead_press_barbell.png'],
            preparation_steps=[
                'E_D_SEATED_OVERHEAD_PRESS_BARBELL_PREP_ONE',
                'E_D_SEATED_OVERHEAD_PRESS_BARBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_OVERHEAD_PRESS_BARBELL_EXEC_ONE',
                'E_D_SEATED_OVERHEAD_PRESS_BARBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_OVERHEAD_PRESS_BARBELL_TIP_ONE',
                'E_D_SEATED_OVERHEAD_PRESS_BARBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 311: Seated Overhead Press: Dumbbell
        ExerciseDefinition(
            id='exercise-311',
            title= "E_D_SEATED_OVERHEAD_PRESS_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_overhead_press_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_overhead_press_dumbbell.png'],
            preparation_steps=[
                'E_D_SEATED_OVERHEAD_PRESS_DUMBBELL_PREP_ONE',
                'E_D_SEATED_OVERHEAD_PRESS_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_OVERHEAD_PRESS_DUMBBELL_EXEC_ONE',
                'E_D_SEATED_OVERHEAD_PRESS_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_OVERHEAD_PRESS_DUMBBELL_TIP_ONE',
                'E_D_SEATED_OVERHEAD_PRESS_DUMBBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 312: Seated Overhead Press: Machine
        ExerciseDefinition(
            id='exercise-312',
            title= "E_D_SEATED_OVERHEAD_PRESS_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_overhead_press_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_overhead_press_machine.png'],
            preparation_steps=[
                'E_D_SEATED_OVERHEAD_PRESS_MACHINE_PREP_ONE',
                'E_D_SEATED_OVERHEAD_PRESS_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_OVERHEAD_PRESS_MACHINE_EXEC_ONE',
                'E_D_SEATED_OVERHEAD_PRESS_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_OVERHEAD_PRESS_MACHINE_TIP_ONE',
                'E_D_SEATED_OVERHEAD_PRESS_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 313: Seated Overhead Press: Smith Machine
        ExerciseDefinition(
            id='exercise-313',
            title= "E_D_SEATED_OVERHEAD_PRESS_SMITH_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_overhead_press_smith_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_overhead_press_smith_machine.png'],
            preparation_steps=[
                'E_D_SEATED_OVERHEAD_PRESS_SMITH_MACHINE_PREP_ONE',
                'E_D_SEATED_OVERHEAD_PRESS_SMITH_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_OVERHEAD_PRESS_SMITH_MACHINE_EXEC_ONE',
                'E_D_SEATED_OVERHEAD_PRESS_SMITH_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_OVERHEAD_PRESS_SMITH_MACHINE_TIP_ONE',
                'E_D_SEATED_OVERHEAD_PRESS_SMITH_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.ARM],
            equipment=ExerciseEquipment.SMITH_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 314: Seated Rear Delt Row: Dumbbell
        ExerciseDefinition(
            id='exercise-314',
            title= "E_D_SEATED_REAR_DELT_ROW_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_rear_delt_row_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_rear_delt_row_dumbbell.png'],
            preparation_steps=[
                'E_D_SEATED_REAR_DELT_ROW_DUMBBELL_PREP_ONE',
                'E_D_SEATED_REAR_DELT_ROW_DUMBBELL_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_REAR_DELT_ROW_DUMBBELL_EXEC_ONE',
                'E_D_SEATED_REAR_DELT_ROW_DUMBBELL_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_REAR_DELT_ROW_DUMBBELL_TIP_ONE',
                'E_D_SEATED_REAR_DELT_ROW_DUMBBELL_TIP_TWO'
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.BACK],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 315: Seated Reverse Fly: Machine
        ExerciseDefinition(
            id='exercise-315',
            title= "E_D_SEATED_REVERSE_FLY_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_reverse_fly_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_reverse_fly_machine.png'],
            preparation_steps=[
                'E_D_SEATED_REVERSE_FLY_MACHINE_PREP_ONE',
                'E_D_SEATED_REVERSE_FLY_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_REVERSE_FLY_MACHINE_EXEC_ONE',
                'E_D_SEATED_REVERSE_FLY_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_REVERSE_FLY_MACHINE_TIP_ONE',
                'E_D_SEATED_REVERSE_FLY_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.BACK],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 316: Seated Row (Close Grip): Machine
        ExerciseDefinition(
            id='exercise-316',
            title= "E_D_SEATED_ROW_CLOSE_GRIP_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_row_close_grip_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_row_close_grip_machine.png'],
            preparation_steps=[
                'E_D_SEATED_ROW_CLOSE_GRIP_MACHINE_PREP_ONE',
                'E_D_SEATED_ROW_CLOSE_GRIP_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_ROW_CLOSE_GRIP_MACHINE_EXEC_ONE',
                'E_D_SEATED_ROW_CLOSE_GRIP_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_ROW_CLOSE_GRIP_MACHINE_TIP_ONE',
                'E_D_SEATED_ROW_CLOSE_GRIP_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 317: Seated Row (Wide Grip): Cable
        ExerciseDefinition(
            id='exercise-317',
            title= "E_D_SEATED_ROW_WIDE_GRIP_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_row_wide_grip_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_row_wide_grip_cable.png'],
            preparation_steps=[
                'E_D_SEATED_ROW_WIDE_GRIP_CABLE_PREP_ONE',
                'E_D_SEATED_ROW_WIDE_GRIP_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_ROW_WIDE_GRIP_CABLE_EXEC_ONE',
                'E_D_SEATED_ROW_WIDE_GRIP_CABLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_ROW_WIDE_GRIP_CABLE_TIP_ONE',
                'E_D_SEATED_ROW_WIDE_GRIP_CABLE_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 318: Seated Row: Cable
        ExerciseDefinition(
            id='exercise-318',
            title= "E_D_SEATED_ROW_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_row_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_row_cable.png'],
            preparation_steps=[
                'E_D_SEATED_ROW_CABLE_PREP_ONE',
                'E_D_SEATED_ROW_CABLE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_ROW_CABLE_EXEC_ONE',
                'E_D_SEATED_ROW_CABLE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_ROW_CABLE_TIP_ONE',
                'E_D_SEATED_ROW_CABLE_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 319: Seated Row: Machine
        ExerciseDefinition(
            id='exercise-319',
            title= "E_D_SEATED_ROW_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_row_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_row_machine.png'],
            preparation_steps=[
                'E_D_SEATED_ROW_MACHINE_PREP_ONE',
                'E_D_SEATED_ROW_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_ROW_MACHINE_EXEC_ONE',
                'E_D_SEATED_ROW_MACHINE_EXEC_TWO',
                'E_D_SEATED_ROW_MACHINE_EXEC_THREE'
            ],
            key_tips=[
                'E_D_SEATED_ROW_MACHINE_TIP_ONE',
                'E_D_SEATED_ROW_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ARM, FocusArea.SHOULDER],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 320: Seated Row With Twist: Band
        ExerciseDefinition(
            id='exercise-320',
            title= "E_D_SEATED_ROW_WITH_TWIST_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_row_with_twist_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_row_with_twist_band.png'],
            preparation_steps=[
                'E_D_SEATED_ROW_WITH_TWIST_BAND_PREP_ONE',
                'E_D_SEATED_ROW_WITH_TWIST_BAND_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_ROW_WITH_TWIST_BAND_EXEC_ONE',
                'E_D_SEATED_ROW_WITH_TWIST_BAND_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_ROW_WITH_TWIST_BAND_TIP_ONE',
                'E_D_SEATED_ROW_WITH_TWIST_BAND_TIP_TWO'
            ],
            focus_areas=[FocusArea.BACK, FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.BAND,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        # Exercise 321: Seated Torso Rotation: Machine
        ExerciseDefinition(
            id='exercise-321',
            title= "E_D_SEATED_TORSO_ROTATION_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/seated_torso_rotation_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/seated_torso_rotation_machine.png'],
            preparation_steps=[
                'E_D_SEATED_TORSO_ROTATION_MACHINE_PREP_ONE',
                'E_D_SEATED_TORSO_ROTATION_MACHINE_PREP_TWO'
            ],
            execution_steps=[
                'E_D_SEATED_TORSO_ROTATION_MACHINE_EXEC_ONE',
                'E_D_SEATED_TORSO_ROTATION_MACHINE_EXEC_TWO'
            ],
            key_tips=[
                'E_D_SEATED_TORSO_ROTATION_MACHINE_TIP_ONE',
                'E_D_SEATED_TORSO_ROTATION_MACHINE_TIP_TWO'
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.WEIGHT_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
ExerciseDefinition(
            id='exercise-322',
            title= "E_D_SHRUG_TITLE",
            video_urls=['regular_directory/exercises/videos/shrug.mp4'],
            cover_image_url=['regular_directory/exercises/images/shrug.png'],
            preparation_steps=[
                'E_D_SHRUG_PREP_ONE',
            ],
            execution_steps=[
                'E_D_SHRUG_EXEC_ONE',
                'E_D_SHRUG_EXEC_TWO',
                'E_D_SHRUG_EXEC_THREE',
            ],
            key_tips=[
                'E_D_SHRUG_TIP_ONE',
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.BACK],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-323',
            title= "E_D_SHRUG_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/shrug_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/shrug_barbell.png'],
            preparation_steps=[
                'E_D_SHRUG_BARBELL_PREP_ONE',
                'E_D_SHRUG_BARBELL_PREP_TWO',
            ],
            execution_steps=[
                'E_D_SHRUG_BARBELL_EXEC_ONE',
                'E_D_SHRUG_BARBELL_EXEC_TWO',
                'E_D_SHRUG_BARBELL_EXEC_THREE',
            ],
            key_tips=[
                'E_D_SHRUG_BARBELL_TIP_ONE',
                'E_D_SHRUG_BARBELL_TIP_TWO',
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.BACK],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-324',
            title= "E_D_SHRUG_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/shrug_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/shrug_cable.png'],
            preparation_steps=[
                'E_D_SHRUG_CABLE_PREP_ONE',
                'E_D_SHRUG_CABLE_PREP_TWO',
            ],
            execution_steps=[
                'E_D_SHRUG_CABLE_EXEC_ONE',
                'E_D_SHRUG_CABLE_EXEC_TWO',
                'E_D_SHRUG_CABLE_EXEC_THREE',
            ],
            key_tips=[
                'E_D_SHRUG_CABLE_TIP_ONE',
                'E_D_SHRUG_CABLE_TIP_TWO',
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.BACK],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-325',
            title= "E_D_SHRUG_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/shrug_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/shrug_dumbbell.png'],
            preparation_steps=[
                'E_D_SHRUG_DUMBBELL_PREP_ONE',
                'E_D_SHRUG_DUMBBELL_PREP_TWO',
            ],
            execution_steps=[
                'E_D_SHRUG_DUMBBELL_EXEC_ONE',
                'E_D_SHRUG_DUMBBELL_EXEC_TWO',
                'E_D_SHRUG_DUMBBELL_EXEC_THREE',
            ],
            key_tips=[
                'E_D_SHRUG_DUMBBELL_TIP_ONE',
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.BACK],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-326',
            title= "E_D_SHRUG_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/shrug_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/shrug_machine.png'],
            preparation_steps=[
                'E_D_SHRUG_MACHINE_PREP_ONE',
                'E_D_SHRUG_MACHINE_PREP_TWO',
            ],
            execution_steps=[
                'E_D_SHRUG_MACHINE_EXEC_ONE',
                'E_D_SHRUG_MACHINE_EXEC_TWO',
                'E_D_SHRUG_MACHINE_EXEC_THREE',
            ],
            key_tips=[
                'E_D_SHRUG_MACHINE_TIP_ONE',
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.BACK],
            equipment=ExerciseEquipment.WEIGHT_MACHINE, # Mapped from 'Lever Shrug Machine'
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-327',
            title= "E_D_SHRUG_SMITH_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/shrug_smith_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/shrug_smith_machine.png'],
            preparation_steps=[
                'E_D_SHRUG_SMITH_MACHINE_PREP_ONE',
                'E_D_SHRUG_SMITH_MACHINE_PREP_TWO',
            ],
            execution_steps=[
                'E_D_SHRUG_SMITH_MACHINE_EXEC_ONE',
                'E_D_SHRUG_SMITH_MACHINE_EXEC_TWO',
                'E_D_SHRUG_SMITH_MACHINE_EXEC_THREE',
            ],
            key_tips=[
                'E_D_SHRUG_SMITH_MACHINE_TIP_ONE',
                'E_D_SHRUG_SMITH_MACHINE_TIP_TWO',
            ],
            focus_areas=[FocusArea.SHOULDER, FocusArea.BACK],
            equipment=ExerciseEquipment.SMITH_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-328',
            title= "E_D_SIDE_BRIDGE_TITLE",
            video_urls=['regular_directory/exercises/videos/side_bridge.mp4'],
            cover_image_url=['regular_directory/exercises/images/side_bridge.png'],
            preparation_steps=[
                'E_D_SIDE_BRIDGE_PREP_ONE',
                'E_D_SIDE_BRIDGE_PREP_TWO',
            ],
            execution_steps=[
                'E_D_SIDE_BRIDGE_EXEC_ONE',
                'E_D_SIDE_BRIDGE_EXEC_TWO',
                'E_D_SIDE_BRIDGE_EXEC_THREE',
            ],
            key_tips=[
                'E_D_SIDE_BRIDGE_TIP_ONE',
                'E_D_SIDE_BRIDGE_TIP_TWO',
                'E_D_SIDE_BRIDGE_TIP_THREE',
            ],
            focus_areas=[FocusArea.ABDOMEN],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
        ExerciseDefinition(
            id='exercise-329',
            title= "E_D_SIDE_LUNGE_TITLE",
            video_urls=['regular_directory/exercises/videos/side_lunge.mp4'],
            cover_image_url=['regular_directory/exercises/images/side_lunge.png'],
            preparation_steps=[
                'E_D_SIDE_LUNGE_PREP_ONE',
                'E_D_SIDE_LUNGE_PREP_TWO',
            ],
            execution_steps=[
                'E_D_SIDE_LUNGE_EXEC_ONE',
                'E_D_SIDE_LUNGE_EXEC_TWO',
                'E_D_SIDE_LUNGE_EXEC_THREE',
                'E_D_SIDE_LUNGE_EXEC_FOUR',
            ],
            key_tips=[
                'E_D_SIDE_LUNGE_TIP_ONE',
                'E_D_SIDE_LUNGE_TIP_TWO',
                'E_D_SIDE_LUNGE_TIP_THREE',
            ],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
ExerciseDefinition(
            id='exercise-322',
            title= "E_D_SHRUG_TITLE",
            video_urls=['regular_directory/exercises/videos/shrug.mp4'],
            cover_image_url=['regular_directory/exercises/images/shrug.png'],
                preparation_steps=['E_D_SHRUG_PREP_ONE'],
                execution_steps=['E_D_SHRUG_EXEC_ONE', 'E_D_SHRUG_EXEC_TWO', 'E_D_SHRUG_EXEC_THREE'],
                key_tips=['E_D_SHRUG_TIP_ONE'],
            focus_areas=[FocusArea('shoulder'), FocusArea('back')],
            equipment=ExerciseEquipment('body_weight'),
            metric_type=ExerciseMetricType('reps_only')
        ),
        ExerciseDefinition(
            id='exercise-323',
            title= "E_D_SHRUG_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/shrug_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/shrug_barbell.png'],
                preparation_steps=['E_D_SHRUG_BARBELL_PREP_ONE', 'E_D_SHRUG_BARBELL_PREP_TWO'],
                execution_steps=['E_D_SHRUG_BARBELL_EXEC_ONE', 'E_D_SHRUG_BARBELL_EXEC_TWO', 'E_D_SHRUG_BARBELL_EXEC_THREE'],
                key_tips=['E_D_SHRUG_BARBELL_TIP_ONE', 'E_D_SHRUG_BARBELL_TIP_TWO'],
            focus_areas=[FocusArea('shoulder'), FocusArea('back')],
            equipment=ExerciseEquipment('barbell'),
            metric_type=ExerciseMetricType('reps_only')
        ),
        ExerciseDefinition(
            id='exercise-324',
            title= "E_D_SHRUG_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/shrug_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/shrug_cable.png'],
                preparation_steps=['E_D_SHRUG_CABLE_PREP_ONE', 'E_D_SHRUG_CABLE_PREP_TWO'],
                execution_steps=['E_D_SHRUG_CABLE_EXEC_ONE', 'E_D_SHRUG_CABLE_EXEC_TWO', 'E_D_SHRUG_CABLE_EXEC_THREE'],
                key_tips=['E_D_SHRUG_CABLE_TIP_ONE', 'E_D_SHRUG_CABLE_TIP_TWO'],
            focus_areas=[FocusArea('shoulder'), FocusArea('back')],
            equipment=ExerciseEquipment('cable_machine'),
            metric_type=ExerciseMetricType('reps_only')
        ),
        ExerciseDefinition(
            id='exercise-325',
            title= "E_D_SHRUG_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/shrug_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/shrug_dumbbell.png'],
                preparation_steps=['E_D_SHRUG_DUMBBELL_PREP_ONE', 'E_D_SHRUG_DUMBBELL_PREP_TWO'],
                execution_steps=['E_D_SHRUG_DUMBBELL_EXEC_ONE', 'E_D_SHRUG_DUMBBELL_EXEC_TWO', 'E_D_SHRUG_DUMBBELL_EXEC_THREE'],
                key_tips=['E_D_SHRUG_DUMBBELL_TIP_ONE'],
            focus_areas=[FocusArea('shoulder'), FocusArea('back')],
            equipment=ExerciseEquipment('dumbbell'),
            metric_type=ExerciseMetricType('reps_only')
        ),
        ExerciseDefinition(
            id='exercise-326',
            title= "E_D_SHRUG_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/shrug_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/shrug_machine.png'],
                preparation_steps=['E_D_SHRUG_MACHINE_PREP_ONE', 'E_D_SHRUG_MACHINE_PREP_TWO'],
                execution_steps=['E_D_SHRUG_MACHINE_EXEC_ONE', 'E_D_SHRUG_MACHINE_EXEC_TWO', 'E_D_SHRUG_MACHINE_EXEC_THREE'],
                key_tips=['E_D_SHRUG_MACHINE_TIP_ONE'],
            focus_areas=[FocusArea('shoulder'), FocusArea('back')],
            equipment=ExerciseEquipment('weight_machine'),
            metric_type=ExerciseMetricType('reps_only')
        ),
        ExerciseDefinition(
            id='exercise-327',
            title= "E_D_SHRUG_SMITH_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/shrug_smith_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/shrug_smith_machine.png'],
                preparation_steps=['E_D_SHRUG_SMITH_MACHINE_PREP_ONE', 'E_D_SHRUG_SMITH_MACHINE_PREP_TWO'],
                execution_steps=['E_D_SHRUG_SMITH_MACHINE_EXEC_ONE', 'E_D_SHRUG_SMITH_MACHINE_EXEC_TWO', 'E_D_SHRUG_SMITH_MACHINE_EXEC_THREE'],
                key_tips=['E_D_SHRUG_SMITH_MACHINE_TIP_ONE', 'E_D_SHRUG_SMITH_MACHINE_TIP_TWO'],
            focus_areas=[FocusArea('shoulder'), FocusArea('back')],
            equipment=ExerciseEquipment('smith_machine'),
            metric_type=ExerciseMetricType('reps_only')
        ),
        ExerciseDefinition(
            id='exercise-328',
            title= "E_D_SIDE_BRIDGE_TITLE",
            video_urls=['regular_directory/exercises/videos/side_bridge.mp4'],
            cover_image_url=['regular_directory/exercises/images/side_bridge.png'],
                preparation_steps=['E_D_SIDE_BRIDGE_PREP_ONE', 'E_D_SIDE_BRIDGE_PREP_TWO'],
                execution_steps=['E_D_SIDE_BRIDGE_EXEC_ONE', 'E_D_SIDE_BRIDGE_EXEC_TWO', 'E_D_SIDE_BRIDGE_EXEC_THREE'],
                key_tips=['E_D_SIDE_BRIDGE_TIP_ONE', 'E_D_SIDE_BRIDGE_TIP_TWO', 'E_D_SIDE_BRIDGE_TIP_THREE'],
            focus_areas=[FocusArea('abdomen')],
            equipment=ExerciseEquipment('body_weight'),
            metric_type=ExerciseMetricType('time_based')
        ),
        ExerciseDefinition(
            id='exercise-329',
            title= "E_D_SIDE_LUNGE_TITLE",
            video_urls=['regular_directory/exercises/videos/side_lunge.mp4'],
            cover_image_url=['regular_directory/exercises/images/side_lunge.png'],
                preparation_steps=['E_D_SIDE_LUNGE_PREP_ONE', 'E_D_SIDE_LUNGE_PREP_TWO'],
                execution_steps=['E_D_SIDE_LUNGE_EXEC_ONE', 'E_D_SIDE_LUNGE_EXEC_TWO', 'E_D_SIDE_LUNGE_EXEC_THREE', 'E_D_SIDE_LUNGE_EXEC_FOUR'],
                key_tips=['E_D_SIDE_LUNGE_TIP_ONE', 'E_D_SIDE_LUNGE_TIP_TWO', 'E_D_SIDE_LUNGE_TIP_THREE'],
            focus_areas=[FocusArea('buttocks'), FocusArea('leg')],
            equipment=ExerciseEquipment('body_weight'),
            metric_type=ExerciseMetricType('reps_only')
        ),

        # Exercises 330-391 (Current response)
        ExerciseDefinition(
            id='exercise-330',
            title= "E_D_SIDE_LUNGE_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/side_lunge_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/side_lunge_barbell.png'],
                preparation_steps=['E_D_SIDE_LUNGE_BARBELL_PREP_ONE', 'E_D_SIDE_LUNGE_BARBELL_PREP_TWO', 'E_D_SIDE_LUNGE_BARBELL_PREP_THREE'],
                execution_steps=['E_D_SIDE_LUNGE_BARBELL_EXEC_ONE', 'E_D_SIDE_LUNGE_BARBELL_EXEC_TWO', 'E_D_SIDE_LUNGE_BARBELL_EXEC_THREE'],
                key_tips=['E_D_SIDE_LUNGE_BARBELL_TIP_ONE', 'E_D_SIDE_LUNGE_BARBELL_TIP_TWO'],
            focus_areas=[FocusArea('buttocks'), FocusArea('leg')],
            equipment=ExerciseEquipment('barbell'),
            metric_type=ExerciseMetricType('reps_only')
        ),
        ExerciseDefinition(
            id='exercise-331',
            title= "E_D_SIDE_LUNGE_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/side_lunge_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/side_lunge_dumbbell.png'],
                preparation_steps=['E_D_SIDE_LUNGE_DUMBBELL_PREP_ONE', 'E_D_SIDE_LUNGE_DUMBBELL_PREP_TWO', 'E_D_SIDE_LUNGE_DUMBBELL_PREP_THREE'],
                execution_steps=['E_D_SIDE_LUNGE_DUMBBELL_EXEC_ONE', 'E_D_SIDE_LUNGE_DUMBBELL_EXEC_TWO', 'E_D_SIDE_LUNGE_DUMBBELL_EXEC_THREE'],
                key_tips=['E_D_SIDE_LUNGE_DUMBBELL_TIP_ONE', 'E_D_SIDE_LUNGE_DUMBBELL_TIP_TWO'],
            focus_areas=[FocusArea('buttocks'), FocusArea('leg')],
            equipment=ExerciseEquipment('dumbbell'),
            metric_type=ExerciseMetricType('reps_only')
        ),
        ExerciseDefinition(
            id='exercise-332',
            title= "E_D_SIDE_LUNGE_KETTLEBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/side_lunge_kettlebell.mp4'],
            cover_image_url=['regular_directory/exercises/images/side_lunge_kettlebell.png'],
                preparation_steps=['E_D_SIDE_LUNGE_KETTLEBELL_PREP_ONE', 'E_D_SIDE_LUNGE_KETTLEBELL_PREP_TWO', 'E_D_SIDE_LUNGE_KETTLEBELL_PREP_THREE'],
                execution_steps=['E_D_SIDE_LUNGE_KETTLEBELL_EXEC_ONE', 'E_D_SIDE_LUNGE_KETTLEBELL_EXEC_TWO', 'E_D_SIDE_LUNGE_KETTLEBELL_EXEC_THREE'],
                key_tips=['E_D_SIDE_LUNGE_KETTLEBELL_TIP_ONE', 'E_D_SIDE_LUNGE_KETTLEBELL_TIP_TWO'],
            focus_areas=[FocusArea('buttocks'), FocusArea('leg')],
            equipment=ExerciseEquipment('kettlebell'),
            metric_type=ExerciseMetricType('reps_only')
        ),
        ExerciseDefinition(
            id='exercise-334',
            title= "E_D_SIDE_PLANK_TITLE",
            video_urls=['regular_directory/exercises/videos/side_plank.mp4'],
            cover_image_url=['regular_directory/exercises/images/side_plank.png'],
                preparation_steps=['E_D_SIDE_PLANK_PREP_ONE', 'E_D_SIDE_PLANK_PREP_TWO'],
                execution_steps=['E_D_SIDE_PLANK_EXEC_ONE', 'E_D_SIDE_PLANK_EXEC_TWO', 'E_D_SIDE_PLANK_EXEC_THREE'],
                key_tips=['E_D_SIDE_PLANK_TIP_ONE', 'E_D_SIDE_PLANK_TIP_TWO', 'E_D_SIDE_PLANK_TIP_THREE'],
            focus_areas=[FocusArea('abdomen')],
            equipment=ExerciseEquipment('body_weight'),
            metric_type=ExerciseMetricType('time_based')
        ),
        
        
        
        
        
        ExerciseDefinition(
            id='exercise-359',
            title= "E_D_SIT_UP_BODYWEIGHT_TITLE",
            video_urls=['regular_directory/exercises/videos/sit_up.mp4'],
            cover_image_url=['regular_directory/exercises/images/sit_up.png'],
                preparation_steps=['E_D_SIT_UP_BODYWEIGHT_PREP_ONE', 'E_D_SIT_UP_BODYWEIGHT_PREP_TWO', 'E_D_SIT_UP_BODYWEIGHT_PREP_THREE'],
                execution_steps=['E_D_SIT_UP_BODYWEIGHT_EXEC_ONE', 'E_D_SIT_UP_BODYWEIGHT_EXEC_TWO', 'E_D_SIT_UP_BODYWEIGHT_EXEC_THREE'],
                key_tips=['E_D_SIT_UP_BODYWEIGHT_TIP_ONE', 'E_D_SIT_UP_BODYWEIGHT_TIP_TWO'],
            focus_areas=[FocusArea('abdomen')],
            equipment=ExerciseEquipment('body_weight'),
            metric_type=ExerciseMetricType('reps_only')
        ),
        
        ExerciseDefinition(
            id='exercise-361',
            title= "E_D_SIT_UP_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/sit_up_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/sit_up_dumbbell.png'],
                preparation_steps=['E_D_SIT_UP_DUMBBELL_PREP_ONE', 'E_D_SIT_UP_DUMBBELL_PREP_TWO', 'E_D_SIT_UP_DUMBBELL_PREP_THREE'],
                execution_steps=['E_D_SIT_UP_DUMBBELL_EXEC_ONE', 'E_D_SIT_UP_DUMBBELL_EXEC_TWO', 'E_D_SIT_UP_DUMBBELL_EXEC_THREE'],
                key_tips=['E_D_SIT_UP_DUMBBELL_TIP_ONE', 'E_D_SIT_UP_DUMBBELL_TIP_TWO'],
            focus_areas=[FocusArea('abdomen')],
            equipment=ExerciseEquipment('dumbbell'),
            metric_type=ExerciseMetricType('reps_only')
        ),
        
        
        
        
        ExerciseDefinition(
            id='exercise-366',
            title= "E_D_SIT_UP_KETTLEBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/sit_up_kettlebell.mp4'],
            cover_image_url=['regular_directory/exercises/images/sit_up_kettlebell.png'],
                preparation_steps=['E_D_SIT_UP_KETTLEBELL_PREP_ONE', 'E_D_SIT_UP_KETTLEBELL_PREP_TWO', 'E_D_SIT_UP_KETTLEBELL_PREP_THREE'],
                execution_steps=['E_D_SIT_UP_KETTLEBELL_EXEC_ONE', 'E_D_SIT_UP_KETTLEBELL_EXEC_TWO', 'E_D_SIT_UP_KETTLEBELL_EXEC_THREE'],
                key_tips=['E_D_SIT_UP_KETTLEBELL_TIP_ONE', 'E_D_SIT_UP_KETTLEBELL_TIP_TWO'],
            focus_areas=[FocusArea('abdomen')],
            equipment=ExerciseEquipment('kettlebell'),
            metric_type=ExerciseMetricType('reps_only')
        ),
        
        
        
        
        
        
        
        
        
        
        
        ExerciseDefinition(
            id='exercise-385',
            title= "E_D_SKULL_CRUSHER_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/skull_crusher_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/skull_crusher_dumbbell.png'],
                preparation_steps=['E_D_SKULL_CRUSHER_DUMBBELL_PREP_ONE', 'E_D_SKULL_CRUSHER_DUMBBELL_PREP_TWO', 'E_D_SKULL_CRUSHER_DUMBBELL_PREP_THREE'],
                execution_steps=['E_D_SKULL_CRUSHER_DUMBBELL_EXEC_ONE', 'E_D_SKULL_CRUSHER_DUMBBELL_EXEC_TWO', 'E_D_SKULL_CRUSHER_DUMBBELL_EXEC_THREE'],
                key_tips=['E_D_SKULL_CRUSHER_DUMBBELL_TIP_ONE', 'E_D_SKULL_CRUSHER_DUMBBELL_TIP_TWO'],
            focus_areas=[FocusArea('arm')],
            equipment=ExerciseEquipment('dumbbell'),
            metric_type=ExerciseMetricType('reps_only')
        ),
        
        ExerciseDefinition(
            id='exercise-387',
            title= "E_D_SKULL_CRUSHER_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/skull_crusher_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/skull_crusher_barbell.png'],
                preparation_steps=['E_D_SKULL_CRUSHER_BARBELL_PREP_ONE', 'E_D_SKULL_CRUSHER_BARBELL_PREP_TWO', 'E_D_SKULL_CRUSHER_BARBELL_PREP_THREE'],
                execution_steps=['E_D_SKULL_CRUSHER_BARBELL_EXEC_ONE', 'E_D_SKULL_CRUSHER_BARBELL_EXEC_TWO', 'E_D_SKULL_CRUSHER_BARBELL_EXEC_THREE'],
                key_tips=['E_D_SKULL_CRUSHER_BARBELL_TIP_ONE', 'E_D_SKULL_CRUSHER_BARBELL_TIP_TWO'],
            focus_areas=[FocusArea('arm')],
            equipment=ExerciseEquipment('barbell'),
            metric_type=ExerciseMetricType('reps_only')
        ),
        
        
        ExerciseDefinition(
            id='exercise-390',
            title= "E_D_STRAIGHT_ARM_PLANK_TITLE",
            video_urls=['regular_directory/exercises/videos/straight_arm_plank.mp4'],
            cover_image_url=['regular_directory/exercises/images/straight_arm_plank.png'],
                preparation_steps=['E_D_STRAIGHT_ARM_PLANK_PREP_ONE', 'E_D_STRAIGHT_ARM_PLANK_PREP_TWO'],
                execution_steps=['E_D_STRAIGHT_ARM_PLANK_EXEC_ONE', 'E_D_STRAIGHT_ARM_PLANK_EXEC_TWO', 'E_D_STRAIGHT_ARM_PLANK_EXEC_THREE'],
                key_tips=['E_D_STRAIGHT_ARM_PLANK_TIP_ONE', 'E_D_STRAIGHT_ARM_PLANK_TIP_TWO', 'E_D_STRAIGHT_ARM_PLANK_TIP_THREE'],
            focus_areas=[FocusArea('abdomen')],
            equipment=ExerciseEquipment('body_weight'),
            metric_type=ExerciseMetricType('time_based')
        ),
        ExerciseDefinition(
            id='exercise-391',
            title= "E_D_STANDING_SIDE_CRUNCH_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/standing_side_crunch_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/standing_side_crunch_cable.png'],
                preparation_steps=['E_D_STANDING_SIDE_CRUNCH_CABLE_PREP_ONE', 'E_D_STANDING_SIDE_CRUNCH_CABLE_PREP_TWO'],
                execution_steps=['E_D_STANDING_SIDE_CRUNCH_CABLE_EXEC_ONE', 'E_D_STANDING_SIDE_CRUNCH_CABLE_EXEC_TWO', 'E_D_STANDING_SIDE_CRUNCH_CABLE_EXEC_THREE'],
                key_tips=['E_D_STANDING_SIDE_CRUNCH_CABLE_TIP_ONE', 'E_D_STANDING_SIDE_CRUNCH_CABLE_TIP_TWO'],
            focus_areas=[FocusArea('abdomen')],
            equipment=ExerciseEquipment('cable_machine'),
            metric_type=ExerciseMetricType('reps_only')
        ),
ExerciseDefinition(
            id='exercise-392',
            title= "E_D_STANDING_GLUTE_KICKBACK_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/standing_glute_kickback_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/standing_glute_kickback_cable.png'],
                preparation_steps=[],
                execution_steps=['E_D_STANDING_GLUTE_KICKBACK_EXEC_ONE', 'E_D_STANDING_GLUTE_KICKBACK_EXEC_TWO', 'E_D_STANDING_GLUTE_KICKBACK_EXEC_THREE'],
                key_tips=['E_D_STANDING_GLUTE_KICKBACK_TIP_ONE', 'E_D_STANDING_GLUTE_KICKBACK_TIP_TWO'],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
    ExerciseDefinition(
            id='exercise-393',
            title= "E_D_STANDING_GLUTE_KICKBACK_MACHINE_TITLE",
            video_urls=['regular_directory/exercises/videos/standing_glute_kickback_machine.mp4'],
            cover_image_url=['regular_directory/exercises/images/standing_glute_kickback_machine.png'],
                preparation_steps=[],
                execution_steps=[],
                key_tips=[],
            focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
    ExerciseDefinition(
            id='exercise-394',
            title= "E_D_STANDING_INCLINE_FLY_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/standing_incline_fly_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/standing_incline_fly_band.png'],
                preparation_steps=[],
                execution_steps=[],
                key_tips=[],
            focus_areas=[FocusArea.ARM, FocusArea.SHOULDER, FocusArea.CHEST],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
    
    ExerciseDefinition(
            id='exercise-396',
            title= "E_D_STANDING_INCLINE_FLY_DUMBBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/standing_incline_fly_dumbbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/standing_incline_fly_dumbbell.png'],
                preparation_steps=[],
                execution_steps=[],
                key_tips=[],
            focus_areas=[FocusArea.ARM, FocusArea.SHOULDER, FocusArea.CHEST],
            equipment=ExerciseEquipment.DUMBBELL,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
    ExerciseDefinition(
            id='exercise-397',
            title= "E_D_STANDING_INCLINE_PRESS_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/standing_incline_press_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/standing_incline_press_band.png'],
                preparation_steps=[],
                execution_steps=[],
                key_tips=[],
            focus_areas=[FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
    ExerciseDefinition(
            id='exercise-398',
            title= "E_D_STANDING_LEG_EXTENSION_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/standing_leg_extension_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/standing_leg_extension_band.png'],
                preparation_steps=['E_D_STANDING_LEG_EXTENSION_BAND_PREP_ONE', 'E_D_STANDING_LEG_EXTENSION_BAND_PREP_TWO'],
                execution_steps=['E_D_STANDING_LEG_EXTENSION_BAND_EXEC_ONE', 'E_D_STANDING_LEG_EXTENSION_BAND_EXEC_TWO', 'E_D_STANDING_LEG_EXTENSION_BAND_EXEC_THREE'],
                key_tips=['E_D_STANDING_LEG_EXTENSION_BAND_TIP_ONE'],
            focus_areas=[FocusArea.LEG],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
    ExerciseDefinition(
            id='exercise-399',
            title= "E_D_STANDING_REAR_DELT_ROW_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/standing_rear_delt_row_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/standing_rear_delt_row_band.png'],
                preparation_steps=['E_D_STANDING_REAR_DELT_ROW_BAND_PREP_ONE', 'E_D_STANDING_REAR_DELT_ROW_BAND_PREP_TWO'],
                execution_steps=['E_D_STANDING_REAR_DELT_ROW_BAND_EXEC_ONE', 'E_D_STANDING_REAR_DELT_ROW_BAND_EXEC_TWO', 'E_D_STANDING_REAR_DELT_ROW_BAND_EXEC_THREE'],
                key_tips=['E_D_STANDING_REAR_DELT_ROW_BAND_TIP_ONE'],
            focus_areas=[FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
    ExerciseDefinition(
            id='exercise-400',
            title= "E_D_STANDING_REAR_DELT_ROW_CABLE_TITLE",
            video_urls=['regular_directory/exercises/videos/standing_rear_delt_row_cable.mp4'],
            cover_image_url=['regular_directory/exercises/images/standing_rear_delt_row_cable.png'],
                preparation_steps=['E_D_STANDING_REAR_DELT_ROW_CABLE_PREP_ONE', 'E_D_STANDING_REAR_DELT_ROW_CABLE_PREP_TWO'],
                execution_steps=['E_D_STANDING_REAR_DELT_ROW_CABLE_EXEC_ONE', 'E_D_STANDING_REAR_DELT_ROW_CABLE_EXEC_TWO', 'E_D_STANDING_REAR_DELT_ROW_CABLE_EXEC_THREE'],
                key_tips=['E_D_STANDING_REAR_DELT_ROW_CABLE_TIP_ONE', 'E_D_STANDING_REAR_DELT_ROW_CABLE_TIP_TWO'],
            focus_areas=[FocusArea.SHOULDER],
            equipment=ExerciseEquipment.CABLE_MACHINE,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
    ExerciseDefinition(
            id='exercise-401',
            title= "E_D_STANDING_REVERSE_FLY_BAND_TITLE",
            video_urls=['regular_directory/exercises/videos/standing_reverse_fly_band.mp4'],
            cover_image_url=['regular_directory/exercises/images/standing_reverse_fly_band.png'],
                preparation_steps=['E_D_STANDING_REVERSE_FLY_BAND_PREP_ONE'],
                execution_steps=['E_D_STANDING_REVERSE_FLY_BAND_EXEC_ONE', 'E_D_STANDING_REVERSE_FLY_BAND_EXEC_TWO', 'E_D_STANDING_REVERSE_FLY_BAND_EXEC_THREE'],
                key_tips=['E_D_STANDING_REVERSE_FLY_BAND_TIP_ONE', 'E_D_STANDING_REVERSE_FLY_BAND_TIP_TWO'],
            focus_areas=[FocusArea.SHOULDER],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
    ExerciseDefinition(
            id='exercise-402',
            title= "E_D_WRIST_ROLLER_PLATE_TITLE",
            video_urls=['regular_directory/exercises/videos/wrist_roller_plate.mp4'],
            cover_image_url=['regular_directory/exercises/images/wrist_roller_plate.png'],
                preparation_steps=['E_D_WRIST_ROLLER_PLATE_PREP_ONE', 'E_D_WRIST_ROLLER_PLATE_PREP_TWO'],
                execution_steps=['E_D_WRIST_ROLLER_PLATE_EXEC_ONE', 'E_D_WRIST_ROLLER_PLATE_EXEC_TWO'],
                key_tips=['E_D_WRIST_ROLLER_PLATE_TIP_ONE', 'E_D_WRIST_ROLLER_PLATE_TIP_TWO', 'E_D_WRIST_ROLLER_PLATE_TIP_THREE'],
            focus_areas=[FocusArea.ARM],
            equipment=ExerciseEquipment.BODY_WEIGHT,
            metric_type=ExerciseMetricType.REPS_ONLY
        ),
    ExerciseDefinition(
            id='exercise-403',
            title= "E_D_ZERCHER_CARRY_BARBELL_TITLE",
            video_urls=['regular_directory/exercises/videos/zercher_carry_barbell.mp4'],
            cover_image_url=['regular_directory/exercises/images/zercher_carry_barbell.png'],
                preparation_steps=['E_D_ZERCHER_CARRY_BARBELL_PREP_ONE'],
                execution_steps=['E_D_ZERCHER_CARRY_BARBELL_EXEC_ONE'],
                key_tips=['E_D_ZERCHER_CARRY_BARBELL_TIP_ONE'],
            focus_areas=[FocusArea.FULL_BODY],
            equipment=ExerciseEquipment.BARBELL,
            metric_type=ExerciseMetricType.TIME_BASED
        ),
    
        

#         ExerciseDefinition(
#             id='exercise-2',
#             title= "E_D_ALTERNATING_PUNCH_TITLE",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/alternating_punch.png'],
#                 preparation_steps=[
#                     'E_D_ALTERNATING_PUNCH_PREP_ONE',
#                     'E_D_ALTERNATING_PUNCH_PREP_TWO',
#                     'E_D_ALTERNATING_PUNCH_PREP_THREE'
#                 ],
#                 execution_steps=[
#                     'E_D_ALTERNATING_PUNCH_EXEC_ONE',
#                     'E_D_ALTERNATING_PUNCH_EXEC_TWO',
#                     'E_D_ALTERNATING_PUNCH_EXEC_THREE'
#                 ],
#                 key_tips=[
#                     'E_D_ALTERNATING_PUNCH_TIP_ONE',
#                     'E_D_ALTERNATING_PUNCH_TIP_TWO',
#                     'E_D_ALTERNATING_PUNCH_TIP_THREE'
#                 ],
#             focus_areas=[FocusArea.SHOULDER, FocusArea.ARM, FocusArea.CHEST],
#             equipment=ExerciseEquipment.BODY_WEIGHT,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-3',
#             title= "E_D_ALTERNATING_V_UP_BAND_TITLE",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/alternating_v_up_band.png'],
#                 preparation_steps=[
#                     'E_D_ALTERNATING_V_UP_BAND_PREP_ONE',
#                     'E_D_ALTERNATING_V_UP_BAND_PREP_TWO'
#                 ],
#                 execution_steps=[
#                     'E_D_ALTERNATING_V_UP_BAND_EXEC_ONE',
#                     'E_D_ALTERNATING_V_UP_BAND_EXEC_TWO'
#                 ],
#                 key_tips=[
#                     'E_D_ALTERNATING_V_UP_BAND_TIP_ONE'
#                 ],
#             focus_areas=[FocusArea.ABDOMEN, FocusArea.LEG],
#             equipment=ExerciseEquipment.BAND,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-4',
#             title= "E_D_ARM_CIRCLES_TITLE",
#             video_urls=['regular_directory/exercises/videos/arm_circles.mp4'],
#             cover_image_url=['regular_directory/exercises/images/arm_circles.png'],
#                 preparation_steps=[
#                     'E_D_ARM_CIRCLES_PREP_ONE',
#                     'E_D_ARM_CIRCLES_PREP_TWO'
#                 ],
#                 execution_steps=[
#                     'E_D_ARM_CIRCLES_EXEC_ONE',
#                     'E_D_ARM_CIRCLES_EXEC_TWO',
#                     'E_D_ARM_CIRCLES_EXEC_THREE'
#                 ],
#                 key_tips=[
#                     'E_D_ARM_CIRCLES_TIP_ONE',
#                     'E_D_ARM_CIRCLES_TIP_TWO'
#                 ],
#             focus_areas=[FocusArea.SHOULDER],
#             equipment=ExerciseEquipment.BODY_WEIGHT,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-5',
#             title= "E_D_ARNOLD_DUMBBELL_TITLE",
#             video_urls=['regular_directory/exercises/videos/arnold_dumbbell.mp4'],
#             cover_image_url=['regular_directory/exercises/images/arnold_dumbbell.png'],
#                 preparation_steps=[
#                     'E_D_ARNOLD_DUMBBELL_PREP_ONE',
#                     'E_D_ARNOLD_DUMBBELL_PREP_TWO'
#                 ],
#                 execution_steps=[
#                     'E_D_ARNOLD_DUMBBELL_EXEC_ONE',
#                     'E_D_ARNOLD_DUMBBELL_EXEC_TWO'
#                 ],
#                 key_tips=[
#                     'E_D_ARNOLD_DUMBBELL_TIP_ONE',
#                     'E_D_ARNOLD_DUMBBELL_TIP_TWO',
#                     'E_D_ARNOLD_DUMBBELL_TIP_THREE'
#                 ],
#             focus_areas=[FocusArea.SHOULDER, FocusArea.ARM],
#             equipment=ExerciseEquipment.DUMBBELL,
#             metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
#         ),
#         ExerciseDefinition(
#             id='exercise-6',
#             title= "E_D_BACK_EXTENSION_TITLE",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/back_extension.png'],
#                 preparation_steps=[
#                     'E_D_BACK_EXTENSION_PREP_ONE',
#                     'E_D_BACK_EXTENSION_PREP_TWO'
#                 ],
#                 execution_steps=[
#                     'E_D_BACK_EXTENSION_EXEC_ONE',
#                     'E_D_BACK_EXTENSION_EXEC_TWO'
#                 ],
#                 key_tips=[
#                     'E_D_BACK_EXTENSION_TIP_ONE',
#                     'E_D_BACK_EXTENSION_TIP_TWO'
#                 ],
#             focus_areas=[FocusArea.BACK, FocusArea.BUTTOCKS, FocusArea.LEG],
#             equipment=ExerciseEquipment.BODY_WEIGHT,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-7',
#             title= "E_D_BACK_EXTENSION_ON_FLOOR_TITLE",
#             video_urls=['regular_directory/exercises/videos/back_extension_on_floor.mp4'],
#             cover_image_url=['regular_directory/exercises/images/back_extension_on_floor.png'],
#                 preparation_steps=[
#                     'E_D_BACK_EXTENSION_ON_FLOOR_PREP_ONE'
#                 ],
#                 execution_steps=[
#                     'E_D_BACK_EXTENSION_ON_FLOOR_EXEC_ONE',
#                     'E_D_BACK_EXTENSION_ON_FLOOR_EXEC_TWO'
#                 ],
#                 key_tips=[
#                     'E_D_BACK_EXTENSION_ON_FLOOR_TIP_ONE',
#                     'E_D_BACK_EXTENSION_ON_FLOOR_TIP_TWO'
#                 ],
#             focus_areas=[FocusArea.BACK],
#             equipment=ExerciseEquipment.BODY_WEIGHT,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-8',
#             title= "E_D_BACK_EXTENSION_BAND_TITLE",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/back_extension_band.png'],
#                 preparation_steps=[
#                     'E_D_BACK_EXTENSION_BAND_PREP_ONE',
#                     'E_D_BACK_EXTENSION_BAND_PREP_TWO',
#                     'E_D_BACK_EXTENSION_BAND_PREP_THREE'
#                 ],
#                 execution_steps=[
#                     'E_D_BACK_EXTENSION_BAND_EXEC_ONE',
#                     'E_D_BACK_EXTENSION_BAND_EXEC_TWO'
#                 ],
#                 key_tips=[
#                     'E_D_BACK_EXTENSION_BAND_TIP_ONE',
#                     'E_D_BACK_EXTENSION_BAND_TIP_TWO'
#                 ],
#             focus_areas=[FocusArea.BACK],
#             equipment=ExerciseEquipment.BAND,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-9',
#             title= "E_D_BACK_EXTENSION_MACHINE_TITLE",
#             video_urls=['regular_directory/exercises/videos/back_extension_machine.mp4'],
#             cover_image_url=['regular_directory/exercises/images/back_extension_machine.png'],
#                 preparation_steps=[
#                     'E_D_BACK_EXTENSION_MACHINE_PREP_ONE',
#                     'E_D_BACK_EXTENSION_MACHINE_PREP_TWO'
#                 ],
#                 execution_steps=[
#                     'E_D_BACK_EXTENSION_MACHINE_EXEC_ONE',
#                     'E_D_BACK_EXTENSION_MACHINE_EXEC_TWO'
#                 ],
#                 key_tips=[
#                     'E_D_BACK_EXTENSION_MACHINE_TIP_ONE',
#                     'E_D_BACK_EXTENSION_MACHINE_TIP_TWO',
#                     'E_D_BACK_EXTENSION_MACHINE_TIP_THREE'
#                 ],
#             focus_areas=[FocusArea.BACK],
#             equipment=ExerciseEquipment.WEIGHT_MACHINE,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-1',
#             title="e_d_ab_wheel_title",
#             video_urls=['regular_directory/exercises/videos/ab_wheel.mp4'],
#             cover_image_url=['regular_directory/exercises/images/ab_wheel.png'],
#             preparation_steps=[
#                 'e_d_ab_wheel_prep_one',
#                 'e_d_ab_wheel_prep_two'
#             ],
#             execution_steps=[
#                 'e_d_ab_wheel_exec_one',
#                 'e_d_ab_wheel_exec_two',
#                 'e_d_ab_wheel_exec_three'
#             ],
#             key_tips=[
#                 'e_d_ab_wheel_tip_one',
#                 'e_d_ab_wheel_tip_two'
#             ],
#             focus_areas=[FocusArea.ABDOMEN, FocusArea.SHOULDER, FocusArea.BACK],
#             equipment=ExerciseEquipment.BODY_WEIGHT,
#             metric_type=ExerciseMetricType.TIME_BASED
#         ),
        
#         # Additional exercises extracted from exercises.txt and messages.po
#         ExerciseDefinition(
#             id='exercise-10',
#             title="e_d_backward_lunge_with_barbell",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/backward_lunge_barbell.png'],
#             preparation_steps=[
#                 'e_d_backward_lunge_with_barbell_prep_one',
#                 'e_d_backward_lunge_with_barbell_prep_two'
#             ],
#             execution_steps=[
#                 'e_d_backward_lunge_with_barbell_exec_one',
#                 'e_d_backward_lunge_with_barbell_exec_two'
#             ],
#             key_tips=[
#                 'e_d_backward_lunge_with_barbell_tip_one',
#                 'e_d_backward_lunge_with_barbell_tip_two'
#             ],
#             focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
#             equipment=ExerciseEquipment.BARBELL,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-11',
#             title="e_d_backward_lunge_with_cable",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/backward_lunge_cable.png'],
#             preparation_steps=[
#                 'e_d_backward_lunge_with_cable_prep_one',
#                 'e_d_backward_lunge_with_cable_prep_two'
#             ],
#             execution_steps=[
#                 'e_d_backward_lunge_with_cable_exec_one',
#                 'e_d_backward_lunge_with_cable_exec_two'
#             ],
#             key_tips=[
#                 'e_d_backward_lunge_with_cable_tip_one',
#                 'e_d_backward_lunge_with_cable_tip_two'
#             ],
#             focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
#             equipment=ExerciseEquipment.CABLE_MACHINE,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-12',
#             title="e_d_backward_lunge_with_dumbbell",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/backward_lunge_dumbbell.png'],
#             preparation_steps=[
#                 'e_d_backward_lunge_with_dumbbell_prep_one'
#             ],
#             execution_steps=[
#                 'e_d_backward_lunge_with_dumbbell_exec_one',
#                 'e_d_backward_lunge_with_dumbbell_exec_two'
#             ],
#             key_tips=[
#                 'e_d_backward_lunge_with_dumbbell_tip_one',
#                 'e_d_backward_lunge_with_dumbbell_tip_two'
#             ],
#             focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
#             equipment=ExerciseEquipment.DUMBBELL,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-13',
#             title="e_d_backward_lunge_with_kettlebell",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/backward_lunge_kettlebell.png'],
#             preparation_steps=[
#                 'e_d_backward_lunge_with_kettlebell_prep_one'
#             ],
#             execution_steps=[
#                 'e_d_backward_lunge_with_kettlebell_exec_one',
#                 'e_d_backward_lunge_with_kettlebell_exec_two'
#             ],
#             key_tips=[
#                 'e_d_backward_lunge_with_kettlebell_tip_one',
#                 'e_d_backward_lunge_with_kettlebell_tip_two'
#             ],
#             focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
#             equipment=ExerciseEquipment.KETTLEBELL,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-14',
#             title="e_d_backward_lunge_with_smith_machine",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/backward_lunge_smith.png'],
#             preparation_steps=[
#                 'e_d_backward_lunge_with_smith_machine_prep_one'
#             ],
#             execution_steps=[
#                 'e_d_backward_lunge_with_smith_machine_exec_one',
#                 'e_d_backward_lunge_with_smith_machine_exec_two'
#             ],
#             key_tips=[
#                 'e_d_backward_lunge_with_smith_machine_tip_one',
#                 'e_d_backward_lunge_with_smith_machine_tip_two'
#             ],
#             focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
#             equipment=ExerciseEquipment.SMITH_MACHINE,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-15',
#             title="e_d_ball_slams",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/ball_slams.png'],
#             preparation_steps=[
#                 'e_d_ball_slams_prep_one'
#             ],
#             execution_steps=[
#                 'e_d_ball_slams_exec_one',
#                 'e_d_ball_slams_exec_two',
#                 'e_d_ball_slams_exec_three'
#             ],
#             key_tips=[
#                 'e_d_ball_slams_tip_one',
#                 'e_d_ball_slams_tip_two'
#             ],
#             focus_areas=[FocusArea.FULL_BODY],
#             equipment=ExerciseEquipment.BODY_WEIGHT,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-16',
#             title="e_d_band_pull_through",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/band_pull_through.png'],
#             preparation_steps=[
#                 'e_d_band_pull_through_prep_one'
#             ],
#             execution_steps=[
#                 'e_d_band_pull_through_exec_one',
#                 'e_d_band_pull_through_exec_two'
#             ],
#             key_tips=[
#                 'e_d_band_pull_through_tip_one',
#                 'e_d_band_pull_through_tip_two',
#                 'e_d_band_pull_through_tip_three',
#                 'e_d_band_pull_through_tip_four'
#             ],
#             focus_areas=[FocusArea.BUTTOCKS, FocusArea.BACK, FocusArea.LEG],
#             equipment=ExerciseEquipment.HANDLE_BAND,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-17',
#             title="e_d_bench_fly_with_cable",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bench_fly_cable.png'],
#             preparation_steps=[
#                 'e_d_bench_fly_with_cable_prep_one'
#             ],
#             execution_steps=[
#                 'e_d_bench_fly_with_cable_exec_one',
#                 'e_d_bench_fly_with_cable_exec_two',
#                 'e_d_bench_fly_with_cable_exec_three'
#             ],
#             key_tips=[
#                 'e_d_bench_fly_with_cable_tip_one',
#                 'e_d_bench_fly_with_cable_tip_two',
#                 'e_d_bench_fly_with_cable_tip_three'
#             ],
#             focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
#             equipment=ExerciseEquipment.CABLE_MACHINE,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-18',
#             title="e_d_bench_fly_with_dumbbell",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bench_fly_dumbbell.png'],
#             preparation_steps=[
#                 'e_d_bench_fly_with_dumbbell_prep_one'
#             ],
#             execution_steps=[
#                 'e_d_bench_fly_with_dumbbell_exec_one',
#                 'e_d_bench_fly_with_dumbbell_exec_two',
#                 'e_d_bench_fly_with_dumbbell_exec_three'
#             ],
#             key_tips=[
#                 'e_d_bench_fly_with_dumbbell_tip_one',
#                 'e_d_bench_fly_with_dumbbell_tip_two',
#                 'e_d_bench_fly_with_dumbbell_tip_three'
#             ],
#             focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
#             equipment=ExerciseEquipment.DUMBBELL,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-19',
#             title="e_d_bench_jump",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bench_jump.png'],
#             preparation_steps=[
#                 'e_d_bench_jump_prep_one'
#             ],
#             execution_steps=[
#                 'e_d_bench_jump_exec_one',
#                 'e_d_bench_jump_exec_two',
#                 'e_d_bench_jump_exec_three'
#             ],
#             key_tips=[
#                 'e_d_bench_jump_tip_one',
#                 'e_d_bench_jump_tip_two',
#                 'e_d_bench_jump_tip_three'
#             ],
#             focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
#             equipment=ExerciseEquipment.BODY_WEIGHT,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-20',
#             title="e_d_bench_pistol_squat",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bench_pistol_squat.png'],
#             preparation_steps=[
#                 'e_d_bench_pistol_squat_prep_one'
#             ],
#             execution_steps=[
#                 'e_d_bench_pistol_squat_exec_one',
#                 'e_d_bench_pistol_squat_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bench_pistol_squat_tip_one',
#                 'e_d_bench_pistol_squat_tip_two',
#                 'e_d_bench_pistol_squat_tip_three'
#             ],
#             focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
#             equipment=ExerciseEquipment.BODY_WEIGHT,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-21',
#             title="e_d_bench_press_close_grip_barbell",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bench_press_close_barbell.png'],
#             preparation_steps=[
#                 'e_d_bench_press_close_grip_barbell_prep_one'
#             ],
#             execution_steps=[
#                 'e_d_bench_press_close_grip_barbell_exec_one',
#                 'e_d_bench_press_close_grip_barbell_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bench_press_close_grip_barbell_tip_one',
#                 'e_d_bench_press_close_grip_barbell_tip_two'
#             ],
#             focus_areas=[FocusArea.ARM, FocusArea.CHEST, FocusArea.SHOULDER],
#             equipment=ExerciseEquipment.BARBELL,
#             metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
#         ),
#         ExerciseDefinition(
#             id='exercise-22',
#             title="e_d_bench_press_close_grip_dumbbell",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bench_press_close_dumbbell.png'],
#             preparation_steps=[
#                 'e_d_bench_press_close_grip_dumbbell_prep_one'
#             ],
#             execution_steps=[
#                 'e_d_bench_press_close_grip_dumbbell_exec_one',
#                 'e_d_bench_press_close_grip_dumbbell_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bench_press_close_grip_dumbbell_tip_one',
#                 'e_d_bench_press_close_grip_dumbbell_tip_two'
#             ],
#             focus_areas=[FocusArea.ARM, FocusArea.CHEST, FocusArea.SHOULDER],
#             equipment=ExerciseEquipment.DUMBBELL,
#             metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
#         ),
#         ExerciseDefinition(
#             id='exercise-23',
#             title="e_d_bench_press_wide_grip_barbell",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bench_press_wide_barbell.png'],
#             preparation_steps=[
#                 'e_d_bench_press_wide_grip_barbell_prep_one'
#             ],
#             execution_steps=[
#                 'e_d_bench_press_wide_grip_barbell_exec_one',
#                 'e_d_bench_press_wide_grip_barbell_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bench_press_wide_grip_barbell_tip_one',
#                 'e_d_bench_press_wide_grip_barbell_tip_two'
#             ],
#             focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
#             equipment=ExerciseEquipment.BARBELL,
#             metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
#         ),
#         ExerciseDefinition(
#             id='exercise-24',
#             title="e_d_bench_press_with_band",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bench_press_band.png'],
#             preparation_steps=[
#                 'e_d_bench_press_with_band_prep_one'
#             ],
#             execution_steps=[
#                 'e_d_bench_press_with_band_exec_one',
#                 'e_d_bench_press_with_band_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bench_press_with_band_tip_one',
#                 'e_d_bench_press_with_band_tip_two',
#                 'e_d_bench_press_with_band_tip_three'
#             ],
#             focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
#             equipment=ExerciseEquipment.HANDLE_BAND,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-25',
#             title="e_d_bench_squat",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bench_squat.png'],
#             preparation_steps=[
#                 'e_d_bench_squat_prep_one'
#             ],
#             execution_steps=[
#                 'e_d_bench_squat_exec_one',
#                 'e_d_bench_squat_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bench_squat_tip_one',
#                 'e_d_bench_squat_tip_two',
#                 'e_d_bench_squat_tip_three'
#             ],
#             focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
#             equipment=ExerciseEquipment.BODY_WEIGHT,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
# ExerciseDefinition(
#             id='exercise-20',
#             title="e_d_bench_pistol_squat",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bench_pistol_squat.png'],
#             preparation_steps=['e_d_bench_pistol_squat_prep_one'],
#             execution_steps=[
#                 'e_d_bench_pistol_squat_exec_one',
#                 'e_d_bench_pistol_squat_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bench_pistol_squat_tip_one',
#                 'e_d_bench_pistol_squat_tip_two',
#                 'e_d_bench_pistol_squat_tip_three'
#             ],
#             focus_areas=[FocusArea.BUTTOCKS, FocusArea.LEG],
#             equipment=ExerciseEquipment.BODY_WEIGHT,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-21',
#             title="e_d_bench_press_close_grip_barbell",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bench_press_close_barbell.png'],
#             preparation_steps=['e_d_bench_press_close_grip_barbell_prep_one'],
#             execution_steps=[
#                 'e_d_bench_press_close_grip_barbell_exec_one',
#                 'e_d_bench_press_close_grip_barbell_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bench_press_close_grip_barbell_tip_one',
#                 'e_d_bench_press_close_grip_barbell_tip_two'
#             ],
#             focus_areas=[FocusArea.ARM, FocusArea.CHEST, FocusArea.SHOULDER],
#             equipment=ExerciseEquipment.BARBELL,
#             metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
#         ),
#         ExerciseDefinition(
#             id='exercise-22',
#             title="e_d_bench_press_close_grip_dumbbell",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bench_press_close_dumbbell.png'],
#             preparation_steps=['e_d_bench_press_close_grip_dumbbell_prep_one'],
#             execution_steps=[
#                 'e_d_bench_press_close_grip_dumbbell_exec_one',
#                 'e_d_bench_press_close_grip_dumbbell_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bench_press_close_grip_dumbbell_tip_one',
#                 'e_d_bench_press_close_grip_dumbbell_tip_two'
#             ],
#             focus_areas=[FocusArea.ARM, FocusArea.CHEST, FocusArea.SHOULDER],
#             equipment=ExerciseEquipment.DUMBBELL,
#             metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
#         ),
#         ExerciseDefinition(
#             id='exercise-23',
#             title="e_d_bench_press_wide_grip_barbell",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bench_press_wide_barbell.png'],
#             preparation_steps=['e_d_bench_press_wide_grip_barbell_prep_one'],
#             execution_steps=[
#                 'e_d_bench_press_wide_grip_barbell_exec_one',
#                 'e_d_bench_press_wide_grip_barbell_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bench_press_wide_grip_barbell_tip_one',
#                 'e_d_bench_press_wide_grip_barbell_tip_two'
#             ],
#             focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
#             equipment=ExerciseEquipment.BARBELL,
#             metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
#         ),
#         ExerciseDefinition(
#             id='exercise-24',
#             title="e_d_bench_press_with_band",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bench_press_band.png'],
#             preparation_steps=['e_d_bench_press_with_band_prep_one'],
#             execution_steps=[
#                 'e_d_bench_press_with_band_exec_one',
#                 'e_d_bench_press_with_band_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bench_press_with_band_tip_one',
#                 'e_d_bench_press_with_band_tip_two',
#                 'e_d_bench_press_with_band_tip_three'
#             ],
#             focus_areas=[FocusArea.CHEST, FocusArea.SHOULDER, FocusArea.ARM],
#             equipment=ExerciseEquipment.BAND,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-25',
#             title="e_d_bench_squat",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bench_squat.png'],
#             preparation_steps=['e_d_bench_squat_prep_one'],
#             execution_steps=[
#                 'e_d_bench_squat_exec_one',
#                 'e_d_bench_squat_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bench_squat_tip_one',
#                 'e_d_bench_squat_tip_two',
#                 'e_d_bench_squat_tip_three'
#             ],
#             focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
#             equipment=ExerciseEquipment.BODY_WEIGHT,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-26',
#             title="e_d_bench_squat_barbell",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bench_squat_barbell.png'],
#             preparation_steps=['e_d_bench_squat_barbell_prep_one'],
#             execution_steps=[
#                 'e_d_bench_squat_barbell_exec_one'
#             ],
#             key_tips=[
#                 'e_d_bench_squat_barbell_tip_one',
#                 'e_d_bench_squat_barbell_tip_two',
#                 'e_d_bench_squat_barbell_tip_three'
#             ],
#             focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
#             equipment=ExerciseEquipment.BARBELL,
#             metric_type=ExerciseMetricType.PERCENT_1RM_AND_REPS
#         ),
#         ExerciseDefinition(
#             id='exercise-27',
#             title="e_d_bench_squat_dumbbell",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bench_squat_dumbbell.png'],
#             preparation_steps=['e_d_bench_squat_dumbbell_prep_one'],
#             execution_steps=[
#                 'e_d_bench_squat_dumbbell_exec_one'
#             ],
#             key_tips=[
#                 'e_d_bench_squat_dumbbell_tip_one',
#                 'e_d_bench_squat_dumbbell_tip_two',
#                 'e_d_bench_squat_dumbbell_tip_three'
#             ],
#             focus_areas=[FocusArea.LEG, FocusArea.BUTTOCKS],
#             equipment=ExerciseEquipment.DUMBBELL,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-28',
#             title="e_d_bent_arm_pullover_barbell",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bent_arm_pullover_barbell.png'],
#             preparation_steps=['e_d_bent_arm_pullover_barbell_prep_one'],
#             execution_steps=[
#                 'e_d_bent_arm_pullover_barbell_exec_one',
#                 'e_d_bent_arm_pullover_barbell_exec_two',
#                 'e_d_bent_arm_pullover_barbell_exec_three'
#             ],
#             key_tips=[
#                 'e_d_bent_arm_pullover_barbell_tip_one',
#                 'e_d_bent_arm_pullover_barbell_tip_two'
#             ],
#             focus_areas=[FocusArea.BACK, FocusArea.ARM, FocusArea.CHEST],
#             equipment=ExerciseEquipment.BARBELL,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-29',
#             title="e_d_bent_knee_bicycle_crunch",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bent_knee_bicycle_crunch.png'],
#             preparation_steps=['e_d_bent_knee_bicycle_crunch_prep_one'],
#             execution_steps=[
#                 'e_d_bent_knee_bicycle_crunch_exec_one',
#                 'e_d_bent_knee_bicycle_crunch_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bent_knee_bicycle_crunch_tip_one',
#                 'e_d_bent_knee_bicycle_crunch_tip_two',
#                 'e_d_bent_knee_bicycle_crunch_tip_three'
#             ],
#             focus_areas=[FocusArea.ABDOMEN, FocusArea.LEG],
#             equipment=ExerciseEquipment.BODY_WEIGHT,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-30',
#             title="e_d_bent_knee_side_plank",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bent_knee_side_plank.png'],
#             preparation_steps=['e_d_bent_knee_side_plank_prep_one'],
#             execution_steps=[
#                 'e_d_bent_knee_side_plank_exec_one'
#             ],
#             key_tips=[
#                 'e_d_bent_knee_side_plank_tip_one',
#                 'e_d_bent_knee_side_plank_tip_two',
#                 'e_d_bent_knee_side_plank_tip_three'
#             ],
#             focus_areas=[FocusArea.ABDOMEN],
#             equipment=ExerciseEquipment.BODY_WEIGHT,
#             metric_type=ExerciseMetricType.TIME_BASED
#         ),
#         ExerciseDefinition(
#             id='exercise-31',
#             title="e_d_bent_knee_wipers",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bent_knee_wipers.png'],
#             preparation_steps=['e_d_bent_knee_wipers_prep_one'],
#             execution_steps=[
#                 'e_d_bent_knee_wipers_exec_one',
#                 'e_d_bent_knee_wipers_exec_two',
#                 'e_d_bent_knee_wipers_exec_three'
#             ],
#             key_tips=[
#                 'e_d_bent_knee_wipers_tip_one',
#                 'e_d_bent_knee_wipers_tip_two',
#                 'e_d_bent_knee_wipers_tip_three'
#             ],
#             focus_areas=[FocusArea.ABDOMEN],
#             equipment=ExerciseEquipment.BODY_WEIGHT,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-32',
#             title="e_d_bent_over_rear_delt_row_barbell",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bent_over_rear_delt_row_barbell.png'],
#             preparation_steps=['e_d_bent_over_rear_delt_row_barbell_prep_one'],
#             execution_steps=[
#                 'e_d_bent_over_rear_delt_row_barbell_exec_one',
#                 'e_d_bent_over_rear_delt_row_barbell_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bent_over_rear_delt_row_barbell_tip_one',
#                 'e_d_bent_over_rear_delt_row_barbell_tip_two'
#             ],
#             focus_areas=[FocusArea.SHOULDER, FocusArea.BACK],
#             equipment=ExerciseEquipment.BARBELL,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-33',
#             title="e_d_bent_over_rear_delt_row_dumbbell",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bent_over_rear_delt_row_dumbbell.png'],
#             preparation_steps=['e_d_bent_over_rear_delt_row_dumbbell_prep_one'],
#             execution_steps=[
#                 'e_d_bent_over_rear_delt_row_dumbbell_exec_one',
#                 'e_d_bent_over_rear_delt_row_dumbbell_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bent_over_rear_delt_row_dumbbell_tip_one',
#                 'e_d_bent_over_rear_delt_row_dumbbell_tip_two'
#             ],
#             focus_areas=[FocusArea.SHOULDER, FocusArea.BACK],
#             equipment=ExerciseEquipment.DUMBBELL,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-34',
#             title="e_d_bent_over_rear_delt_row_kettlebell",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bent_over_rear_delt_row_kettlebell.png'],
#             preparation_steps=['e_d_bent_over_rear_delt_row_kettlebell_prep_one'],
#             execution_steps=[
#                 'e_d_bent_over_rear_delt_row_kettlebell_exec_one',
#                 'e_d_bent_over_rear_delt_row_kettlebell_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bent_over_rear_delt_row_kettlebell_tip_one',
#                 'e_d_bent_over_rear_delt_row_kettlebell_tip_two'
#             ],
#             focus_areas=[FocusArea.SHOULDER, FocusArea.BACK],
#             equipment=ExerciseEquipment.KETTLEBELL,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-35',
#             title="e_d_bent_over_rear_delt_row_smith_machine",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bent_over_rear_delt_row_smith.png'],
#             preparation_steps=['e_d_bent_over_rear_delt_row_smith_machine_prep_one'],
#             execution_steps=[
#                 'e_d_bent_over_rear_delt_row_smith_machine_exec_one',
#                 'e_d_bent_over_rear_delt_row_smith_machine_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bent_over_rear_delt_row_smith_machine_tip_one',
#                 'e_d_bent_over_rear_delt_row_smith_machine_tip_two'
#             ],
#             focus_areas=[FocusArea.SHOULDER, FocusArea.BACK],
#             equipment=ExerciseEquipment.SMITH_MACHINE,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-36',
#             title="e_d_bent_over_reverse_fly_band",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bent_over_reverse_fly_band.png'],
#             preparation_steps=['e_d_bent_over_reverse_fly_band_prep_one'],
#             execution_steps=[
#                 'e_d_bent_over_reverse_fly_band_exec_one',
#                 'e_d_bent_over_reverse_fly_band_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bent_over_reverse_fly_band_tip_one',
#                 'e_d_bent_over_reverse_fly_band_tip_two'
#             ],
#             focus_areas=[FocusArea.SHOULDER, FocusArea.BACK],
#             equipment=ExerciseEquipment.BAND,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-37',
#             title="e_d_bent_over_reverse_fly_dumbbell",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bent_over_reverse_fly_dumbbell.png'],
#             preparation_steps=['e_d_bent_over_reverse_fly_dumbbell_prep_one'],
#             execution_steps=[
#                 'e_d_bent_over_reverse_fly_dumbbell_exec_one',
#                 'e_d_bent_over_reverse_fly_dumbbell_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bent_over_reverse_fly_dumbbell_tip_one',
#                 'e_d_bent_over_reverse_fly_dumbbell_tip_two'
#             ],
#             focus_areas=[FocusArea.SHOULDER, FocusArea.BACK],
#             equipment=ExerciseEquipment.DUMBBELL,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-38',
#             title="e_d_bent_over_row_barbell",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bent_over_row_barbell.png'],
#             preparation_steps=['e_d_bent_over_row_barbell_prep_one'],
#             execution_steps=[
#                 'e_d_bent_over_row_barbell_exec_one',
#                 'e_d_bent_over_row_barbell_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bent_over_row_barbell_tip_one',
#                 'e_d_bent_over_row_barbell_tip_two'
#             ],
#             focus_areas=[FocusArea.BACK, FocusArea.ARM],
#             equipment=ExerciseEquipment.BARBELL,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-39',
#             title="e_d_bent_over_row_dumbbell",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bent_over_row_dumbbell.png'],
#             preparation_steps=['e_d_bent_over_row_dumbbell_prep_one'],
#             execution_steps=[
#                 'e_d_bent_over_row_dumbbell_exec_one',
#                 'e_d_bent_over_row_dumbbell_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bent_over_row_dumbbell_tip_one',
#                 'e_d_bent_over_row_dumbbell_tip_two'
#             ],
#             focus_areas=[FocusArea.BACK, FocusArea.ARM],
#             equipment=ExerciseEquipment.DUMBBELL,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-40',
#             title="e_d_bent_over_row_kettlebell",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bent_over_row_kettlebell.png'],
#             preparation_steps=['e_d_bent_over_row_kettlebell_prep_one'],
#             execution_steps=[
#                 'e_d_bent_over_row_kettlebell_exec_one',
#                 'e_d_bent_over_row_kettlebell_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bent_over_row_kettlebell_tip_one',
#                 'e_d_bent_over_row_kettlebell_tip_two'
#             ],
#             focus_areas=[FocusArea.BACK, FocusArea.ARM],
#             equipment=ExerciseEquipment.KETTLEBELL,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-41',
#             title="e_d_bent_over_row_smith_machine",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bent_over_row_smith_machine.png'],
#             preparation_steps=['e_d_bent_over_row_smith_machine_prep_one'],
#             execution_steps=[
#                 'e_d_bent_over_row_smith_machine_exec_one',
#                 'e_d_bent_over_row_smith_machine_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bent_over_row_smith_machine_tip_one',
#                 'e_d_bent_over_row_smith_machine_tip_two'
#             ],
#             focus_areas=[FocusArea.BACK, FocusArea.SHOULDER],
#             equipment=ExerciseEquipment.SMITH_MACHINE,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-42',
#             title="e_d_bicep_curl_bodyweight",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bicep_curl_bodyweight.png'],
#             preparation_steps=['e_d_bicep_curl_bodyweight_prep_one'],
#             execution_steps=[
#                 'e_d_bicep_curl_bodyweight_exec_one',
#                 'e_d_bicep_curl_bodyweight_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bicep_curl_bodyweight_tip_one',
#                 'e_d_bicep_curl_bodyweight_tip_two'
#             ],
#             focus_areas=[FocusArea.ARM],
#             equipment=ExerciseEquipment.BODY_WEIGHT,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-43',
#             title="e_d_bicep_curl_band",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bicep_curl_band.png'],
#             preparation_steps=['e_d_bicep_curl_band_prep_one'],
#             execution_steps=[
#                 'e_d_bicep_curl_band_exec_one'
#             ],
#             key_tips=[
#                 'e_d_bicep_curl_band_tip_one',
#                 'e_d_bicep_curl_band_tip_two'
#             ],
#             focus_areas=[FocusArea.ARM],
#             equipment=ExerciseEquipment.BAND,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-44',
#             title="e_d_bicep_curl_barbell",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bicep_curl_barbell.png'],
#             preparation_steps=['e_d_bicep_curl_barbell_prep_one'],
#             execution_steps=[
#                 'e_d_bicep_curl_barbell_exec_one'
#             ],
#             key_tips=[
#                 'e_d_bicep_curl_barbell_tip_one',
#                 'e_d_bicep_curl_barbell_tip_two'
#             ],
#             focus_areas=[FocusArea.ARM],
#             equipment=ExerciseEquipment.BARBELL,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-45',
#             title="e_d_bicep_curl_cable",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bicep_curl_cable.png'],
#             preparation_steps=['e_d_bicep_curl_cable_prep_one'],
#             execution_steps=[
#                 'e_d_bicep_curl_cable_exec_one'
#             ],
#             key_tips=[
#                 'e_d_bicep_curl_cable_tip_one',
#                 'e_d_bicep_curl_cable_tip_two',
#                 'e_d_bicep_curl_cable_tip_three'
#             ],
#             focus_areas=[FocusArea.ARM],
#             equipment=ExerciseEquipment.CABLE_MACHINE,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-46',
#             title="e_d_bicep_curl_dumbbell",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bicep_curl_dumbbell.png'],
#             preparation_steps=['e_d_bicep_curl_dumbbell_prep_one'],
#             execution_steps=[
#                 'e_d_bicep_curl_dumbbell_exec_one'
#             ],
#             key_tips=[
#                 'e_d_bicep_curl_dumbbell_tip_one',
#                 'e_d_bicep_curl_dumbbell_tip_two'
#             ],
#             focus_areas=[FocusArea.ARM],
#             equipment=ExerciseEquipment.DUMBBELL,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-47',
#             title="e_d_bicep_curl_machine",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bicep_curl_machine.png'],
#             preparation_steps=['e_d_bicep_curl_machine_prep_one'],
#             execution_steps=[
#                 'e_d_bicep_curl_machine_exec_one'
#             ],
#             key_tips=[
#                 'e_d_bicep_curl_machine_tip_one',
#                 'e_d_bicep_curl_machine_tip_two'
#             ],
#             focus_areas=[FocusArea.ARM],
#             equipment=ExerciseEquipment.WEIGHT_MACHINE,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-48',
#             title="e_d_bicep_curl_smith_machine",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bicep_curl_smith_machine.png'],
#             preparation_steps=['e_d_bicep_curl_smith_machine_prep_one'],
#             execution_steps=[
#                 'e_d_bicep_curl_smith_machine_exec_one'
#             ],
#             key_tips=[
#                 'e_d_bicep_curl_smith_machine_tip_one',
#                 'e_d_bicep_curl_smith_machine_tip_two'
#             ],
#             focus_areas=[FocusArea.ARM],
#             equipment=ExerciseEquipment.SMITH_MACHINE,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-49',
#             title="e_d_bicycle_crunch",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bicycle_crunch.png'],
#             preparation_steps=['e_d_bicycle_crunch_prep_one'],
#             execution_steps=[
#                 'e_d_bicycle_crunch_exec_one',
#                 'e_d_bicycle_crunch_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bicycle_crunch_tip_one',
#                 'e_d_bicycle_crunch_tip_two'
#             ],
#             focus_areas=[FocusArea.ABDOMEN, FocusArea.LEG],
#             equipment=ExerciseEquipment.BODY_WEIGHT,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
#         ExerciseDefinition(
#             id='exercise-50',
#             title="e_d_bicycle_crunch_band",
#             video_urls=None,
#             cover_image_url=['regular_directory/exercises/images/bicycle_crunch_band.png'],
#             preparation_steps=['e_d_bicycle_crunch_band_prep_one'],
#             execution_steps=[
#                 'e_d_bicycle_crunch_band_exec_one',
#                 'e_d_bicycle_crunch_band_exec_two'
#             ],
#             key_tips=[
#                 'e_d_bicycle_crunch_band_tip_one',
#                 'e_d_bicycle_crunch_band_tip_two'
#             ],
#             focus_areas=[FocusArea.ABDOMEN, FocusArea.LEG],
#             equipment=ExerciseEquipment.BAND,
#             metric_type=ExerciseMetricType.REPS_ONLY
#         ),
    ]
