from typing import Annotated

from fastapi import  APIRouter, Body, Depends, Form, HTTPException, Query, Security, UploadFile, status
from fastapi.responses import JSONResponse
from data.local_database.model.coach import Coach
from data.local_database.model.coach_program import CoachProgram
from data.local_database.model.trainee_history import TraineeHistory
from data.local_database.model.user_physical_data import UserPhysicalData
from data.local_database.model.user_files import FileData
from data.remote_api.model.exceptions import NotFoundError
from dependeny_manager import dm
from domain_models import  UserUpdateRequest, UserPhysicalDataUpsert,UserInDB,GallaryTag, ArchiveUserImagesResponse,UserPhysicalDataValidationError

from domain_models.response_model import ErrorResponse
from utility.decode_jwt_user_id import read_user_or_raise
from utility.translation_keys import TranslationKeys
from utility.constants import upload_directory_path
from fastapi.encoders import jsonable_encoder
from data.local_database.model.program_enrollment import ExerciseDefinition, ProgramEnrollment, WorkoutProgram



router = APIRouter(
    prefix="/coach",
    tags=["Coach"],
    #TOdo add dependency
)

@router.get("/coach_profile/", responses={
    200: {"model": Coach, "description": "HTTP_200_OK"},
    404: {"description": "HTTP_404_NOT_FOUND"},
})
async def read_coach(
    user_id: Annotated[str, Security(read_user_or_raise, scopes=["coach"])],
):
    coach = await dm.coach_repo.read_coach(user_id=user_id)
    if coach is None:
        coach = Coach(user_id=user_id,biography='', is_active=True)
        coach = await dm.coach_repo.upsert_coach(coach=coach)
        # raise HTTPException(
        #     status_code=status.HTTP_404_NOT_FOUND,
        #     detail=ErrorResponse(
        #         error_detail='TranslationKeys.OBJECT_NOT_FOUND',
        #         message=TranslationKeys.OBJECT_NOT_FOUND
        #     ).model_dump()
        # )
    return JSONResponse(
        content=coach.model_dump()
    )

@router.put("/update_coach_profile/", responses={
    200: {"model": Coach, "description": "HTTP_200_OK"},
    404: {"description": "HTTP_404_NOT_FOUND"},
})
async def update_coach(
    user_id: Annotated[str, Security(read_user_or_raise, scopes=["coach"])],
    coach_profile: Annotated[Coach, Body()]
):
    coach = await dm.coach_repo.upsert_coach(coach=coach_profile)
    if coach is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ErrorResponse(
                error_detail='TranslationKeys.OBJECT_NOT_FOUND',
                message=TranslationKeys.OBJECT_NOT_FOUND
            ).model_dump()
        )
    return JSONResponse(
        content=coach.model_dump()
    )

@router.post("/upsert_coach_program/", responses={
    200: {"model": CoachProgram, "description": "HTTP_200_OK"},
    400: {"description": "HTTP_400_BAD_REQUEST"},
})
async def upsert_coach_program(
    user_id: Annotated[str, Security(read_user_or_raise, scopes=["coach"])],
    program: Annotated[CoachProgram, Body()]
):
    program.user_id = user_id
    coach_program = await dm.coach_repo.upsert_coach_program(program=program)
    return JSONResponse(
        content=coach_program.model_dump()
    )

@router.delete("/delete_coach_program/", status_code=status.HTTP_204_NO_CONTENT, responses={
    204: {"description": "HTTP_204_NO_CONTENT"},
    404: {"description": "HTTP_404_NOT_FOUND"},
})
async def delete_coach_program(
    user_id: Annotated[str, Security(read_user_or_raise, scopes=["coach"])],
    program_id: Annotated[str, Query()]
):
    try:
        await dm.coach_repo.delete_coach_program(program_id=program_id)
    except NotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ErrorResponse(
                error_detail='TranslationKeys.OBJECT_NOT_FOUND',
                message=TranslationKeys.OBJECT_NOT_FOUND
            ).model_dump()
        )

