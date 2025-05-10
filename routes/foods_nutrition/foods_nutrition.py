
from datetime import datetime
from typing import Annotated, Any, Callable

from fastapi import  APIRouter, Body, Depends, Form, HTTPException, Query, UploadFile, status
from fastapi.responses import JSONResponse
from data.common_data_model.language import Language
from dependeny_manager import dm
from domain_models import  AudioMemeType, InvalidArgumentError,FailedPreconditionError,PermissionDeniedError, NotFoundError,InternalError, ServiceUnavailableError, DeadlineExceededError,ResourceExhaustedError, Food
from domain_models.response_model import ErrorResponse
from utility.decode_jwt_user_id import read_user_or_raise
from utility.translation_keys import TranslationKeys
from fastapi.encoders import jsonable_encoder

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
    language : Annotated[Language, Form()],
    prompt: UploadFile,
) :
    if prompt.filename is None or prompt.size is None or prompt.content_type is None:
        message = TranslationKeys.INVALID_UPLOAD_FILE_REQUEST
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorResponse(
                error_detail='TranslationKeys.INVALID_UPLOAD_FILE_REQUEST',
                message=message
            ).model_dump()

        )
    if prompt.content_type not in ['audio/aac', 'audio/mp3','audio/wav','audio/flac', 'audio/ogg', 'audio/aiff']:
        message = TranslationKeys.INVALID_UPLOAD_FILE_REQUEST
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorResponse(
                error_detail='TranslationKeys.INVALID_UPLOAD_FILE_REQUEST',
                message=f"{message}: Unsupported file type {prompt.content_type}"
            ).model_dump()
        )
    if prompt.size > 7 * 1024 * 1024:  # Restrict file size to 5 MB
        message = TranslationKeys.FILE_LIMIT_EXCEEDED.format(file_size_limit = 7 )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorResponse(
                error_detail='TranslationKeys.FILE_LIMIT_EXCEEDED',
                message=message
            ).model_dump()
        )

    prompt_bytes = await prompt.read()
    return await _handle_food_request(
        request =dm.food_nutrition_repo.read_foods_nutritions_by_voice,
        user_id=user_id,
        foods=prompt_bytes,
        meme_type=meme_type,
        language = language,
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
    return JSONResponse(
        content=[jsonable_encoder(food.model_dump(by_alias=True)) for food in foods]
    )

@router.post("/update_foods_nutritions/",responses={
    200 : {"model" : Food, "description": "HTTP_200_OK",},
    403 : {"description": "HTTP_403_FORBIDDEN"}
    })
async def update_foods_nutritions(
    user_id: Annotated[str , Depends(read_user_or_raise)],
    food: Annotated[Food , Body()],
) :
    if user_id != food.user_id:
        raise HTTPException(
            status_code= status.HTTP_403_FORBIDDEN,
            detail=TranslationKeys.PERMISSION_DENIED
        )
    update_food = await dm.food_nutrition_repo.update_user_food(food=food)
    return JSONResponse(
        content=jsonable_encoder(update_food.model_dump(by_alias=True))
    )

@router.delete("/delete_foods_nutritions/",status_code=status.HTTP_204_NO_CONTENT, responses={
    204 : {"description": "HTTP_204_NO_CONTENT",},
    404 : {"description": "HTTP_404_NOT_FOUND",},
    })
async def delete_foods_nutritions(
    user_id: Annotated[str , Depends(read_user_or_raise)],
    food_ids: Annotated[list[str] , Query()],
) :
    try:
        res = await dm.food_nutrition_repo.delete_user_foods(foods_ids=food_ids)
        print(res)
    except NotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ErrorResponse(error_detail='TranslationKeys.OBJECT_NOT_FOUND', message=f'{TranslationKeys.OBJECT_NOT_FOUND} missing_id: {e.args[0]}').model_dump()
        )


async def _handle_food_request(request: Callable[..., Any], **kwargs: Any) -> JSONResponse:
    try:
        foods = await request(**kwargs)    
        return JSONResponse(
            content=[jsonable_encoder(food.model_dump(by_alias=True)) for food in foods]
        )   
        
    except InvalidArgumentError :
        message = TranslationKeys.INVALID_ARGUMENT
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorResponse(
                error_detail='TranslationKeys.INVALID_ARGUMENT',
                message=message
            ).model_dump()
        )
    except FailedPreconditionError :
        message = TranslationKeys.FAILED_PRECONDITION
        raise HTTPException(
            status_code=status.HTTP_412_PRECONDITION_FAILED,
            detail=ErrorResponse(
                error_detail='TranslationKeys.FAILED_PRECONDITION',
                message=message
            ).model_dump()
        )
    except  PermissionDeniedError :
        message = TranslationKeys.PERMISSION_DENIED
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=ErrorResponse(
                error_detail='TranslationKeys.PERMISSION_DENIED',
                message=message
            ).model_dump()
        )
    except  NotFoundError :
        message = TranslationKeys.NOT_FOUND
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ErrorResponse(
                error_detail='TranslationKeys.NOT_FOUND',
                message=message
            ).model_dump()
        )
    except  InternalError :
        message = TranslationKeys.INTERNAL_ERROR
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=ErrorResponse(
                error_detail='TranslationKeys.INTERNAL_ERROR',
                message=message
            ).model_dump()
        )
    except  ServiceUnavailableError :
        message = TranslationKeys.SERVICE_UNAVAILABLE
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=ErrorResponse(
                error_detail='TranslationKeys.SERVICE_UNAVAILABLE',
                message=message
            ).model_dump()
        )
    except  DeadlineExceededError :
        message = TranslationKeys.DEADLINE_EXCEEDED
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail=ErrorResponse(
                error_detail='TranslationKeys.DEADLINE_EXCEEDED',
                message=message
            ).model_dump()
        )
    except  ResourceExhaustedError :
        message = TranslationKeys.RESOURCE_EXHAUSTED
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=ErrorResponse(
                error_detail='TranslationKeys.RESOURCE_EXHAUSTED',
                message=message
            ).model_dump()
        )
    except Exception :
        message = TranslationKeys.SERVICE_UNAVAILABLE
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=ErrorResponse(
                error_detail='TranslationKeys.SERVICE_UNAVAILABLE',
                message=message
            ).model_dump()
        )