
from fastapi import  FastAPI
import routes.auth.auth as auth
import routes.user.user as user
import os



app = FastAPI(root_path="/api/v1")

app.include_router(auth.router)
app.include_router(user.router)


# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = 30

@app.get("/")
async def read_root():
    return {"Hello": "World"}


