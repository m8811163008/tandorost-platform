
from typing import Annotated

from fastapi import  APIRouter, Body, Depends
from dependeny_manager import dm

from utility.decode_jwt_user_id import read_user_or_raise




router = APIRouter(
    prefix="/foods_nutrition",
    tags=["Foods Nutritions"],
    #TOdo add dependency
)



@router.post("/read_foods_nutritions_by_text/")
async def read_foods_nutritions_by_text(
    user_id: Annotated[str , Depends(read_user_or_raise)],
    prompt : Annotated[str , Body()],
) :
    await dm.food_nutrition_repo.read_foods_nutritions_by_text(foods=prompt)
    
    # return ApiResponse.success(
    #     data = user.model_dump(exclude={"verification_code", "hashed_password"})
    # ).to_dict()

