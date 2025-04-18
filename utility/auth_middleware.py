from starlette.requests import Request
from starlette.responses import Response
from typing import Optional
from utility.decode_jwt_user_id import jwt_user_id, read_user_or_raise
from typing import Callable, Awaitable
from fastapi.responses import HTMLResponse
from utility.constants import protected_directory

def handle_unauthorized_access() -> HTMLResponse:
    try:
        with open(f"{protected_directory}/404.html", "rt") as file:
            content = file.read()
            return HTMLResponse(content=content, status_code=401)
    except Exception as e:
        raise e



async def auth_middleware(request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
    if request.url.path.startswith("/api/v1/protected_static"):
        authorization: Optional[str] = request.headers.get("Authorization")
        if not authorization or not authorization.startswith("Bearer "):
            return handle_unauthorized_access()
        token = authorization.split(" ")[1]
        try:
            user_id = jwt_user_id(token= token)
            await read_user_or_raise(user_id=str(user_id))
        except Exception :
            return handle_unauthorized_access()
    response = await call_next(request) # type: ignore
    return response # type: ignore