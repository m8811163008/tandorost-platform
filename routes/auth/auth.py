from fastapi import APIRouter, Body, Form, Query, Security, UploadFile
from fastapi.responses import JSONResponse
from data.common_data_model.language import Language

from data.remote_api.model.exceptions import DeadlineExceededError, FailedPreconditionError, InternalError, InvalidArgumentError, NotFoundError, PermissionDeniedError, ResourceExhaustedError, ServiceUnavailableError
from domain_models import (GallaryTag , InvalidPassword, InvalidVerificationCode, UsernameAlreadyInUse, UsernameIsInactive, UsernameNotRegisteredYet, VerifiationCodeRequestReachedLimit, NetworkConnectionError ,VerificationType, Token, Currency, PaymentMethod, SubscriptionType,
                           UserInDbSubscriptionPayment,
                           VerifyRejection
                           )
from fastapi.security import  OAuth2PasswordRequestForm
from typing import Annotated
from datetime import datetime, timezone
from fastapi import Depends, HTTPException, status
from domain_models.response_model import ErrorResponse
# from repositories.auth import 
from utility import (
    EnvirenmentVariable,
    check_verify_rate_limit,
    TranslationKeys,
    translation_manager
)
from dependeny_manager import dm
from utility.constants import rate_limit_second
from utility.decode_jwt_user_id import read_user_or_raise
from google.oauth2 import id_token
from google.auth.transport import requests
from domain_models import UsernameType, username_type, Referral


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

GOOGLE_CLIENT_ID = "1050674706678-b6mpufv8njbec0gp4jf6ie9oj7oncb1b.apps.googleusercontent.com"

@router.post("/send_verification_code/", responses={
    200 : {"model" : None, "description": "HTTP_200_OK",},
    429 : {"description": "HTTP_429_TOO_MANY_REQUESTS",},
    404 : {"description": "HTTP_404_NOT_FOUND",},
    409 : {"description": "HTTP_409_CONFLICT",},
    503 : {"description": "HTTP_503_SERVICE_UNAVAILABLE",},
    })
async def send_verification_code(
    identifier : Annotated[str, Form(pattern=r"(^09\d{9}$)|(^[^@]+@[^@]+\.[^@]+$)")],
    verification_type : VerificationType
):  
    try:
        await check_verify_rate_limit(identifier=identifier, rate_limit_second=rate_limit_second)
    except VerifiationCodeRequestReachedLimit as e:
        message = translation_manager.gettext(TranslationKeys.RATE_LIMIT_REACH).format(second= e.seconds_left)
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail= ErrorResponse(error_detail='TranslationKeys.RATE_LIMIT_REACH', message=message).model_dump()
        )
 
    try:
        await dm.auth_repo.save_verification_code(identifier=identifier, verification_type = verification_type)
        
    except UsernameNotRegisteredYet:
        message = translation_manager.gettext(TranslationKeys.USERNAME_NOT_REGISTERED_YET)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= ErrorResponse(error_detail='TranslationKeys.USERNAME_NOT_REGISTERED_YET', message=message).model_dump()
        )
    except UsernameAlreadyInUse:
        message = translation_manager.gettext(TranslationKeys.USERNAME_IN_USE).format(user_name=identifier)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail= ErrorResponse(error_detail='TranslationKeys.USERNAME_IN_USE', message=message).model_dump()
        )

    user_type = username_type(username=identifier)
    if user_type == UsernameType.PHONENUMBER:
        try:
            await dm.auth_repo.send_sms_verification_code(username=identifier)
        except NetworkConnectionError: 
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail= ErrorResponse(error_detail='TranslationKeys.REMOTE_SERVICE_UNAVAILABLE', message=translation_manager.gettext(TranslationKeys.REMOTE_SERVICE_UNAVAILABLE)).model_dump()
            )
    if user_type == UsernameType.EMAIL:
        try:
            subject = translation_manager.gettext(TranslationKeys.VERIFICATION_EMAIL_SUBJECT)
            body = translation_manager.gettext(TranslationKeys.VERIFICATION_EMAIL_BODY)
            await dm.auth_repo.send_email_verification_code(username=identifier, subject =subject, body = body)
        except NetworkConnectionError: 
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail= ErrorResponse(error_detail='TranslationKeys.REMOTE_SERVICE_UNAVAILABLE', message=translation_manager.gettext(TranslationKeys.REMOTE_SERVICE_UNAVAILABLE)).model_dump()
            )
    return JSONResponse(content=translation_manager.gettext(TranslationKeys.VERIFICATION_CODE_SEND))
    

