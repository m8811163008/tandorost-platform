
from fastapi import  APIRouter
from repositories.user.user import UserRepository


from domain_models.user import User

# MongoDB configuration
MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "tandorost"
BASE_URL = 'http://127.0.0.1:8001'

# Initialize the repository
user_repo = UserRepository(MONGO_URI, DATABASE_NAME)

router = APIRouter()

@router.get("/users/{user_name}/")
async def read_user(
    user_name: str,
) -> User | None:
    return await user_repo.get_user(user_name)


# @app.get("/users/me/items/")
# async def read_own_items(
#     current_user: Annotated[User, Depends(get_current_active_user)],
# ):
#     return [{"item_id": "Foo", "owner": current_user.username}]
