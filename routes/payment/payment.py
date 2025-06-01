

from typing import Annotated

from fastapi import  APIRouter, Depends
from fastapi.responses import JSONResponse
from dependeny_manager import dm
from domain_models.data_models import UserInDbSubscriptionPayment, UserFoodCount

from utility.decode_jwt_user_id import read_user_or_raise

from fastapi.encoders import jsonable_encoder

router = APIRouter(
    prefix="/payment",
    tags=["Payment Data"],
)


@router.get("/read_subscriptions/",responses={
    200 : {"model" : list[UserInDbSubscriptionPayment], "description": "HTTP_200_OK",},
    404 : {"description": "HTTP_404_NOT_FOUND",},
    })
async def read_subscriptions(
    user_id: Annotated[str , Depends(read_user_or_raise)],
) :
    subscription_payment = await dm.payment_repo.read_payment_subscription(user_id=user_id)
    return JSONResponse(
        content=jsonable_encoder([item.model_dump() for item in subscription_payment])
        )
@router.get("/read_user_food_count/",responses={
    200 : {"model" : UserFoodCount, "description": "HTTP_200_OK",},
    404 : {"description": "HTTP_404_NOT_FOUND",},
    })
async def read_user_food_count(
    user_id: Annotated[str , Depends(read_user_or_raise)],
) :
    food_count = await dm.payment_repo.read_user_food_count(user_id=user_id)
    return JSONResponse(
        content=jsonable_encoder(food_count.model_dump())
        )


@router.post("/create_subscription_payment/", responses={
    200 : {"model" : UserInDbSubscriptionPayment, "description": "HTTP_200_OK",},
    })
async def create_subscription_payment(
    subscription_data: Annotated[UserInDbSubscriptionPayment, Depends()],
):
    subscription_payment = await dm.payment_repo.create_payment_subscription(subscription_data=subscription_data)
    return JSONResponse(
        content= jsonable_encoder(subscription_payment.model_dump())
    )