@router.post("/verify_verification_code/", responses={
    204 : {"description": "HTTP_204_NO_CONTENT",},
    401 : {"description": "HTTP_401_UNAUTHORIZED",},
    404 : {"description": "HTTP_404_NOT_FOUND",},
    409 : {"description": "HTTP_409_CONFLICT",},
    503 : {"description": "HTTP_503_SERVICE_UNAVAILABLE",},
    }, status_code=status.HTTP_204_NO_CONTENT)
async def verify_verification_code(
    identifier : Annotated[str, Form(pattern=r"(^09\d{9}$)|(^[^@]+@[^@]+\.[^@]+$)")],
    verification_code : Annotated[str, Form(min_length=4, max_length=4, pattern=r"^\d{4}$")],
):  
    
    try:
        await dm.auth_repo.verify_code(username=identifier,verification_code = verification_code)

    except UsernameNotRegisteredYet :
        message = translation_manager.gettext(TranslationKeys.USERNAME_NOT_REGISTERED_YET)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= ErrorResponse(error_detail='TranslationKeys.USERNAME_NOT_REGISTERED_YET', message=message).model_dump()
        )
    except UsernameAlreadyInUse : 
        message = translation_manager.gettext(TranslationKeys.USERNAME_IN_USE).format(user_name=identifier)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail= ErrorResponse(error_detail='TranslationKeys.USERNAME_IN_USE', message=message).model_dump()
        )
    except InvalidVerificationCode:
        message = translation_manager.gettext(TranslationKeys.INVALID_VERIFICATION_CODE)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = ErrorResponse(error_detail='TranslationKeys.INVALID_VERIFICATION_CODE', message=message).model_dump()
        )    

    
@router.post("/register/", responses={
    200 : {"model" : None, "description": "HTTP_200_OK",},
    404 : {"description": "HTTP_404_NOT_FOUND",},
    409 : {"description": "HTTP_409_CONFLICT",},
    401 : {"description": "HTTP_401_UNAUTHORIZED",},
    })
async def register(
    identifier: Annotated[str, Form(pattern=r"(^09\d{9}$)|(^[^@]+@[^@]+\.[^@]+$)")],
    password : Annotated[str, Form(min_length=4)],
    verification_code : Annotated[str, Form(min_length=4, max_length=4, pattern=r"^\d{4}$")],
):
    try:
        await dm.auth_repo.verify_code(username=identifier,verification_code = verification_code)

    except UsernameNotRegisteredYet :
        message = translation_manager.gettext(TranslationKeys.USERNAME_NOT_REGISTERED_YET)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= ErrorResponse(error_detail='TranslationKeys.USERNAME_NOT_REGISTERED_YET', message=message).model_dump()
        )
    except UsernameAlreadyInUse : 
        message = translation_manager.gettext(TranslationKeys.USERNAME_IN_USE).format(user_name=identifier)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail= ErrorResponse(error_detail='TranslationKeys.USERNAME_IN_USE', message=message).model_dump()
        )
    except InvalidVerificationCode:
        message = translation_manager.gettext(TranslationKeys.INVALID_VERIFICATION_CODE)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = ErrorResponse(error_detail='TranslationKeys.INVALID_VERIFICATION_CODE', message=message).model_dump()
        )
    upserted_user = await dm.auth_repo.update_user_account(password=password,username=identifier)
    assert(upserted_user.id != None)
    await createFreeSubscription(user_id=upserted_user.id)
    await dm.user_repo.update_referral_when_register(invite_contact=identifier, invited_user_id=upserted_user.id)
    return JSONResponse(content=translation_manager.gettext(TranslationKeys.USER_REGISTERED))

async def createFreeSubscription(user_id : str, ):
    subscription_data = UserInDbSubscriptionPayment(
        subscriber_user_id = user_id,
        paid_amount = 0,
        discount_amount= 0,
        currency = Currency.IRRIAL,
        payment_method=PaymentMethod.INPAYMENTCAFEBAZZAR,
        purchase_date = datetime.now(timezone.utc),
        subscription_type= SubscriptionType.FREETIER
    )
    await dm.payment_repo.create_payment_subscription(subscription_data=subscription_data)
    

@router.post("/forgot_password/", responses={
    200 : {"model" : None, "description": "HTTP_200_OK",},
    404 : {"description": "HTTP_404_NOT_FOUND",},
    409 : {"description": "HTTP_409_CONFLICT",},
    })
