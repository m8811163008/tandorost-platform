from fastapi.security import SecurityScopes
from starlette.requests import Request
from starlette.responses import Response
from typing import Optional
from utility.decode_jwt_user_id import jwt_user_id, read_user_or_raise
from typing import Callable, Awaitable
from fastapi.responses import HTMLResponse
from utility.constants import protected_directory, root_endpoint, regular_directory

def handle_unauthorized_access() -> HTMLResponse:
    try:
        with open(f"{protected_directory}/404.html", "rt") as file:
            content = file.read()
            return HTMLResponse(content=content, status_code=401)
    except Exception as e:
        raise e



async def auth_middleware(request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
    if request.method == "OPTIONS":
        response = await call_next(request) # type: ignore
        return response
    if request.url.path.startswith(f"{root_endpoint}/{protected_directory}"):

        authorization: Optional[str] = request.headers.get("Authorization")
        if not authorization or not authorization.startswith("Bearer "):
            return handle_unauthorized_access()
        token = authorization.split(" ")[1]
        try:
            user_id = jwt_user_id(security_scopes=SecurityScopes(scopes=['trainer']) ,token= token)
            await read_user_or_raise(user_id=str(user_id))
        except Exception as e:
            return handle_unauthorized_access()
    if request.url.path.startswith(f"{root_endpoint}/{regular_directory}"):
        # Allow access to regular_directory for everyone, no auth required
        pass
    response = await call_next(request) # type: ignore
    return response # type: ignore