# app/services/auth_service.py
import bcrypt
import time
from sqlmodel import Session, select
from app.models.user_models import User

class AuthService:
    # 1. Password 단방향 암호화
    # 회원가입 -> password 암호화 -> DB
    def get_hashed_pwd(self, pwd:str) -> str:
        encoded_pwd = pwd.encode('utf-8')
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(encoded_pwd, salt)

    # 2. Password 검증
    # 로그인 -> password 암호화 -> DB 암호화된 패스워드 == 클라이언트입력 암호화된 패스워드
    def verify_pwd(self, pwd: str, hpwd: str) -> bool:
        encoded_pwd = pwd.encode('utf-8')
        return bcrypt.checkpw(password=encoded_pwd,hashed_password=hpwd)

    # 3. 회원가입때 DB 로직 구현
    # - 가입일시 만들어서 User.created_at
    # - (1) Password 암호화 함수를 이용하여 암호화된 패스워드 -> User.pwd
    # - DB에 user를 넣는다.
    def signup(self, db: Session, login_id: str, pwd: str, name: str) -> User | None:
        try:
            hashed_pwd = self.get_hashed_pwd(pwd)
            user = User(login_id=login_id, pwd=hashed_pwd, name=name)
            user.created_at = int(time.time())

            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        except Exception as e:
            print(e)
        return None

    # login_id로 DB에서 사용자 정보 가져오는 함수
    def get_user_by_name(self, db: Session, login_id: str) -> User | None:
        stmt = select(User).where(User.login_id==login_id)
        results = db.exec(stmt)
        for user in results:
            return user
        return None

    # 4. 로그인API에서 사용할 DB 로직 구현
    # - DB에 저장된 사용자 정보를 불러온다(login_id)
    # - 클라이언트가 입력한 패스워드 문자열을 암호화 하여
    # DB에 저장된 패스워드와 일치하는지 (2)번 함수로 검사한다.
    def signin(self, db: Session, login_id: str, pwd: str) -> User | None:
        dbUser = self.get_user_by_name(db, login_id)
        if not dbUser:
            return None
        
        if not self.verify_pwd(pwd, dbUser.pwd):
            return None

        return dbUser
    
    def get_users(self, db:Session, page: int=1, limit:int=10):
        if limit > 10:
            limit = 10
        nOffset = (page-1) * limit
        users = db.exec(
            select(User).offset(nOffset).limit(limit)
        ).all()
        return users