async def forgot_password(
    identifier: Annotated[str, Form(pattern=r"(^09\d{9}$)|(^[^@]+@[^@]+\.[^@]+$)")],
    new_password : Annotated[str, Form(min_length=4)],
    verification_code : Annotated[str, Form(min_length=4, max_length=4, pattern=r"^\d{4}$")],
):
    try:
        await dm.auth_repo.verify_code(username=identifier,verification_code = verification_code, is_register_request=False)
    except UsernameNotRegisteredYet :
        message = translation_manager.gettext(TranslationKeys.USERNAME_NOT_REGISTERED_YET)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = ErrorResponse(error_detail='TranslationKeys.USERNAME_NOT_REGISTERED_YET', message=message).model_dump()
        )
    except InvalidVerificationCode:
        message = translation_manager.gettext(TranslationKeys.INVALID_VERIFICATION_CODE)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = ErrorResponse(error_detail='TranslationKeys.INVALID_VERIFICATION_CODE', message=message).model_dump()
        )    

    await dm.auth_repo.update_user_account(password=new_password,username=identifier)
    return JSONResponse(content=translation_manager.gettext(TranslationKeys.PASSWORD_RESTORED))
    


@router.post("/token/", responses={
    200 : {"model" : Token, "description": "HTTP_200_OK",},
    403 : {"description": "HTTP_403_FORBIDDEN",},
    404 : {"description": "HTTP_404_NOT_FOUND",},
    401 : {"description": "HTTP_401_UNAUTHORIZED",},
    })
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    try:
        await dm.auth_repo.authenticate(username=form_data.username, password=form_data.password)
    except UsernameNotRegisteredYet:
        message = translation_manager.gettext(TranslationKeys.USERNAME_NOT_REGISTERED_YET)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=ErrorResponse(error_detail='TranslationKeys.USERNAME_NOT_REGISTERED_YET', message=message).model_dump()
        )
    except UsernameIsInactive:
        message = translation_manager.gettext(TranslationKeys.USERNAME_IS_INACTIVE)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail = ErrorResponse(error_detail='TranslationKeys.USERNAME_IS_INACTIVE', message=message).model_dump()
        )
    except InvalidPassword:
        message = translation_manager.gettext(TranslationKeys.INVALID_PASSWORD)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = ErrorResponse(error_detail='TranslationKeys.INVALID_PASSWORD', message=message).model_dump()
        )
    token = await dm.auth_repo.issue_access_token(username= form_data.username,access_token_expire_minute=EnvirenmentVariable.ACCESS_TOKEN_EXPIRE_MINUTES())
    return JSONResponse(content=token.model_dump())

@router.post("/logout/", status_code=status.HTTP_204_NO_CONTENT, responses={
    204 : {"description": "HTTP_204_NO_CONTENT",},
    })
async def logout(
    user_id: Annotated[str , Depends(read_user_or_raise)],
):
    await dm.auth_repo.logout(user_id=user_id)


@router.post("/verify_google/", responses={
    200 : {"model" : Token, "description": "HTTP_200_OK",},
    503 : {"description": "HTTP_503_SERVICE_UNAVAILABLE",},
    401 : {"description": "HTTP_401_UNAUTHORIZED",},
    })
async def verify_google(
    google_token: Annotated[str, Body()],
    default_google_user_password : Annotated[str | None, Query()] = "4321"
):
    try:
        # 1. Verify Google ID Token
        idinfo = id_token.verify_oauth2_token(google_token, requests.Request(), GOOGLE_CLIENT_ID)
        user_google_id = idinfo['sub']
        user_email = idinfo.get('email')
        user_name = idinfo.get('name')
        user_picture = idinfo.get('picture')

        # 2. Check if user exists in your database (by email)
        user_in_db = await dm.auth_repo.read_user_by_identifier(identifier=user_email)
        if user_in_db is None:
            # Registration flow: create user with email verified
            # You may want to store Google ID, name, and picture if your model supports it
            upserted_user = await dm.auth_repo.update_user_account(
                password=default_google_user_password,  # default_google_user_password
                username=user_email,
                is_verified=True
            )
            # Optionally, create free subscription for new users
            await createFreeSubscription(user_id=upserted_user.id)
            await dm.user_repo.update_referral_when_register(invite_contact=user_email, invited_user_id=upserted_user.id)
        else:
            # Login flow: ensure email is marked as verified
            if not user_in_db.is_email_verified:
                await dm.auth_repo.update_user_account(
                    password=user_in_db.hashed_password or "",
                    username=user_email,
                    is_verified=True
                )

        # 3. Issue JWT token for the user
        token = await dm.auth_repo.issue_access_token(
            username=user_email,
            access_token_expire_minute=EnvirenmentVariable.ACCESS_TOKEN_EXPIRE_MINUTES()
        )
        return JSONResponse(content=token.model_dump())

    except ValueError as e:
        
        message = translation_manager.gettext(TranslationKeys.INVALID_VERIFICATION_CODE)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=ErrorResponse(error_detail='TranslationKeys.INVALID_VERIFICATION_CODE', message=str(e)).model_dump()
        )
    except Exception as e:
        message = translation_manager.gettext(TranslationKeys.REMOTE_SERVICE_UNAVAILABLE)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=ErrorResponse(error_detail='TranslationKeys.REMOTE_SERVICE_UNAVAILABLE', message=str(e)).model_dump()
        )
