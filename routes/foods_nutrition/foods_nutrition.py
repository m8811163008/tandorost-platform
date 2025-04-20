
from typing import Annotated

from fastapi import  APIRouter, Body, Depends, Form, UploadFile
from dependeny_manager import dm
from domain_models import ApiResponse, AudioMemeType
from utility.decode_jwt_user_id import read_user_or_raise




router = APIRouter(
    prefix="/foods_nutrition",
    tags=["Foods Nutritions"],
    #TOdo add dependency
)



@router.post("/read_foods_nutritions_by_text/")
async def read_foods_nutritions_by_text(
    user_id: Annotated[str , Depends(read_user_or_raise)],
    prompt : Annotated[str , Body(max_length = 700)],
) :
    foods = await dm.food_nutrition_repo.read_foods_nutritions_by_text(foods=prompt)
    
    return ApiResponse.success(
        data = foods.model_dump()
    ).to_dict()


@router.post("/read_foods_nutritions_by_voice/")
async def read_foods_nutritions_by_voice(
    user_id: Annotated[str , Depends(read_user_or_raise)],
    meme_type : Annotated[AudioMemeType, Form()],
    prompt: UploadFile
) :
    prompt_bytes = await prompt.read()
    foods = await dm.food_nutrition_repo.read_foods_nutritions_by_voice(foods=prompt_bytes, meme_type=meme_type)
    
    return ApiResponse.success(
        data = foods.model_dump()
    ).to_dict()



