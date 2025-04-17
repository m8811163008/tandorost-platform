
from fastapi import  FastAPI , Depends
from routes.auth import router as auth_router
from routes.user import router as user_router
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from utility import (
    get_accept_language, 
    translation_manager, 
    TranslationKeys
)


from fastapi.staticfiles import StaticFiles


app = FastAPI(root_path="/api/v1", dependencies=[Depends(get_accept_language)])


app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize routers
app.include_router(auth_router)
app.include_router(user_router)

# Initialize middlewares
app.add_middleware(TrustedHostMiddleware)

@app.get("/")
async def read_root():
    # DEBUG CLEAR DATABASE
    from dependeny_manager import dm
    await dm.local_database.clear()
    welcome_message = translation_manager.gettext(TranslationKeys.WELCOME_MESSAGE).format(user_name="Milad")
    return {"Hello": f"{welcome_message}"}