@router.get("/read_coach_programs/", responses={
    200: {"model": list[CoachProgram], "description": "HTTP_200_OK"},
    404: {"description": "HTTP_404_NOT_FOUND"},
})
async def read_coach_programs(
    user_id: Annotated[str, Security(read_user_or_raise, scopes=["coach"])],
):
    programs = await dm.coach_repo.read_coach_programs(user_id=user_id)
    if programs is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ErrorResponse(
                error_detail='TranslationKeys.OBJECT_NOT_FOUND',
                message=TranslationKeys.OBJECT_NOT_FOUND
            ).model_dump()
        )
    return JSONResponse(
        content=[program.model_dump() for program in programs]
    )


@router.get("/read_coaches/", responses={
    200: {"model": list[Coach], "description": "HTTP_200_OK"},
    404: {"description": "HTTP_404_NOT_FOUND"},
})
async def read_coaches(
    user_id: Annotated[str, Security(read_user_or_raise)],
):
    coaches = await dm.coach_repo.read_coaches()
    return JSONResponse(
        content=[coach.model_dump() for coach in coaches]
    )
    
@router.get("/read_coaches_profile/", responses={
    200: {"model": list[UserInDB], "description": "HTTP_200_OK"},
    404: {"description": "HTTP_404_NOT_FOUND"},
})
async def read_coaches_profile(
    user_id: Annotated[str, Security(read_user_or_raise)],
):
    coachesProfile = await dm.coach_repo.read_coaches_profile()
    return JSONResponse(
        content=[coachProfile.model_dump(exclude={"verification_code", "hashed_password", "is_phone_number_verified", "is_email_verified"}) for coachProfile in coachesProfile]
    )

@router.get("/read_coach_programs_by_coach_id/", responses={
    200: {"model": list[Coach], "description": "HTTP_200_OK"},
    404: {"description": "HTTP_404_NOT_FOUND"},
})
async def read_coach_programs_by_coach_id(
    user_id: Annotated[str, Security(read_user_or_raise)],
    coach_id : Annotated[str, Query()],
):
    coach_programs = await dm.coach_repo.read_coach_programs(user_id=coach_id)
    return JSONResponse(
        content=[coach_program.model_dump() for coach_program in coach_programs]
    )

    
@router.get("/read_coach_images/", responses={
    200: {"model": list[FileData], "description": "HTTP_200_OK"},
    404: {"description": "HTTP_404_NOT_FOUND"},
})
async def read_coach_images(
    user_id: Annotated[str, Depends(read_user_or_raise)],
    coach_id : Annotated[str, Query()],
):
    coach_images = await dm.user_files_repo.read_user_image_gallary(user_id=coach_id, tags=[GallaryTag.CERTIFICATE, GallaryTag.ACHIVEMENT, GallaryTag.PROFILE_IMAGE])
    return JSONResponse(
        content=[jsonable_encoder(coach_image.model_dump()) for coach_image in coach_images]
    )

@router.get("/read_trainee_history/", responses={
    200: {"model": list[TraineeHistory], "description": "HTTP_200_OK"},
    404: {"description": "HTTP_404_NOT_FOUND"},
})
async def read_trainee_history(
    user_id: Annotated[str, Security(read_user_or_raise, scopes=["coach"])],
    trainee_id: Annotated[str, Query()],
):
    trainee_history = await dm.coach_repo.read_trainee_history(user_id=trainee_id)
    if trainee_history is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ErrorResponse(
                error_detail='TranslationKeys.OBJECT_NOT_FOUND',
                message=TranslationKeys.OBJECT_NOT_FOUND
            ).model_dump()
        )
    return JSONResponse(
        content=[th.model_dump() for th in trainee_history]
    )

@router.post("/upsert_trainee_history/", responses={
    200: {"model": TraineeHistory, "description": "HTTP_200_OK"},
    400: {"description": "HTTP_400_BAD_REQUEST"},
})
async def upsert_trainee_history(
    user_id: Annotated[str, Depends(read_user_or_raise)],
    trainee_history: Annotated[TraineeHistory, Body()]
):
    result = await dm.coach_repo.upsert_trainee_history(trainee_history=trainee_history)
    return JSONResponse(
        content=result.model_dump()
    )
    
