

from typing import Annotated

from fastapi import  APIRouter, Depends, HTTPException, Security, status
from fastapi.responses import JSONResponse

from dependeny_manager import dm

from domain_models.fitness_data import FitnessData
from domain_models.nutrition_requrement import NutritionRequerments
from domain_models.response_model import ErrorResponse
from utility.decode_jwt_user_id import read_user_or_raise
from utility.translation_keys import TranslationKeys
from fastapi.encoders import jsonable_encoder

router = APIRouter(
    prefix="/fitness",
    tags=["Fitness Data"],
)


@router.get("/fitness_data/",responses={
    200 : {"model" : FitnessData, "description": "HTTP_200_OK",},
    404 : {"description": "HTTP_404_NOT_FOUND",},
    })
async def fitness_data(
    user_id: Annotated[str , Depends(read_user_or_raise)],
) :
    fitness_data = await dm.fitness_repo.fitness_data(user_id=user_id)
    if fitness_data is None:
        message = TranslationKeys.NOT_FOUND
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ErrorResponse(
                error_detail='TranslationKeys.NOT_FOUND',
                message=message
            ).model_dump()
        )
    return JSONResponse(
        content= jsonable_encoder(fitness_data.model_dump())
    )


@router.get("/athlete_fitness_data/",responses={
    200 : {"model" : FitnessData, "description": "HTTP_200_OK",},
    404 : {"description": "HTTP_404_NOT_FOUND",},
    })
async def athlete_fitness_data(
    user_id: Annotated[str , Security(read_user_or_raise, scopes=["coach"])],
    athlete_user_id: str,
) :
    fitness_data = await dm.fitness_repo.fitness_data(user_id=athlete_user_id)
    if fitness_data is None:
        message = TranslationKeys.NOT_FOUND
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ErrorResponse(
                error_detail='TranslationKeys.NOT_FOUND',
                message=message
            ).model_dump()
        )
    return JSONResponse(
        content= jsonable_encoder(fitness_data.model_dump())
    )

@router.get("/nutrition_requerment_data/",responses={
    200 : {"model" : NutritionRequerments, "description": "HTTP_200_OK",},
    404 : {"description": "HTTP_404_NOT_FOUND",},
    })
async def nutrition_requerment_data(
    user_id: Annotated[str , Depends(read_user_or_raise)],
) :
    nutrition_requerment_data = await dm.fitness_repo.nutrition_requerment_data(user_id=user_id)
    if nutrition_requerment_data is None:
        message = TranslationKeys.NOT_FOUND
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ErrorResponse(
                error_detail='TranslationKeys.NOT_FOUND',
                message=message
            ).model_dump()
        )
    return JSONResponse(
        content= jsonable_encoder(nutrition_requerment_data.model_dump())
    )
