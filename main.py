from fastapi import FastAPI
from app.dependencies.sqlite_db import *
from app.routers import post_handlers
from app.routers import auth_routers

app = FastAPI()
create_db_and_tables()

app.include_router(post_handlers.router)
app.include_router(auth_routers.router)