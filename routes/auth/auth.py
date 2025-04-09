
from random import Random
from fastapi import APIRouter, Form
from domain_models.exceptions import UsernameAlreadyInUse
from domain_models.response_model import ApiResponse
from data.local_database.model.token import Token
from domain_models.user import User, UserInDB
from domain_models.verification_code import VerificationCode
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated, Any
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from jwt.exceptions import InvalidTokenError
from utility.envirement_variables import EnvirenmentVariable
from utility.translation_keys import TranslationKeys
from utility.translation_utils import translation_manager
from dependeny_manager import dm  
from routes.auth.utility import is_valid_password, create_access_token, get_password_hash
import jwt


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)
tokenUrl = "api/v1/auth/token/"


oauth2_scheme = OAuth2PasswordBearer(tokenUrl=tokenUrl)


@router.post("/token/")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = await authenticate_user(form_data.username, form_data.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=TranslationKeys.INCORRECT_CREDENTIALS,
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=EnvirenmentVariable.ACCESS_TOKEN_EXPIRE_MINUTES())
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    assert(user.id is not None)
    token_instance = Token(access_token=access_token, token_type="bearer", user_id= user.id)
    return await dm.auth_repo.save_token(token_instance)

@router.post("/verify_phone_number", status_code = status.HTTP_201_CREATED)
async def verify(
        phone_number : Annotated[str, Form(pattern=r"^09\d{9}$")],
):  
    random_code = Random().randint(1000, 9999)
    verification_code = VerificationCode(created_at= datetime.now().isoformat(), verification_code=random_code)
    user = UserInDB(username=phone_number,verification_code=verification_code)
    try:
       await dm.user_repo.create_user(user=user)
    except UsernameAlreadyInUse as e:
        raise HTTPException(
            
            status_code=status.HTTP_409_CONFLICT,
            detail = ApiResponse.error(message='TranslationKeys.USERNAME_IN_USE', error_detail=translation_manager.gettext(TranslationKeys.USERNAME_IN_USE).format(user_name=phone_number)).to_dict()
        )
    
    
@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    user_name: Annotated[str, Form(pattern=r"^09\d{9}$")],
    password : Annotated[str, Form(min_length=4)],
) -> dict[str, Any]:
    hashed_password = get_password_hash(password)
    user = UserInDB(username=user_name, hashed_password=hashed_password)
    try:
        await dm.user_repo.create_user(user = user)
    except UsernameAlreadyInUse as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail = ApiResponse.error(message=e.detail, error_detail=translation_manager.gettext("username_in_use").format(user_name=user_name)).to_dict()
        )
    data = User(**user.model_dump()).model_dump()
    return ApiResponse.success(message='User registered successfully', data=data).to_dict()
    

@router.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


async def get_user(user_name:str) -> UserInDB | None:
    return await dm.user_repo.get_user(user_name=user_name)
    

async def authenticate_user( username: str, password: str) -> UserInDB | None:
    user = await get_user(username)
    if user is None:
        return None
    if user.hashed_password is None:
        return None
    if not is_valid_password(password, user.hashed_password):
        return None
    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=ApiResponse.error(message=TranslationKeys.INVALID_CREDENTIALS, error_detail= TranslationKeys.INVALID_CREDENTIALS).to_dict(),
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, ey = EnvirenmentVariable.SECRET_KEY(), algorithms=[EnvirenmentVariable.ALGORITHM()]) # type: ignore
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        # token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = await get_user(user_name=username)
    if user is None:
        raise credentials_exception
    return user
