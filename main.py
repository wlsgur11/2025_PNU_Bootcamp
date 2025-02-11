from fastapi import FastAPI
from app.dependencies.sqlite_db import *
from app.routers import post_routers
from app.routers import auth_routers
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
create_db_and_tables()

origins = [
    "http://localhost:8000",
    "http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post_routers.router)
app.include_router(auth_routers.router)