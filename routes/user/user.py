

from typing import Annotated

from fastapi import  APIRouter, Body, Depends, Form, HTTPException, Query, UploadFile, status
from fastapi.responses import JSONResponse
from data.local_database.model.user_bio_data import UserBioData
from data.local_database.model.user_files import FileData
from data.remote_api.model.exceptions import NotFoundError
from dependeny_manager import dm
from domain_models import  UserUpdateRequest, UserBioDataUpsert,UserInDB,GallaryTag, ArchiveUserImagesResponse,UserBioDataValidationError

from domain_models.response_model import ErrorResponse
from utility.decode_jwt_user_id import read_user_or_raise
from utility.translation_keys import TranslationKeys
from utility.constants import upload_directory_path
from fastapi.encoders import jsonable_encoder



router = APIRouter(
    prefix="/user",
    tags=["User"],
    #TOdo add dependency
)



@router.get("/user_profile/",  responses={
    200 : {"model" : UserInDB , "description": "HTTP_200_OK",},
    })
async def read_user(
    user_id: Annotated[str , Depends(read_user_or_raise)],
) :
    user = await dm.user_repo.read_user(user_id=user_id)
    assert(user is not None)
    return JSONResponse(
        content=user.model_dump(by_alias=True,exclude={"verification_code", "hashed_password", "is_verified"})
    )

@router.put("/update_profile/",  responses={
    200 : {"model" : UserInDB , "description": "HTTP_200_OK",},
    403 : {"description": "HTTP_403_FORBIDDEN",},
    404 : {"description": "HTTP_404_NOT_FOUND",}
    })
async def update_user(
    user_id: Annotated[str , Depends(read_user_or_raise)],
    user_profile : Annotated[UserUpdateRequest, Body()]
) :
     user_dict = user_profile.model_dump()
     user_dict['_id'] = user_id
     user_in_db = UserInDB( **user_dict )
     user_in_db.is_verified = True
     log_in_user = await dm.user_repo.read_user(user_id=user_id)
     assert(log_in_user is not None)
     assert(log_in_user.id is not None)
     if log_in_user.phone_number != user_profile.phone_number:
         raise HTTPException(
             status_code= status.HTTP_403_FORBIDDEN,
             detail=TranslationKeys.PERMISSION_DENIED
         )
     user = await dm.user_repo.update_user( user=user_in_db)
     if user is None:
         raise HTTPException(
             status_code= status.HTTP_404_NOT_FOUND,
             detail=TranslationKeys.USER_NOT_FOUND
         )
     else:
        return JSONResponse(
            content=user.model_dump(by_alias=True,exclude={"verification_code", "hashed_password", "is_verified"})
        )


@router.put("/update_user_bio_data/",  responses={
    200 : {"model" : UserBioData, "description": "HTTP_200_OK",},
    400 : {"description": "HTTP_400_BAD_REQUEST",},
    })
async def update_user_bio_data(
    user_id: Annotated[str , Depends(read_user_or_raise)],
    user_bio_data : Annotated[UserBioDataUpsert, Body()]
) :
    try:
        bio_data = await dm.user_repo.upsert_user_bio_data(
            user_id = user_id,
            user_bio_data=user_bio_data
        )
        model_dump = bio_data.model_dump(by_alias=True)
        return JSONResponse(
            content=jsonable_encoder(model_dump)
        )

    except UserBioDataValidationError as e:
        message = TranslationKeys.INVALID_ARGUMENT
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= ErrorResponse(error_detail= 'TranslationKeys.INVALID_ARGUMENT', message=f'{message} : {e.detail}').model_dump()
        )

@router.delete("/delete_user_bio_data/",status_code=status.HTTP_204_NO_CONTENT, responses={
    204 : {"description": "HTTP_204_NO_CONTENT",},
    400 : {"description": "HTTP_400_BAD_REQUEST",},
    404 : {"description": "HTTP_404_NOT_FOUND",},
    })
async def delete_user_bio_data(
    user_id: Annotated[str, Depends(read_user_or_raise)],
    data_point_id: Annotated[str, Query()],
):
    try:   
        await dm.user_repo.delete_user_bio_data(user_id=user_id, data_point_id=data_point_id)
    except UserBioDataValidationError as e:
        message = TranslationKeys.INVALID_ARGUMENT
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= ErrorResponse(error_detail= 'TranslationKeys.INVALID_ARGUMENT', message=f'{message} : {e.detail}').model_dump()
        )
    except NotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ErrorResponse(error_detail='TranslationKeys.OBJECT_NOT_FOUND', message=TranslationKeys.OBJECT_NOT_FOUND).model_dump()
        )


@router.get("/read_user_bio_data/",  responses={
    200 : {"model" : UserBioData, "description": "HTTP_200_OK",},
    404 : {"description": "HTTP_404_NOT_FOUND",},
    })
