
from typing import Annotated

from fastapi import  APIRouter, Body, Depends, HTTPException, status
from data.local_database.model.pydantic_object_id import ObjectId
from data.local_database.model.user import UserInDB
from dependeny_manager import dm
from domain_models.response_model import ApiResponse
from utility.decode_jwt_user_id import jwt_user_id
from utility.translation_keys import TranslationKeys


router = APIRouter(
    prefix="/user",
    tags=["User"],
)

@router.get("/user_profile/")
async def read_user(
    user_id: Annotated[ObjectId , Depends(jwt_user_id)],
) :
     user = await dm.user_repo.read_user(user_id=user_id)
     if user is None:
         raise HTTPException(
             status_code= status.HTTP_404_NOT_FOUND,
             detail=TranslationKeys.USER_NOT_FOUND
         )
     else:
         return ApiResponse.success(
             data = user.model_dump(exclude={
                 "hashed_password",
                 "verification_code",
             })
         ).to_dict()

@router.put("/update_profile/")
async def update_user(
    user_id: Annotated[ObjectId , Depends(jwt_user_id)],
    user_profile : Annotated[UserInDB, Body()]
) :
     user = await dm.user_repo.update_user(user_id=user_id, user=user_profile, exclude={ "hashed_password", "verification_code", "is_verified"})
     if user is None:
         raise HTTPException(
             status_code= status.HTTP_404_NOT_FOUND,
             detail=TranslationKeys.USER_NOT_FOUND
         )
     else:
         return ApiResponse.success(
             data = user.model_dump(exclude={
                 "hashed_password",
                 "verification_code",
             })
         ).to_dict()


# @app.get("/users/me/items/")
# async def read_own_items(
#     current_user: Annotated[User, Depends(get_current_active_user)],
# ):
#     return [{"item_id": "Foo", "owner": current_user.username}]
