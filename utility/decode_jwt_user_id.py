from typing import Annotated
from bson import ObjectId
from fastapi import Depends, HTTPException,status
from jwt import (decode, InvalidTokenError, ExpiredSignatureError)


from fastapi.security import OAuth2PasswordBearer
from utility.constants import token_url
from utility.envirement_variables import EnvirenmentVariable
from utility.translation_keys import TranslationKeys


oauth2_scheme = OAuth2PasswordBearer(tokenUrl=token_url)

def jwt_user_id(token: Annotated[str, Depends(oauth2_scheme)]) -> ObjectId:
    try:
        secret_key = EnvirenmentVariable.SECRET_KEY()
        algorithm = EnvirenmentVariable.ALGORITHM()
        try:
            payload = decode(token, secret_key, algorithms=[algorithm])
        except ExpiredSignatureError:
            raise InvalidTokenError
        user_id = payload.get("user_id")
        if user_id is None:
            raise InvalidTokenError
        return ObjectId(user_id)
    except (InvalidTokenError, InvalidTokenError) as e:
        raise HTTPException(
             status_code= status.HTTP_401_UNAUTHORIZED,
             detail=TranslationKeys.INVALID_TOKEN
         )