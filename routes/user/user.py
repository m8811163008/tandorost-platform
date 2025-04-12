
from fastapi import  APIRouter
# from dependeny_manager import dm
# from domain_models import User

# MongoDB configuration
# MONGO_URI = "mongodb://localhost:27017"
# DATABASE_NAME = "tandorost"
# BASE_URL = 'http://127.0.0.1:8001'

router = APIRouter()

# @router.get("/users/{user_name}/")
# async def read_user(
#     user_name: str,
# ) -> User | None:
#     return await dm.user_repo.get_user(user_name)


# @app.get("/users/me/items/")
# async def read_own_items(
#     current_user: Annotated[User, Depends(get_current_active_user)],
# ):
#     return [{"item_id": "Foo", "owner": current_user.username}]
