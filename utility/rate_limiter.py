from domain_models import VerifiationCodeRequestReachedLimit
from datetime import datetime
from dependeny_manager import dm  

async def check_verify_rate_limit(phonenumber: str, rate_limit_second: int):
    user = await dm.user_repo.get_user(user_name= phonenumber)
    if user is not None and user.verification_code is not None:
        created_at = datetime.fromisoformat(user.verification_code.created_at)
        time_delta = datetime.now() - created_at
        if time_delta.seconds  < rate_limit_second:
            seconds_left = rate_limit_second - time_delta.seconds
            raise VerifiationCodeRequestReachedLimit(seconds_left=seconds_left)
