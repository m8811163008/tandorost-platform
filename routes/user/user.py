
from datetime import datetime
from typing import Annotated

from fastapi import  APIRouter, Body, Depends, Form, HTTPException, Query, UploadFile, status
from dependeny_manager import dm
from domain_models import ApiResponse, UserUpdateRequest, UserBioDataRequest,UserBioData,UserInDB,GallaryTag,UserStaticFiles, FileMetaData

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
     user_in_db.is_verified = True
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
    profile_image_meta_data = await dm.user_files_repo.read_user_profile_image(
        user_id=user_id,
    )
    if profile_image_meta_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= ApiResponse.error(message= 'TranslationKeys.OBJECT_NOT_FOUND', error_detail=TranslationKeys.OBJECT_NOT_FOUND).to_dict()
        )
    return ApiResponse.success(
                data = profile_image_meta_data
            ).to_dict()

@router.get("/read_user_image_gallary/")
async def read_user_image_gallary(
    user_id: Annotated[str , Depends(read_user_or_raise)],
    tags: Annotated[list[GallaryTag] , Query()],
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

@router.put("/add_user_images/", description='profile image or image gallary files should not be None at same time')
async def add_user_images(
    user_id: Annotated[str, Depends(read_user_or_raise)],
    tag: Annotated[GallaryTag, Form()],
    image_gallary_files: list[UploadFile]
):
    if len(image_gallary_files) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ApiResponse.error(
                message='TranslationKeys.INVALID_UPLOAD_FILE_REQUEST',
                error_detail=TranslationKeys.INVALID_UPLOAD_FILE_REQUEST
            ).to_dict()
        )

    user_static_files = await dm.user_files_repo.read_user_static_files(user_id=user_id)
    if user_static_files is None:
        user_static_files = UserStaticFiles(user_id=user_id, image_gallery={})

    # Use this naming format for storing on the system: {user_id}_{upload_date_iso_format}_{original_filename}
    # Save file on the system for each user in /user_{user_id}/uploads/
    upload_date_time = datetime.now()
    images_meta_data: list[FileMetaData] = []

    for image_gallary_file in image_gallary_files:
        if image_gallary_file.filename is None or image_gallary_file.size is None or image_gallary_file.content_type is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ApiResponse.error(
                    message='TranslationKeys.INVALID_UPLOAD_FILE_REQUEST',
                    error_detail=TranslationKeys.INVALID_UPLOAD_FILE_REQUEST
                ).to_dict()
            )

        # Define the file upload path
        upload_directory = f"user_{user_id}/uploads/"
        file_upload_path = f"{upload_directory}{user_id}_{upload_date_time.isoformat()}_{image_gallary_file.filename}"

        # Save the file to the system
        try:
            with open(file_upload_path, "wb") as file:
                content = await image_gallary_file.read()
                file.write(content)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=ApiResponse.error(
                    message='TranslationKeys.FILE_UPLOAD_FAILED',
                    error_detail=str(e)
                ).to_dict()
            )

        # Create metadata for the uploaded file
        meta_data = FileMetaData(
            file_name=image_gallary_file.filename,
            file_size=image_gallary_file.size,
            upload_date=upload_date_time,
            content_type=image_gallary_file.content_type,
            file_upload_path=file_upload_path,
        )
        images_meta_data.append(meta_data)

    if user_static_files.image_gallery.get(tag) is None:
        user_static_files.image_gallery[tag] = []
    user_static_files.image_gallery[tag].extend(images_meta_data)

    result = await dm.user_files_repo.upsert_user_files(user_files=user_static_files)

    return ApiResponse.success(
        data=result.model_dump()
    ).to_dict()



    
