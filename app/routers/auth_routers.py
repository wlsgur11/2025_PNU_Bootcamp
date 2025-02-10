# app/routers/auth_router.py

from fastapi import APIRouter, Depends, HTTPException
from app.models.parameter_models import AuthSignupReq, AuthSigninReq
from app.dependencies.sqlite_db import get_db_session
from app.dependencies.jwt_utils import JWTUtil
from app.services.auth_service import AuthService

router = APIRouter(prefix='/auth')

# 1. signup
@router.post('/signup')
def auth_signup(req: AuthSignupReq,
                db=Depends(get_db_session),
                jwtUtil: JWTUtil=Depends(),
                authService: AuthService=Depends()):
    user = authService.signup(db, req.login_id, req.pwd, req.name)
    if not user:
        raise HTTPException(status_code=400, detail="뭔가 잘못됐다.")
    user.access_token = jwtUtil.create_token(user.model_dump())
    return user


# 2. signin
@router.post("/signin")
def auth_signin(req: AuthSigninReq, 
                db=Depends(get_db_session),
                jwtUtil: JWTUtil=Depends(),
                authService: AuthService=Depends()):
    user = authService.signin(db, req.login_id, req.pwd)
    if not user:
        raise HTTPException(status_code=401, detail="로그인 실패")
    
    user.access_token = jwtUtil.create_token(user.model_dump())
    return user