
from typing import  Awaitable, Callable
from fastapi import  FastAPI , Request, Response, Header, Depends
import routes.auth.auth as auth
import routes.user.user as user
import os
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

async def get_accept_language(accept_language: str = Header(default="en")):
    print(accept_language)
    return accept_language

# Validate environment variables at runtime
app = FastAPI(root_path="/api/v1", dependencies=[Depends(get_accept_language)])

app.include_router(auth.router)
app.include_router(user.router)

class DefaultLanguageMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next : Callable[[Request], Awaitable[Response]]):
        # Check if the `Accept-Language` header is present
        if "accept-language" not in request.headers:
            # Add a default `Accept-Language` header
            request.headers.__dict__["_list"].append((b"accept-language", b"en"))
        print(request.headers)
        
        response = await call_next(request)
        return response

app.add_middleware(DefaultLanguageMiddleware)
app.add_middleware(TrustedHostMiddleware)


# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = 30

@app.get("/")
async def read_root():
    return {"Hello": "World"}


