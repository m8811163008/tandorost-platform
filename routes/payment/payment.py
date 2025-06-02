

from typing import Annotated

from fastapi import  APIRouter, Depends
from fastapi.responses import JSONResponse
from dependeny_manager import dm
from domain_models.cafe_bazzar_payment import CafeBazzarPayment
from domain_models.data_models import UserInDbSubscriptionPayment, UserFoodCount

from utility.decode_jwt_user_id import read_user_or_raise

from fastapi.encoders import jsonable_encoder

from utility.envirement_variables import EnvirenmentVariable

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

@router.get("/cafe_bazzar_payment_info/",responses={
    200 : {"model" : CafeBazzarPayment, "description": "HTTP_200_OK",},
    404 : {"description": "HTTP_404_NOT_FOUND",},
    })
async def cafe_bazzar_payment_info(
    user_id: Annotated[str , Depends(read_user_or_raise)],
) :
    payment_info =CafeBazzarPayment(
        caffe_bazzar_rsa=EnvirenmentVariable.CAFFE_BAZZAR_RSA(),
        caffe_bazzar_subscription_plan_one_month_sdk= EnvirenmentVariable.CAFFE_BAZZAR_SUBSCRIPTION_PLAN_ONE_MONTH_SDK(),
        caffe_bazzar_subscription_plan_three_month_sdk= EnvirenmentVariable.CAFFE_BAZZAR_SUBSCRIPTION_PLAN_THREE_MONTH_SDK()
    )
    return JSONResponse(
        content=jsonable_encoder(payment_info.model_dump())
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

