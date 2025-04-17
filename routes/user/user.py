
from typing import Annotated

from fastapi import  APIRouter, Body, Depends, File, Form, HTTPException, Query, UploadFile, status
from dependeny_manager import dm
from domain_models import ApiResponse, UserUpdateRequest, UserBioDataRequest,UserBioData,UserInDB,GallaryTag,User
from domain_models.exceptions import InvalidUploadFileRequest
from utility.decode_jwt_user_id import jwt_user_id
from utility.translation_keys import TranslationKeys


router = APIRouter(
    prefix="/user",
    tags=["User"],
    #TOdo add dependency
)

async def read_user_or_raise(user_id: Annotated[str , Depends(jwt_user_id)])-> str:
     user = await dm.user_repo.read_user(user_id=user_id)
     if user is None or user.id is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=TranslationKeys.USER_NOT_FOUND,
        )
     return user.id

@router.get("/user_profile/")
async def read_user(
    user_id: Annotated[str , Depends(read_user_or_raise)],
) :
    user = await dm.user_repo.read_user(user_id=user_id)
    assert(user is not None)
    return ApiResponse.success(
        data = user.model_dump(exclude={"verification_code", "hashed_password"})
    ).to_dict()

@router.put("/update_profile/")
async def update_user(
    user_id: Annotated[str , Depends(read_user_or_raise)],
    user_profile : Annotated[UserUpdateRequest, Body()]
) :
     user_dict = user_profile.model_dump()
     user_dict['_id'] = user_id
     user_in_db = UserInDB( **user_dict )
     user = await dm.user_repo.update_user( user=user_in_db)
     if user is None:
         raise HTTPException(
             status_code= status.HTTP_404_NOT_FOUND,
             detail=TranslationKeys.USER_NOT_FOUND
         )
     else:
         return ApiResponse.success(
             data = user.model_dump(exclude={"verification_code", "hashed_password"})
         ).to_dict()


@router.put("/update_user_bio_data/")
async def update_user_bio_data(
    user_id: Annotated[str , Depends(read_user_or_raise)],
    user_bio_data : Annotated[UserBioDataRequest, Body()]
) :

    bio_data = await dm.user_repo.upsert_user_bio_data(
        user_bio_data=UserBioData(
            user_id=user_id,
            gender=user_bio_data.gender,
            age=user_bio_data.age,
            body_composition=user_bio_data.body_composition
        )
    )
    return ApiResponse.success(
                data = bio_data.model_dump()
            ).to_dict()


@router.get("/read_user_bio_data/")
async def read_user_bio_data(
    user_id: Annotated[str , Depends(read_user_or_raise)],
) :
    bio_data = await dm.user_repo.read_user_bio_data(
        user_id=user_id,
    )
    if bio_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= ApiResponse.error(message= 'TranslationKeys.OBJECT_NOT_FOUND', error_detail=TranslationKeys.OBJECT_NOT_FOUND).to_dict()
        )
    return ApiResponse.success(
                data = bio_data.model_dump()
            ).to_dict()

@router.get("/read_user_image_profile/")
async def read_user_profile_image(
    user_id: Annotated[str , Depends(read_user_or_raise)],
) :
    profile_image_path = await dm.user_files_repo.read_user_profile_image(
        user_id=user_id,
    )
    if profile_image_path is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= ApiResponse.error(message= 'TranslationKeys.OBJECT_NOT_FOUND', error_detail=TranslationKeys.OBJECT_NOT_FOUND).to_dict()
        )
    return ApiResponse.success(
                data = {
                    'profile_path' : profile_image_path
                }
            ).to_dict()

@router.get("/read_user_image_gallary/")
async def read_user_image_gallary(
    user_id: Annotated[str , Depends(read_user_or_raise)],
    tags: Annotated[list[str | GallaryTag] , Query()],
) :
    image_gallary = await dm.user_files_repo.read_user_image_gallary(
        user_id=user_id,
        tags=tags
    )
    if image_gallary is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= ApiResponse.error(message= 'TranslationKeys.OBJECT_NOT_FOUND', error_detail=TranslationKeys.OBJECT_NOT_FOUND).to_dict()
        )
    return ApiResponse.success(
                data = image_gallary
            ).to_dict()

@router.put("/upsert_user_files/", description='profile image or image gallary files should not be None at same time')
async def upsert_user_files(
    user_id: Annotated[str , Depends(read_user_or_raise)],
    tag: Annotated[str | GallaryTag , Form()],
    image_gallary_files: Annotated[
        list[UploadFile] | None, File()
    ],
    profile_image: Annotated[
        UploadFile | None, File()
    ],
) :
    if image_gallary_files is None and profile_image is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= ApiResponse.error(message= 'TranslationKeys.INVALID_UPLOAD_FILE_REQUEST', error_detail=TranslationKeys.INVALID_UPLOAD_FILE_REQUEST).to_dict()
        )
    profile_image_dict = await dm.user_files_repo.read_user_image_gallary(
        user_id=user_id,
        tags=[tag]
    )
    if profile_image_dict is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= ApiResponse.error(message= 'TranslationKeys.OBJECT_NOT_FOUND', error_detail=TranslationKeys.OBJECT_NOT_FOUND).to_dict()
        )
    return ApiResponse.success(
                data = profile_image_dict
            ).to_dict()