@router.get("/read_enrollments/", responses={
    200: {"model": list[ProgramEnrollment], "description": "HTTP_200_OK"},
    404: {"description": "HTTP_404_NOT_FOUND"},
})
async def read_enrollments(
    user_id: Annotated[str, Depends(read_user_or_raise)],
    coach_id: Annotated[str | None, Query()] = None,
    trainee_id: Annotated[str | None, Query()] = None,
):
    if (coach_id is None and trainee_id is None):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ErrorResponse(
                error_detail='TranslationKeys.OBJECT_NOT_FOUND',
                message="Atlest one of coach_id or trainee_id must be provided."
            ).model_dump()
        )
    enrollments = await dm.coach_repo.read_enrollments(coach_id=coach_id, trainee_id=trainee_id)
    if enrollments is None or len(enrollments) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ErrorResponse(
                error_detail='TranslationKeys.OBJECT_NOT_FOUND',
                message=TranslationKeys.OBJECT_NOT_FOUND
            ).model_dump()
        )
    return JSONResponse(
        content=[jsonable_encoder(enrollment.model_dump()) for enrollment in enrollments]
    )

@router.post("/upsert_enrollment/", responses={
    200: {"model": ProgramEnrollment, "description": "HTTP_200_OK"},
    400: {"description": "HTTP_400_BAD_REQUEST"},
})
async def upsert_enrollment(
    user_id: Annotated[str, Depends(read_user_or_raise)],
    program_enrollment: Annotated[ProgramEnrollment, Body()]
):
    result = await dm.coach_repo.upsert_enrollment(program_enrollment=program_enrollment)
    return JSONResponse(
        content=jsonable_encoder(result.model_dump())
    )
    
@router.get("/read_coach_athletes_profile/", responses={
    200: {"model": list[UserInDB], "description": "HTTP_200_OK"},
    404: {"description": "HTTP_404_NOT_FOUND"},
})
async def read_coach_athletes_profile(
    user_id: Annotated[str, Security(read_user_or_raise, scopes=["coach"])],
):
    coachesProfile = await dm.coach_repo.read_coach_athletes_profile(coach_id=user_id)
    return JSONResponse(
        content=[coachProfile.model_dump(exclude={"verification_code", "hashed_password", "is_phone_number_verified", "is_email_verified"}) for coachProfile in coachesProfile]
    )
    
@router.post("/upsert_workout_program/", responses={
    200: {"model": WorkoutProgram, "description": "HTTP_200_OK"},
    400: {"description": "HTTP_400_BAD_REQUEST"},
})
async def upsert_workout_program(
    user_id: Annotated[str, Security(read_user_or_raise)],
    workout_program: Annotated[WorkoutProgram, Body()]
):
    
    result = await dm.coach_repo.upsert_workout_program(workout_program=workout_program)
    return JSONResponse(
        content=result.model_dump()
    )

@router.get("/read_workout_program/", responses={
    200: {"model": list[ExerciseDefinition], "description": "HTTP_200_OK"},
    404: {"description": "HTTP_404_NOT_FOUND"},
})
async def read_workout_program(
    user_id: Annotated[str, Depends(read_user_or_raise)],
    workout_id: Annotated[str, Query()]
):
    workout_program = await dm.coach_repo.read_workout_program(workout_id=workout_id)
    if workout_program is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ErrorResponse(
                error_detail='TranslationKeys.OBJECT_NOT_FOUND',
                message=TranslationKeys.OBJECT_NOT_FOUND
            ).model_dump()
        )
    return JSONResponse(
        content=workout_program.model_dump()
    )
    
@router.get("/read_workouts_definition/", responses={
    200: {"model": WorkoutProgram, "description": "HTTP_200_OK"},
    404: {"description": "HTTP_404_NOT_FOUND"},
})
async def read_workouts_definition(
    user_id: Annotated[str, Depends(read_user_or_raise)],
    workout_id: Annotated[str, Query()]
):
    workout_program = await dm.coach_repo.read_workout_program(workout_id=workout_id)
    if workout_program is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ErrorResponse(
                error_detail='TranslationKeys.OBJECT_NOT_FOUND',
                message=TranslationKeys.OBJECT_NOT_FOUND
            ).model_dump()
        )
    return JSONResponse(
        content=workout_program.model_dump()
    )
    
@router.get("/read_exercise_definition/", responses={
    200: {"model": list[ExerciseDefinition], "description": "HTTP_200_OK"},
    404: {"description": "HTTP_404_NOT_FOUND"},
})
async def read_exercise_definition(
    user_id: Annotated[str, Depends(read_user_or_raise)],
):
    exercises_definition = await dm.coach_repo.read_exercise_definition()
    return JSONResponse(
        content=[exercise.model_dump() for exercise in exercises_definition]
    )
