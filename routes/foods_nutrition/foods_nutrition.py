
from datetime import datetime
from typing import Annotated, Any, Callable

from fastapi import  APIRouter, Body, Depends, Form, HTTPException, Query, UploadFile, status
from dependeny_manager import dm
from domain_models import ApiResponse, AudioMemeType, InvalidArgumentError,FailedPreconditionError,PermissionDeniedError, NotFoundError,InternalError, ServiceUnavailableError, DeadlineExceededError,ResourceExhaustedError, Food
from utility.decode_jwt_user_id import read_user_or_raise
from utility.translation_keys import TranslationKeys




router = APIRouter(
    prefix="/foods_nutrition",
    tags=["Foods Nutritions"],
    #TOdo add dependency
)

@router.post("/read_foods_nutritions_by_text/",responses={
    200 : {"model" : list[Food], "description": "HTTP_200_OK",},
    400 : {"description": "HTTP_400_BAD_REQUEST",},
    412 : {"description": "HTTP_412_PRECONDITION_FAILED",},
    403 : {"description": "HTTP_403_FORBIDDEN",},
    404 : {"description": "HTTP_404_NOT_FOUND",},
    500 : {"description": "HTTP_500_INTERNAL_SERVER_ERROR",},
    503 : {"description": "HTTP_503_SERVICE_UNAVAILABLE",},
    504 : {"description": "HTTP_504_GATEWAY_TIMEOUT",},
    429 : {"description": "HTTP_429_TOO_MANY_REQUESTS",},
    })
async def read_foods_nutritions_by_text(
    user_id: Annotated[str , Depends(read_user_or_raise)],
    prompt : Annotated[str , Body(max_length = 700)],
) :
    return await _handle_food_request(
        request =dm.food_nutrition_repo.read_foods_nutritions_by_text,
        user_id=user_id,
        foods=prompt
    )
        


@router.post("/read_foods_nutritions_by_voice/", responses={
    200 : {"model" : list[Food], "description": "HTTP_200_OK",},
    400 : {"description": "HTTP_400_BAD_REQUEST",},
    412 : {"description": "HTTP_412_PRECONDITION_FAILED",},
    403 : {"description": "HTTP_403_FORBIDDEN",},
    404 : {"description": "HTTP_404_NOT_FOUND",},
    500 : {"description": "HTTP_500_INTERNAL_SERVER_ERROR",},
    503 : {"description": "HTTP_503_SERVICE_UNAVAILABLE",},
    504 : {"description": "HTTP_504_GATEWAY_TIMEOUT",},
    429 : {"description": "HTTP_429_TOO_MANY_REQUESTS",},
    })
async def read_foods_nutritions_by_voice(
    user_id: Annotated[str , Depends(read_user_or_raise)],
    meme_type : Annotated[AudioMemeType, Form()],
    prompt: UploadFile
) :
    if prompt.filename is None or prompt.size is None or prompt.content_type is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ApiResponse.error(
                message='TranslationKeys.INVALID_UPLOAD_FILE_REQUEST',
                error_detail=TranslationKeys.INVALID_UPLOAD_FILE_REQUEST
            ).to_dict()
        )
    if prompt.size > 7 * 1024 * 1024:  # Restrict file size to 5 MB
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ApiResponse.error(
                message='TranslationKeys.INVALID_UPLOAD_FILE_REQUEST',
                error_detail=TranslationKeys.FILE_LIMIT_EXCEEDED.format(file_size_limit = 7 )
            ).to_dict()
        )

    prompt_bytes = await prompt.read()
    return await _handle_food_request(
        request =dm.food_nutrition_repo.read_foods_nutritions_by_voice,
        user_id=user_id,
        foods=prompt_bytes,
        meme_type=meme_type
    )

@router.get("/read_foods_nutritions/",responses={
    200 : {"model" : list[Food], "description": "HTTP_200_OK",},
    })
