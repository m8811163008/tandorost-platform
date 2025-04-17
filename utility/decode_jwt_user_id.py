from typing import Annotated
from fastapi import Depends, HTTPException,status
from jwt import (decode, InvalidTokenError, ExpiredSignatureError) # type: ignore


from fastapi.security import OAuth2PasswordBearer
from pydantic import UUID4
from utility.constants import token_url
from utility.envirement_variables import EnvirenmentVariable
from utility.translation_keys import TranslationKeys
from dependeny_manager import dm


oauth2_scheme = OAuth2PasswordBearer(tokenUrl=token_url)



def jwt_user_id(token: Annotated[str, Depends(oauth2_scheme)]) -> UUID4:
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
        return user_id
    except (InvalidTokenError, InvalidTokenError) as e:
        raise HTTPException(
             status_code= status.HTTP_401_UNAUTHORIZED,
             detail=TranslationKeys.INVALID_TOKEN
         )
    
async def read_user_or_raise(user_id: Annotated[str , Depends(jwt_user_id)])-> str:
     user = await dm.user_repo.read_user(user_id=user_id)
     if user is None or user.id is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=TranslationKeys.USER_NOT_FOUND,
        )
     return user.id