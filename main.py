
import logging
from fastapi import  FastAPI , Depends

from routes.auth import router as auth_router
from routes.user import router as user_router
from routes.foods_nutrition import router as food_nutrition_router
from routes.fitness import router as fitness_router
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware

from utility import (
    auth_middleware,
    get_accept_language, 
    translation_manager, 
    TranslationKeys
)
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.base import BaseHTTPMiddleware
from utility.constants import root_path, protected_directory_path, protected_directory
from fastapi.staticfiles import StaticFiles


app = FastAPI(root_path=root_path, dependencies=[Depends(get_accept_language)])


# Initialize routers
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(food_nutrition_router)
app.include_router(fitness_router)
# Initialize middlewares

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow any origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Initialize middlewares
app.add_middleware(TrustedHostMiddleware)
app.add_middleware(BaseHTTPMiddleware, dispatch=auth_middleware)
from fastapi import Response, Request
from typing import Callable, Awaitable
@app.middleware("http")
async def log_requests(request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
    logging.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logging.info(f"Response status: {response.status_code}")
    return response


app.mount(protected_directory_path, StaticFiles(directory=protected_directory, check_dir=True))


@app.get("/")
async def read_root():
    # DEBUG CLEAR DATABASE
    from dependeny_manager import dm
    await dm.local_database.clear()
    welcome_message = translation_manager.gettext(TranslationKeys.WELCOME_MESSAGE).format(api_uri=f"{root_path}/openapi.json")
    return welcome_message


