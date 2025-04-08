
from fastapi import APIRouter, Form
from domain_models.exceptions import UsernameAlreadyInUse
from domain_models.response_model import ApiResponse
from domain_models.token import Token
from domain_models.user import User, UserInDB
from repositories.auth.token import TokenRepository
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated, Any
from datetime import datetime, timedelta, timezone
import jwt
from fastapi import Depends, HTTPException, status
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext


from repositories.user.user import UserRepository
from utility.envirement_variables import EnvirenmentVariable


# Initialize the repository
token_repo = TokenRepository(EnvirenmentVariable.MONGO_URI(), EnvirenmentVariable.DATABASE_NAME())
user_repo = UserRepository(EnvirenmentVariable.MONGO_URI(), EnvirenmentVariable.DATABASE_NAME())


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)
tokenUrl = "api/v1/auth/token/"


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=tokenUrl)


def is_valid_password(plain_password:str, hashed_password:str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password:str):
    return pwd_context.hash(password)


async def get_user(user_name:str) -> UserInDB | None:
    return await user_repo.get_user(user_name=user_name)
    

async def authenticate_user( username: str, password: str) -> UserInDB | None:
    user = await get_user(username)
    if user is None:
        return None
    if not is_valid_password(password, user.hashed_password):
        return None
    return user


def create_access_token(data: dict[str, Any], expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode,key = EnvirenmentVariable.SECRET_KEY(), algorithm = EnvirenmentVariable.ALGORITHM()) # type: ignore
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
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
    user = await get_user( user_name=username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@router.post("/token/")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = await authenticate_user(form_data.username, form_data.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=EnvirenmentVariable.ACCESS_TOKEN_EXPIRE_MINUTES())
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    assert(user.id is not None)
    token_instance = Token(access_token=access_token, token_type="bearer", user_id= user.id)
    return await token_repo.save_token(token_instance)
    
@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    user_name: Annotated[str, Form(pattern=r"^09\d{9}$")],
    password : Annotated[str, Form(min_length=4)],
) -> dict[str, Any]:
    hashed_password = get_password_hash(password)
    user = UserInDB(username=user_name, hashed_password=hashed_password)
    try:
        await user_repo.save_user(user = user)
    except UsernameAlreadyInUse as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail = ApiResponse.error(message=e.detail, error_code= 409, error_detail=f"The username '{user_name}' is already taken").to_dict()
        )
    data = User(**user.model_dump()).model_dump()
    return ApiResponse.success(message='User registered successfully', data=data).to_dict()
    

@router.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}