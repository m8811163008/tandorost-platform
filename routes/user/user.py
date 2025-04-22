
from typing import Annotated

from fastapi import  APIRouter, Body, Depends, Form, HTTPException, Query, UploadFile, status
from dependeny_manager import dm
from domain_models import ApiResponse, UserUpdateRequest, UserBioDataUpsert,UserInDB,GallaryTag, ArchiveUserImagesResponse,InvalidUserBioDataUpsert

from utility.decode_jwt_user_id import read_user_or_raise
from utility.translation_keys import TranslationKeys
from utility.constants import upload_directory_path



router = APIRouter(
    prefix="/user",
    tags=["User"],
    #TOdo add dependency
)



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
         return ApiResponse.success(
             data = user.model_dump(exclude={"verification_code", "hashed_password"})
         ).to_dict()


@router.put("/update_user_bio_data/")
async def update_user_bio_data(
    user_id: Annotated[str , Depends(read_user_or_raise)],
    user_bio_data : Annotated[UserBioDataUpsert, Body()]
) :
    try:
        bio_data = await dm.user_repo.upsert_user_bio_data(
            user_id = user_id,
            user_bio_data=user_bio_data
        )
        return ApiResponse.success(
                    data = bio_data.model_dump()
                ).to_dict()
    except InvalidUserBioDataUpsert as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= ApiResponse.error(message= 'InvalidUserBioDataUpsert', error_detail=e.detail).to_dict()
        )


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
    user_id: Annotated[str, Depends(read_user_or_raise)],
):
    profile_image_meta_data = await dm.user_files_repo.read_user_profile_image(
        user_id=user_id,
    )
    
    return ApiResponse.success(
        data=[file.model_dump() for file in profile_image_meta_data]
    ).to_dict()

@router.get("/read_user_image_gallary/")
async def read_user_image_gallary(
    user_id: Annotated[str , Depends(read_user_or_raise)],
    tags: Annotated[list[GallaryTag] , Query()],
) :
    images_gallary = await dm.user_files_repo.read_user_image_gallary(
        user_id=user_id,
        tags=tags
    )
    return ApiResponse.success(
                data = [image_gallary.model_dump() for image_gallary in images_gallary]
            ).to_dict()

@router.post("/add_user_images/")
async def add_user_image(
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
    for image_gallary_file in image_gallary_files:
        if image_gallary_file.filename is None or image_gallary_file.size is None or image_gallary_file.content_type is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ApiResponse.error(
                    message='TranslationKeys.INVALID_UPLOAD_FILE_REQUEST',
                    error_detail=TranslationKeys.INVALID_UPLOAD_FILE_REQUEST
                ).to_dict()
            )

    # user_static_files = await dm.user_files_repo.read_user_static_files(user_id=user_id)
    # if user_static_files is None:
    
    upload_directory = f"{upload_directory_path}/user_{user_id}/"
    try:
        images_meta_data = await dm.user_files_repo.save_files_on_disk(user_id=user_id, tag = tag,image_gallary_files=image_gallary_files, upload_directory=upload_directory)
    except Exception as e:
        raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=ApiResponse.error(
                        message='TranslationKeys.FILE_UPLOAD_FAILED',
                        error_detail=str(e)
                    ).to_dict()
                )

    results = await dm.user_files_repo.upsert_user_files(user_files=images_meta_data)

    return ApiResponse.success(
        data = [result.model_dump() for result in results ]
    ).to_dict()

@router.post("/archive_user_images/")
async def archive_user_images(
    user_id: Annotated[str, Depends(read_user_or_raise)],
    images_id: Annotated[list[str], Body()],
):
    updated_images_ids = await dm.user_files_repo.archive_images(images_id=images_id)

    return ApiResponse.success(
        data=ArchiveUserImagesResponse(
            updated_images_ids = updated_images_ids,
            images_id = images_id
        ).model_dump()
    ).to_dict()
