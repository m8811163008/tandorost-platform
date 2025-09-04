

from datetime import datetime
from typing import Annotated

from fastapi import  APIRouter, Body, Depends, Form, HTTPException, Query, UploadFile, status
from fastapi.responses import JSONResponse
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
        content=user.model_dump(exclude={"verification_code", "hashed_password", "is_phone_number_verified", "is_email_verified"})
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
     updated_profile = UserInDB( **user_dict )

     log_in_user = await dm.user_repo.read_user(user_id=user_id)
     assert(log_in_user is not None)
     assert(log_in_user.id is not None)
     updated_profile.is_phone_number_verified = log_in_user.is_phone_number_verified
     updated_profile.is_email_verified = log_in_user.is_email_verified

     user = await dm.user_repo.update_user( user=updated_profile)
     if user is None:
         raise HTTPException(
             status_code= status.HTTP_404_NOT_FOUND,
             detail=TranslationKeys.USER_NOT_FOUND
         )
     else:
        return JSONResponse(
            content=user.model_dump(exclude={"verification_code", "hashed_password", "is_phone_number_verified", "is_email_verified"})
        )


@router.put("/update_user_physical_data/",  responses={
    200 : {"model" : UserPhysicalData, "description": "HTTP_200_OK",},
    400 : {"description": "HTTP_400_BAD_REQUEST",},
    })
async def update_user_physical_data(
    user_id: Annotated[str , Depends(read_user_or_raise)],
    user_physical_data : Annotated[UserPhysicalDataUpsert, Body()]
) :
    try:
        physical_data = await dm.user_repo.upsert_user_physical_data(
            user_id = user_id,
            user_physical_data=user_physical_data
        )
        model_dump = physical_data.model_dump()
        return JSONResponse(
            content=jsonable_encoder(model_dump)
        )

    except UserPhysicalDataValidationError as e:
        message = TranslationKeys.INVALID_ARGUMENT
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= ErrorResponse(error_detail= 'TranslationKeys.INVALID_ARGUMENT', message=f'{message} : {e.detail}').model_dump()
        )

@router.delete("/delete_user_physical_data/",status_code=status.HTTP_204_NO_CONTENT, responses={
    204 : {"description": "HTTP_204_NO_CONTENT",},
    400 : {"description": "HTTP_400_BAD_REQUEST",},
    404 : {"description": "HTTP_404_NOT_FOUND",},
    })
async def delete_user_physical_data(
    user_id: Annotated[str, Depends(read_user_or_raise)],
    data_point_id: Annotated[str, Query()],
):
    try:   
        await dm.user_repo.delete_user_physical_data(user_id=user_id, data_point_id=data_point_id)
    except UserPhysicalDataValidationError as e:
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


@router.get("/read_user_physical_data/",  responses={
    200 : {"model" : UserPhysicalData, "description": "HTTP_200_OK",},
    404 : {"description": "HTTP_404_NOT_FOUND",},
    })
async def read_user_physical_data(
    user_id: Annotated[str , Depends(read_user_or_raise)],
) :
    physical_data = await dm.user_repo.read_user_physical_data(
        user_id=user_id,
    )
    if physical_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= ErrorResponse(error_detail= 'TranslationKeys.OBJECT_NOT_FOUND', message=TranslationKeys.OBJECT_NOT_FOUND).model_dump()
        )
    model_dump = physical_data.model_dump()
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
        content=[jsonable_encoder(file.model_dump()) for file in profile_image_meta_data]
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
        content=[jsonable_encoder(file.model_dump()) for file in images_gallary]
    )

@router.post("/add_user_images/",  responses={
    200 : {"model" : list[FileData], "description": "HTTP_200_OK",},
    400 : {"description": "HTTP_400_BAD_REQUEST",},
    500 : {"description": "HTTP_500_INTERNAL_SERVER_ERROR",},
    })
async def add_user_image(
    user_id: Annotated[str, Depends(read_user_or_raise)],
    tag: Annotated[GallaryTag, Form()],
    image_gallary_files: list[UploadFile],
    upload_date: Annotated[datetime | None, Form()] = None,
    description : Annotated[str | None, Form()] = None,
):    
    for image_gallary_file in image_gallary_files:
        if(image_gallary_file.content_type is not None):
            if image_gallary_file.content_type not in ['image/png', 'image/jpeg','image/jpg','image/webp', 'image/heic', 'image/heif' ]:
                #image/heic or image/heif: For HEIC/HEIF images, commonly used on iOS devices.
                #image/webp: For WebP images, supported on modern browsers and Android.
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
        images_meta_data = await dm.user_files_repo.save_files_on_disk(user_id=user_id, tag = tag,image_gallary_files=image_gallary_files,upload_date = upload_date, upload_directory=upload_directory, description=description)
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
        content=[jsonable_encoder(file.model_dump()) for file in results]
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

