from fastapi import APIRouter
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
import os

from repositories.user.user import UserRepository

# MongoDB configuration
MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "tandorost"
BASE_URL = 'http://127.0.0.1:8001'
ACCESS_TOKEN_EXPIRE_MINUTES = 180
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("HS256")

# Initialize the repository
token_repo = TokenRepository(MONGO_URI, DATABASE_NAME)
user_repo = UserRepository(MONGO_URI, DATABASE_NAME)


router = APIRouter(
    # prefix="/auth",
    tags=["Authentication"],
)



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


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
    if SECRET_KEY is None or ALGORITHM is None:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Envirement variables is not set"
            )
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) # type: ignore
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        if SECRET_KEY is None or ALGORITHM is None:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Envirement variables is not set"
            )
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) # type: ignore
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        # token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user =await get_user( user_name=username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends(get_current_user)],
) -> Token:
    user = await authenticate_user(form_data.username, form_data.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    assert(user.id is not None)
    token_instance = Token(access_token=access_token, token_type="bearer", user_id= user.id)
    return await token_repo.save_token(token_instance)
    
@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    user_name: str,
    password : str,
) -> dict[str, str]:
    hashed_password = get_password_hash(password)
    user = UserInDB(username=user_name, hashed_password=hashed_password)
    await user_repo.save_user(user = user)
    return {'Message' : 'Success'}




@router.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}