
from fastapi import  FastAPI , Depends

from routes.auth import router as auth_router
from routes.user import router as user_router
from routes.foods_nutrition import router as food_nutrition_router
from fastapi.middleware.trustedhost import TrustedHostMiddleware

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

# Initialize middlewares
app.add_middleware(TrustedHostMiddleware)
app.add_middleware(BaseHTTPMiddleware, dispatch=auth_middleware)

app.mount(protected_directory_path, StaticFiles(directory=protected_directory, check_dir=True))


@app.get("/")
async def read_root():
    # DEBUG CLEAR DATABASE
    # from dependeny_manager import dm
    # await dm.local_database.clear()
    welcome_message = translation_manager.gettext(TranslationKeys.WELCOME_MESSAGE).format(api_uri=f"{root_path}/openapi.json")
    return welcome_message


