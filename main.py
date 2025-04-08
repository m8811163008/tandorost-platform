
from fastapi import  FastAPI , Header, Depends
import routes.auth.auth as auth
import routes.user.user as user
import os
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from utility.translation_keys import TranslationKeys
from utility.translation_utils import translation_manager

async def get_accept_language(accept_language: str = Header(default="en")):
        if translation_manager.current_language != accept_language:
            translation_manager.set_language(accept_language)


app = FastAPI(root_path="/api/v1", dependencies=[Depends(get_accept_language)])

app.include_router(auth.router)
app.include_router(user.router)

app.add_middleware(TrustedHostMiddleware)


# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = 30

@app.get("/")
async def read_root():
    welcome_message = translation_manager.gettext(TranslationKeys.WELCOME_MESSAGE).format(user_name="Milad")
    
    return {"Hello": f"{welcome_message}"}


