

from random import Random
from fastapi import APIRouter, Form
from domain_models import InvalidPassword, InvalidVerificationCode, UsernameAlreadyInUse, UsernameIsInactive, UsernameNotRegisteredYet, VerifiationCodeRequestReachedLimit, NetworkConnectionError,ApiResponse,VerificationCode,VerificationType
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated, Any
from datetime import datetime
from fastapi import Depends, HTTPException, status
from utility.envirement_variables import EnvirenmentVariable
from utility.rate_limiter import check_verify_rate_limit
from utility.translation_keys import TranslationKeys
from utility.translation_utils import translation_manager
from dependeny_manager import dm  
from utility.constants import token_url, verification_sms_panel_body_id


oauth2_scheme = OAuth2PasswordBearer(tokenUrl=token_url)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.post("/send_verification_code/", status_code = status.HTTP_200_OK)
async def verify(
    phone_number : Annotated[str, Form(pattern=r"^09\d{9}$")],
    verification_type : VerificationType
):  
    try:
        await check_verify_rate_limit(phonenumber=phone_number, rate_limit_second=120)
    except VerifiationCodeRequestReachedLimit as e:
        message =translation_manager.gettext(TranslationKeys.RATE_LIMIT_REACH).format(second= e.seconds_left)
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail= ApiResponse.error(message='TranslationKeys.RATE_LIMIT_REACH', error_detail=message).to_dict()
        )
    
    random_code = str(Random().randint(1000, 9999))
    verification_code = VerificationCode(created_at= datetime.now().isoformat(), verification_code= random_code)

    try:
       await dm.auth_repo.send_verification_code(code=verification_code, username=phone_number,body_id=verification_sms_panel_body_id, verification_type = verification_type)
       return ApiResponse.success(message=translation_manager.gettext(TranslationKeys.USER_REGISTERED), data=None).to_dict()
    except UsernameAlreadyInUse:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail = ApiResponse.error(message='TranslationKeys.USERNAME_IN_USE', error_detail=translation_manager.gettext(TranslationKeys.USERNAME_IN_USE).format(user_name=phone_number)).to_dict()
        )
    except NetworkConnectionError: 
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail = ApiResponse.error(message='TranslationKeys.REMOTE_SERVICE_UNAVAILABLE', error_detail=translation_manager.gettext(TranslationKeys.REMOTE_SERVICE_UNAVAILABLE)).to_dict()
        )
    
@router.post("/register/", status_code=status.HTTP_201_CREATED)
async def register(
    user_name: Annotated[str, Form(pattern=r"^09\d{9}$")],
    password : Annotated[str, Form(min_length=4)],
    verification_code : Annotated[str, Form(min_length=4, max_length=4, pattern=r"^\d{4}$")],
) -> dict[str, Any]:
    try:
        await dm.auth_repo.verify_code(username=user_name,verification_code = verification_code)
    except UsernameNotRegisteredYet :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = ApiResponse.error(message='TranslationKeys.USERNAME_NOT_REGISTERED_YET', error_detail=translation_manager.gettext(TranslationKeys.USERNAME_NOT_REGISTERED_YET).format(user_name=user_name)).to_dict()
        )
    except InvalidVerificationCode:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = ApiResponse.error(message='TranslationKeys.INVALID_VERIFICATION_CODE', error_detail=translation_manager.gettext(TranslationKeys.INVALID_VERIFICATION_CODE).format(user_name=user_name)).to_dict()
        )    

    await dm.auth_repo.update_user_account(password=password,username=user_name, is_enabled=True)
    return ApiResponse.success(message=translation_manager.gettext(TranslationKeys.USER_REGISTERED), data=None).to_dict()
    

@router.post("/forgot_password/", status_code=status.HTTP_201_CREATED)
async def forgot_password(
    user_name: Annotated[str, Form(pattern=r"^09\d{9}$")],
    new_password : Annotated[str, Form(min_length=4)],
    verification_code : Annotated[str, Form(min_length=4, max_length=4, pattern=r"^\d{4}$")],
) -> dict[str, Any]:
    try:
        await dm.auth_repo.verify_code(username=user_name,verification_code = verification_code)
    except UsernameNotRegisteredYet :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = ApiResponse.error(message='TranslationKeys.USERNAME_NOT_REGISTERED_YET', error_detail=translation_manager.gettext(TranslationKeys.USERNAME_NOT_REGISTERED_YET).format(user_name=user_name)).to_dict()
        )
    except InvalidVerificationCode:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = ApiResponse.error(message='TranslationKeys.INVALID_VERIFICATION_CODE', error_detail=translation_manager.gettext(TranslationKeys.INVALID_VERIFICATION_CODE).format(user_name=user_name)).to_dict()
        )    

    await dm.auth_repo.update_user_account(password=new_password,username=user_name)
    return ApiResponse.success(message=translation_manager.gettext(TranslationKeys.PASSWORD_RESTORED), data=None).to_dict()


@router.post("/token/")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    try:
        await dm.auth_repo.authenticate(username=form_data.username, password=form_data.password)
    except UsernameNotRegisteredYet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = ApiResponse.error(message='TranslationKeys.USERNAME_NOT_REGISTERED_YET', error_detail=translation_manager.gettext(TranslationKeys.USERNAME_NOT_REGISTERED_YET)).to_dict()
        )
    except UsernameIsInactive:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail = ApiResponse.error(message='TranslationKeys.USERNAME_IS_INACTIVE', error_detail=translation_manager.gettext(TranslationKeys.USERNAME_IS_INACTIVE)).to_dict()
        )
    except InvalidPassword:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = ApiResponse.error(message='TranslationKeys.INVALID_PASSWORD', error_detail=translation_manager.gettext(TranslationKeys.INVALID_PASSWORD)).to_dict()
        )
    token = await dm.auth_repo.issue_access_token(username= form_data.username,access_token_expire_minute=EnvirenmentVariable.ACCESS_TOKEN_EXPIRE_MINUTES())
    return ApiResponse.success(data=token.model_dump_json()).to_dict()
    

@router.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}