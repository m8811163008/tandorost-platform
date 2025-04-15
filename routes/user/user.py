
from typing import Annotated

from fastapi import  APIRouter, Body, Depends, HTTPException, status
from data.local_database.model.user import UserInDB
from data.local_database.model.user_bio_data import UserBioData
from dependeny_manager import dm
from domain_models import ApiResponse, UserUpdateRequest, UserBioDataRequest
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

# @app.get("/users/me/items/")
# async def read_own_items(
#     current_user: Annotated[User, Depends(get_current_active_user)],
# ):
#     return [{"item_id": "Foo", "owner": current_user.username}]
