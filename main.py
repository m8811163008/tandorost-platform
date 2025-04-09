
from fastapi import  FastAPI , Depends
import routes.auth.auth as auth
import routes.user.user as user
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from utility.translation_keys import TranslationKeys
from utility.translation_utils import translation_manager
from utility.accept_language import get_accept_language
from slowapi.errors import RateLimitExceeded
from slowapi import  _rate_limit_exceeded_handler
from utility.rate_limiter import limiter




app = FastAPI(root_path="/api/v1", dependencies=[Depends(get_accept_language)])
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler) # type: ignore


# Initialize routers
app.include_router(auth.router)
app.include_router(user.router)

# Initialize middlewares
app.add_middleware(TrustedHostMiddleware)

@app.get("/")
async def read_root():
    welcome_message = translation_manager.gettext(TranslationKeys.WELCOME_MESSAGE).format(user_name="Milad")
    return {"Hello": f"{welcome_message}"}


