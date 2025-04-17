
from fastapi import  FastAPI , Depends
from fastapi.responses import HTMLResponse
from routes.auth import router as auth_router
from routes.user import router as user_router
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from utility import (
    get_accept_language, 
    translation_manager, 
    TranslationKeys
)
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
from starlette.responses import Response
from typing import Optional
from starlette.middleware.base import BaseHTTPMiddleware
from utility.constants import root_path, protected_directory_path, protected_directory
from utility.decode_jwt_user_id import jwt_user_id

from fastapi.staticfiles import StaticFiles


app = FastAPI(root_path=root_path, dependencies=[Depends(get_accept_language)])

from typing import Callable, Awaitable

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
            jwt_user_id(token= token)
        except Exception :
            return handle_unauthorized_access()
    response = await call_next(request) # type: ignore
    return response # type: ignore

# Initialize routers
app.include_router(auth_router)
app.include_router(user_router)

# Initialize middlewares
app.add_middleware(TrustedHostMiddleware)
app.add_middleware(BaseHTTPMiddleware, dispatch=auth_middleware)

app.mount(protected_directory_path, StaticFiles(directory=protected_directory, check_dir=True))



@app.get("/")
async def read_root():
    # DEBUG CLEAR DATABASE
    from dependeny_manager import dm
    await dm.local_database.clear()
    welcome_message = translation_manager.gettext(TranslationKeys.WELCOME_MESSAGE).format(api_uri=f"{root_path}/openapi.json")
    return welcome_message


