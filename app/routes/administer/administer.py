

from datetime import datetime
from typing import Annotated

from fastapi import  APIRouter, Body, Depends, Form, HTTPException, Query, Security, UploadFile, status
from fastapi.responses import JSONResponse
from data.local_database.model.user_physical_data import UserPhysicalData
from data.local_database.model.user_files import FileData
from data.remote_api.model.exceptions import NotFoundError
from dependeny_manager import dm
from domain_models import  UserUpdateRequest, UserPhysicalDataUpsert,UserInDB,GallaryTag, ArchiveUserImagesResponse,UserPhysicalDataValidationError,username_type,UsernameType, NetworkConnectionError, PaymentStatus

from domain_models import ErrorResponse, Referral, Role
from utility.decode_jwt_user_id import read_user_or_raise
from utility import TranslationKeys, translation_manager
from utility.constants import upload_directory_path
from fastapi.encoders import jsonable_encoder



router = APIRouter(
    prefix="/administer",
    tags=["Administer"],
    #TOdo add dependency
)



@router.get("/read_user_count/",  responses={
    200 : {"model" : dict , "description": "HTTP_200_OK",},
    })
async def read_user_count(
    user_id: Annotated[str , Security(read_user_or_raise, scopes=["admin"])],
    roles: Annotated[list[Role] , Query()],
) :
    user_count = await dm.user_repo.read_user_count(roles=roles)
    
    return JSONResponse(
        content={"user_count" : user_count}
    )
    
@router.get("/coaches_programs_count/",  responses={
    200 : {"model" : dict , "description": "HTTP_200_OK",},
    })
async def coaches_programs_count(
    user_id: Annotated[str , Security(read_user_or_raise, scopes=["admin"])],
) :
    coaches_programs_count = await dm.coach_repo.read_coaches_programs_count()
    
    return JSONResponse(
        content={"coach_program_count" : coaches_programs_count}
    )
    
@router.get("/completed_exercise_count/",  responses={
    200 : {"model" : dict , "description": "HTTP_200_OK",},
    })
async def completed_exercise_count(
    user_id: Annotated[str , Security(read_user_or_raise, scopes=["admin"])],
) :
    completed_exercise_count = await dm.coach_repo.completed_exercise_count()
    
    return JSONResponse(
        content={"completed_exercise_count" : completed_exercise_count}
    )
    
@router.get("/coaches_purchased_programs_count/",  responses={
    200 : {"model" : dict , "description": "HTTP_200_OK",},
    })
async def coaches_purchased_programs_count(
    user_id: Annotated[str , Security(read_user_or_raise, scopes=["admin"])],
    status: Annotated[list[PaymentStatus], Query()],
    #TODO add duration for report
) :
    user_count = await dm.payment_repo.coaches_purchased_programs_count(status=status)
    
    return JSONResponse(
        content={"coaches_purchased_programs_count" : user_count}
    )
