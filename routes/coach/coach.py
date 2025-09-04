

from typing import Annotated

from fastapi import  APIRouter, Body, Depends, Form, HTTPException, Query, Security, UploadFile, status
from fastapi.responses import JSONResponse
from data.local_database.model.coach import Coach
from data.local_database.model.coach_program import CoachProgram
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