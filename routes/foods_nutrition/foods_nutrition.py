
from typing import Annotated, Any, Callable

from fastapi import  APIRouter, Body, Depends, Form, HTTPException, UploadFile, status
from dependeny_manager import dm
from domain_models import ApiResponse, AudioMemeType, InvalidArgumentError,FailedPreconditionError,PermissionDeniedError, NotFoundError,InternalError, ServiceUnavailableError, DeadlineExceededError,ResourceExhaustedError
from utility.decode_jwt_user_id import read_user_or_raise
from utility.translation_keys import TranslationKeys




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
    return await _handle_food_request(
        request =dm.food_nutrition_repo.read_foods_nutritions_by_text,
        user_id=user_id,
        foods=prompt
    )
        


@router.post("/read_foods_nutritions_by_voice/")
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
        request =dm.food_nutrition_repo.read_foods_nutritions_by_text,
        user_id=user_id,
        foods=prompt_bytes,
        meme_type=meme_type
    )


async def _handle_food_request(request: Callable[..., Any], **kwargs: Any):
    try:
        foods = await request(**kwargs)       
        return ApiResponse.success(
            data = foods.model_dump()
        ).to_dict()
    except InvalidArgumentError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ApiResponse.error(
                message='TranslationKeys.INVALID_ARGUMENT',
                error_detail=TranslationKeys.INVALID_ARGUMENT
            ).to_dict()
        )
    except FailedPreconditionError as e:
        raise HTTPException(
            status_code=status.HTTP_412_PRECONDITION_FAILED,
            detail=ApiResponse.error(
                message='TranslationKeys.FAILED_PRECONDITION',
                error_detail=TranslationKeys.FAILED_PRECONDITION
            ).to_dict()
        )
    except  PermissionDeniedError as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=ApiResponse.error(
                message='TranslationKeys.PERMISSION_DENIED',
                error_detail=TranslationKeys.PERMISSION_DENIED
            ).to_dict()
        )
    except  NotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ApiResponse.error(
                message='TranslationKeys.NOT_FOUND',
                error_detail=TranslationKeys.NOT_FOUND
            ).to_dict()
        )
    except  InternalError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=ApiResponse.error(
                message='TranslationKeys.INTERNAL_ERROR',
                error_detail=TranslationKeys.INTERNAL_ERROR
            ).to_dict()
        )
    except  ServiceUnavailableError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=ApiResponse.error(
                message='TranslationKeys.SERVICE_UNAVAILABLE',
                error_detail=TranslationKeys.SERVICE_UNAVAILABLE
            ).to_dict()
        )
    except  DeadlineExceededError as e:
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail=ApiResponse.error(
                message='TranslationKeys.DEADLINE_EXCEEDED',
                error_detail=TranslationKeys.DEADLINE_EXCEEDED
            ).to_dict()
        )
    except  ResourceExhaustedError as e:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=ApiResponse.error(
                message='TranslationKeys.RESOURCE_EXHAUSTED',
                error_detail=TranslationKeys.RESOURCE_EXHAUSTED
            ).to_dict()
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=ApiResponse.error(
                message='TranslationKeys.SERVICE_UNAVAILABLE',
                error_detail=TranslationKeys.SERVICE_UNAVAILABLE
            ).to_dict()
        )