async def read_foods_nutritions(
    user_id: Annotated[str , Depends(read_user_or_raise)],
    start_date: Annotated[datetime , Query()],
    end_date: Annotated[datetime , Query()],
) :
    foods = await dm.food_nutrition_repo.read_foods_nutritions(user_id=user_id, start_date=start_date, end_date=end_date)
    return ApiResponse.success(
        data = [food.model_dump() for food in foods]
    ).to_dict()

@router.get("/update_foods_nutritions/",responses={
    200 : {"model" : list[Food], "description": "HTTP_200_OK",},
    403 : {"description": "HTTP_403_FORBIDDEN"}
    })
async def update_foods_nutritions(
    user_id: Annotated[str , Depends(read_user_or_raise)],
    food: Annotated[Food , Query()],
) :
    if user_id != food.user_id:
        raise HTTPException(
            status_code= status.HTTP_403_FORBIDDEN,
            detail=TranslationKeys.PERMISSION_DENIED
        )
    food = await dm.food_nutrition_repo.update_user_food(food=food)
    return ApiResponse.success(
        data = food.model_dump()
    ).to_dict()

@router.delete("/delete_foods_nutritions/",responses={
    200 : {"model" : list[str], "description": "HTTP_200_OK",}
    })
async def delete_foods_nutritions(
    user_id: Annotated[str , Depends(read_user_or_raise)],
    food_ids: Annotated[list[str] , Query()],
) :
    deleted_foods = await dm.food_nutrition_repo.delete_user_foods(foods_ids=food_ids)
    return ApiResponse.success(
        data = deleted_foods
    ).to_dict()


async def _handle_food_request(request: Callable[..., Any], **kwargs: Any):
    try:
        foods = await request(**kwargs)       
        return ApiResponse.success(
            data = foods.model_dump()
        ).to_dict()
    except InvalidArgumentError :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ApiResponse.error(
                message='TranslationKeys.INVALID_ARGUMENT',
                error_detail=TranslationKeys.INVALID_ARGUMENT
            ).to_dict()
        )
    except FailedPreconditionError :
        raise HTTPException(
            status_code=status.HTTP_412_PRECONDITION_FAILED,
            detail=ApiResponse.error(
                message='TranslationKeys.FAILED_PRECONDITION',
                error_detail=TranslationKeys.FAILED_PRECONDITION
            ).to_dict()
        )
    except  PermissionDeniedError :
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=ApiResponse.error(
                message='TranslationKeys.PERMISSION_DENIED',
                error_detail=TranslationKeys.PERMISSION_DENIED
            ).to_dict()
        )
    except  NotFoundError :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ApiResponse.error(
                message='TranslationKeys.NOT_FOUND',
                error_detail=TranslationKeys.NOT_FOUND
            ).to_dict()
        )
    except  InternalError :
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=ApiResponse.error(
                message='TranslationKeys.INTERNAL_ERROR',
                error_detail=TranslationKeys.INTERNAL_ERROR
            ).to_dict()
        )
    except  ServiceUnavailableError :
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=ApiResponse.error(
                message='TranslationKeys.SERVICE_UNAVAILABLE',
                error_detail=TranslationKeys.SERVICE_UNAVAILABLE
            ).to_dict()
        )
    except  DeadlineExceededError :
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail=ApiResponse.error(
                message='TranslationKeys.DEADLINE_EXCEEDED',
                error_detail=TranslationKeys.DEADLINE_EXCEEDED
            ).to_dict()
        )
    except  ResourceExhaustedError :
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=ApiResponse.error(
                message='TranslationKeys.RESOURCE_EXHAUSTED',
                error_detail=TranslationKeys.RESOURCE_EXHAUSTED
            ).to_dict()
        )
    except Exception :
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=ApiResponse.error(
                message='TranslationKeys.SERVICE_UNAVAILABLE',
                error_detail=TranslationKeys.SERVICE_UNAVAILABLE
            ).to_dict()
        )