from fastapi import FastAPI
from app.dependencies import *
from app.routers import post_handlers

app = FastAPI()
create_db_and_tables()

app.include_router(post_handlers.router)