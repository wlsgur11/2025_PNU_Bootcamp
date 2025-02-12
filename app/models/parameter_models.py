# parameter_models.py
from pydantic import BaseModel
from dataclasses import dataclass
from app.models.user_models import User

class AuthSigninReq(BaseModel):
    login_id: str
    password: str

class AuthSignupReq(BaseModel):
    login_id: str
    password: str
    nickname: str

@dataclass
class UserResp:
    users: list[User]
    err_str: str | None = None