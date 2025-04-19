
from typing import Annotated

from fastapi import  APIRouter, Body, Depends, Form, HTTPException, Query, UploadFile, status
from dependeny_manager import dm
from domain_models import ApiResponse, UserUpdateRequest, UserBioDataRequest,UserBioData,UserInDB,GallaryTag,UserStaticFiles, ArchiveUserImagesResponse

from utility.decode_jwt_user_id import read_user_or_raise
from utility.translation_keys import TranslationKeys
from utility.constants import upload_directory_path



router = APIRouter(
    prefix="/foods_nutrition",
    tags=["Foods Nutritions"],
    #TOdo add dependency
)



@router.post("/read_foods_nutritions_by_text/")
async def read_foods_nutritions_by_text(
    user_id: Annotated[str , Depends(read_user_or_raise)],
    prompt : str
) -> list[Food]:
    user = await dm.user_repo.read_user(user_id=user_id)
    assert(user is not None)
    return ApiResponse.success(
        data = user.model_dump(exclude={"verification_code", "hashed_password"})
    ).to_dict()

