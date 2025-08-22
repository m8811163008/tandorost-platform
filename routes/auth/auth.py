from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from domain_models import (InvalidPassword, InvalidVerificationCode, UsernameAlreadyInUse, UsernameIsInactive, UsernameNotRegisteredYet, VerifiationCodeRequestReachedLimit, NetworkConnectionError ,VerificationType, Token, Currency, PaymentMethod, SubscriptionType, UserInDbSubscriptionPayment)
from fastapi.security import  OAuth2PasswordRequestForm
from typing import Annotated
from datetime import datetime
from fastapi import Depends, HTTPException, status
from domain_models.response_model import ErrorResponse
# from repositories.auth import UsernameType, username_type
from utility import (
    EnvirenmentVariable,
    check_verify_rate_limit,
    TranslationKeys,
    translation_manager
)
from dependeny_manager import dm ,UsernameType, username_type
from utility.constants import rate_limit_second


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.post("/send_verification_code/", responses={
    200 : {"model" : None, "description": "HTTP_200_OK",},
    429 : {"description": "HTTP_429_TOO_MANY_REQUESTS",},
    404 : {"description": "HTTP_404_NOT_FOUND",},
    409 : {"description": "HTTP_409_CONFLICT",},
    503 : {"description": "HTTP_503_SERVICE_UNAVAILABLE",},
    })
async def verify(
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
        message = translation_manager.gettext(TranslationKeys.USERNAME_IN_USE).format(user_name=phone_number)
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
    return JSONResponse(content=translation_manager.gettext(TranslationKeys.USER_REGISTERED))

async def createFreeSubscription(user_id : str, ):
    subscription_data = UserInDbSubscriptionPayment(
        user_id = user_id,
        paid_amount = 0,
        discount_amount= 0,
        currency = Currency.IRRIAL,
        payment_method=PaymentMethod.INPAYMENTCAFEBAZZAR,
        purchase_date = datetime.now(),
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
    return JSONResponse(content=token.model_dump(by_alias=True))