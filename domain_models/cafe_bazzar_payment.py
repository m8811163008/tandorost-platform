from pydantic import BaseModel

class CafeBazzarPayment(BaseModel):
    caffe_bazzar_rsa: str
    caffe_bazzar_subscription_plan_one_month_sdk: str
    caffe_bazzar_subscription_plan_three_month_sdk: str
    caffe_bazzar_subscription_plan_six_month_sdk: str