# ...existing code...



@router.post("/send_sms/", status_code=status.HTTP_204_NO_CONTENT, responses={
    204 : {"description": "HTTP_204_NO_CONTENT",},
    })
async def send_sms(
    
    numbers: Annotated[list[str] , Query],
):
    await dm.auth_repo.send_sms_najva(numbers=numbers)
    



@router.post("/verify_by_ai/", responses={
    204 : {"description": "status.HTTP_204_NO_CONTENT",},
    400 : {"description": "HTTP_400_BAD_REQUEST",},
    412 : {"description": "HTTP_412_PRECONDITION_FAILED",},
    403 : {"description": "HTTP_403_FORBIDDEN",},
    404 : {"description": "HTTP_404_NOT_FOUND",},
    500 : {"description": "HTTP_500_INTERNAL_SERVER_ERROR",},
    503 : {"description": "HTTP_503_SERVICE_UNAVAILABLE",},
    504 : {"description": "HTTP_504_GATEWAY_TIMEOUT",},
    429 : {"description": "HTTP_429_TOO_MANY_REQUESTS",},
    }, status_code=status.HTTP_204_NO_CONTENT)
async def verify_by_ai(
    user_id: Annotated[str, Security(read_user_or_raise, scopes=["coach"])],
    video_gallary_files: UploadFile,
    user_spoken_language : Annotated[Language, Form()],
    tag: Annotated[GallaryTag, Form()],
    upload_date: Annotated[datetime | None, Form()] = None
):  
    if video_gallary_files.filename is None or video_gallary_files.size is None or video_gallary_files.content_type is None:
        message = TranslationKeys.INVALID_UPLOAD_FILE_REQUEST
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorResponse(
                error_detail='TranslationKeys.INVALID_UPLOAD_FILE_REQUEST',
                message=message
            ).model_dump()

        )
    allowed_types = [
        # 'audio/aac', 'audio/mpeg', 'audio/mp3', 'audio/wav', 'audio/flac', 'audio/ogg', 'audio/aiff',
        'video/mp4', 'video/quicktime', 'video/x-msvideo', 'video/webm', 'video/x-matroska'
    ]
    if video_gallary_files.content_type not in allowed_types:
        message = TranslationKeys.INVALID_UPLOAD_FILE_REQUEST
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorResponse(
                error_detail='TranslationKeys.INVALID_UPLOAD_FILE_REQUEST',
                message=f"{message}: Unsupported file type {video_gallary_files.content_type}"
            ).model_dump()
        )
    if video_gallary_files.size > 70 * 1024 * 1024:  # Restrict file size to 70 MB
        message = TranslationKeys.FILE_LIMIT_EXCEEDED.format(file_size_limit = 7 )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorResponse(
                error_detail='TranslationKeys.FILE_LIMIT_EXCEEDED',
                message=message
            ).model_dump()
        )
    try:
        await dm.auth_repo.verify_by_ai(
            user_id = user_id,
            video_gallary_files=video_gallary_files,
            user_spoken_language = user_spoken_language,
        )
        
        await _save_on_disk(user_id=user_id, tag = tag, video_gallary_files=video_gallary_files,upload_date = upload_date, description = '')
    except VerifyRejection:
        message = TranslationKeys.MISLEADING_OR_FALSE
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorResponse(
                error_detail='status.HTTP_400_BAD_REQUEST',
                message=message
            ).model_dump()
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

        
        
        
async def _save_on_disk(user_id:str,tag: GallaryTag, video_gallary_files: UploadFile, upload_date: datetime | None, description: str | None):
    from utility.constants import upload_directory_path
    upload_directory = f"{upload_directory_path}/user_{user_id}/"
    try:
        # reset the pointer
        await video_gallary_files.seek(0)
        images_meta_data = await dm.user_files_repo.save_files_on_disk(user_id=user_id, tag = tag,image_gallary_files=[video_gallary_files],upload_date = upload_date, upload_directory=upload_directory, description=description)
    except Exception as e:
        raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=ErrorResponse(
                        error_detail='TranslationKeys.FILE_UPLOAD_FAILED',
                        message=f'{TranslationKeys.FILE_UPLOAD_FAILED} : {str(e)}'
                    ).model_dump()
                )

    results = await dm.user_files_repo.upsert_user_files(user_files=images_meta_data)

    # return JSONResponse(
    #     content=[jsonable_encoder(file.model_dump()) for file in results]
    # )


