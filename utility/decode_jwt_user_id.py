from jwt import (decode, InvalidTokenError)

async def decode_jwt_user_id(token: str, secret_key : str, algorithm : str) -> str:
    try:
        payload = decode(token, secret_key, algorithms=[algorithm])
        user_id = payload.get("user_id")
        if user_id is None:
            raise InvalidTokenError
        return user_id
    except InvalidTokenError as e:
        raise e