async def read_user_bio_data(
    user_id: Annotated[str , Depends(read_user_or_raise)],
) :
    bio_data = await dm.user_repo.read_user_bio_data(
        user_id=user_id,
    )
    if bio_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= ErrorResponse(error_detail= 'TranslationKeys.OBJECT_NOT_FOUND', message=TranslationKeys.OBJECT_NOT_FOUND).model_dump()
        )
    model_dump = bio_data.model_dump(by_alias=True)
    return JSONResponse(
        content=jsonable_encoder(model_dump))


@router.get("/read_user_image_profile/",  responses={
    200 : {"model" : list[FileData], "description": "HTTP_200_OK",},
    })
async def read_user_profile_image(
    user_id: Annotated[str, Depends(read_user_or_raise)],
):
    profile_image_meta_data = await dm.user_files_repo.read_user_profile_image(
        user_id=user_id,
    )
    return JSONResponse(
        content=[jsonable_encoder(file.model_dump(by_alias=True)) for file in profile_image_meta_data]
    )


@router.get("/read_user_image_gallary/", responses={
    200 : {"model" : list[FileData], "description": "HTTP_200_OK",},
    })
async def read_user_image_gallary(
    user_id: Annotated[str , Depends(read_user_or_raise)],
    tags: Annotated[list[GallaryTag] , Query()],
) :
    images_gallary = await dm.user_files_repo.read_user_image_gallary(
        user_id=user_id,
        tags=tags
    )
    return JSONResponse(
        content=[jsonable_encoder(file.model_dump(by_alias=True)) for file in images_gallary]
    )

@router.post("/add_user_images/",  responses={
    200 : {"model" : list[FileData], "description": "HTTP_200_OK",},
    400 : {"description": "HTTP_400_BAD_REQUEST",},
    500 : {"description": "HTTP_500_INTERNAL_SERVER_ERROR",},
    })
async def add_user_image(
    user_id: Annotated[str, Depends(read_user_or_raise)],
    tag: Annotated[GallaryTag, Form()],
    image_gallary_files: list[UploadFile]
):    
    for image_gallary_file in image_gallary_files:
        if(image_gallary_file.content_type is not None):
            if image_gallary_file.content_type not in ['image/png', 'image/jpeg','image/jpg']:
                message = TranslationKeys.INVALID_UPLOAD_FILE_REQUEST
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=ErrorResponse(
                        error_detail='TranslationKeys.INVALID_UPLOAD_FILE_REQUEST',
                        message=f"{message}: Unsupported file type {image_gallary_file.content_type}"
                    ).model_dump()
                )
    if len(image_gallary_files) == 0:
        message = TranslationKeys.INVALID_UPLOAD_FILE_REQUEST

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = ErrorResponse(
                error_detail='TranslationKeys.INVALID_UPLOAD_FILE_REQUEST',
                message=message
            ).model_dump()
        )
    for image_gallary_file in image_gallary_files:
        if image_gallary_file.filename is None or image_gallary_file.size is None or image_gallary_file.content_type is None:
            message = TranslationKeys.INVALID_UPLOAD_FILE_REQUEST
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorResponse(
                    error_detail='TranslationKeys.INVALID_UPLOAD_FILE_REQUEST',
                    message=message
                ).model_dump()
            )

    # user_static_files = await dm.user_files_repo.read_user_static_files(user_id=user_id)
    # if user_static_files is None:
    
    upload_directory = f"{upload_directory_path}/user_{user_id}/"
    try:
        images_meta_data = await dm.user_files_repo.save_files_on_disk(user_id=user_id, tag = tag,image_gallary_files=image_gallary_files, upload_directory=upload_directory)
    except Exception as e:
        raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=ErrorResponse(
                        error_detail='TranslationKeys.FILE_UPLOAD_FAILED',
                        message=f'{TranslationKeys.FILE_UPLOAD_FAILED} : {str(e)}'
                    ).model_dump()
                )

    results = await dm.user_files_repo.upsert_user_files(user_files=images_meta_data)

    return JSONResponse(
        content=[jsonable_encoder(file.model_dump(by_alias=True)) for file in results]
    )

@router.post("/archive_user_images/", responses={
    200 : {"model" : ArchiveUserImagesResponse, "description": "HTTP_200_OK",},
    })
async def archive_user_images(
    user_id: Annotated[str, Depends(read_user_or_raise)],
    images_id: Annotated[list[str], Body()],
):
    updated_images_ids = await dm.user_files_repo.archive_images(images_id=images_id)
    return JSONResponse(
        content=ArchiveUserImagesResponse(
            updated_images_ids = updated_images_ids,
            images_id = images_id
        ).model_dump()
    )

