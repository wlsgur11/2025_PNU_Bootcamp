# parameter_models.py
from pydantic import BaseModel

class AuthSigninReq(BaseModel):
    login_id: str
    pwd: str

class AuthSignupReq(BaseModel):
    login_id: str
    pwd: str
    name: str