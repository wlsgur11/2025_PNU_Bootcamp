# parameter_models.py
from pydantic import BaseModel

class AuthSigninReq(BaseModel):
    login_id: str
    password: str

class AuthSignupReq(BaseModel):
    login_id: str
    password: str
    nickname: str