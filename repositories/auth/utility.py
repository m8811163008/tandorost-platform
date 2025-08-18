from datetime import timedelta, datetime, timezone
from typing import Any
from passlib.context import CryptContext
import jwt
import re
from enum import Enum, StrEnum, auto
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def is_valid_password(plain_password:str, hashed_password:str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password:str):
    return pwd_context.hash(password)

def create_access_token(data: dict[str, Any],key : str, algorithm: str, expires_delta: timedelta | None = None, ) ->str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode,key = key, algorithm = algorithm) # type: ignore
    return encoded_jwt

class UsernameType(StrEnum):
    EMAIL = auto()
    PHONENUMBER = auto()
    INVALID = auto()

def username_type(username: str) -> UsernameType:
    if re.match(r'^09\d{9}$', username):
        return UsernameType.PHONENUMBER
    elif re.match(r'^[^@]+@[^@]+\.[^@]+$', username):
        return UsernameType.EMAIL
    else:
        return UsernameType.INVALID