from dataclasses import dataclass
from sqlmodel import Field, SQLModel
from enum import Enum
from fastapi import UploadFile
from pydantic import BaseModel

class RESULT_CODE(Enum):
    SUCCESS = 1
    NOT_FOUND = -2
    FAILED = -3
    USER_FAIL = -4

class Post(SQLModel, table=True):
    id: int | None= Field(primary_key=True)
    price: int = Field(index=True)
    created_at: int = Field(index=True)
    published: bool = Field(index=True)
    title: str
    body: str
    location: str = Field(index=True)
    updated_at: int = Field(index=True)
    author_id: int | None =  Field(default=None, foreign_key="user.id")
    like: int | None = Field(index=True)
    author_name: str | None  = Field(default=None)

# post-{post.id}-{photo.id}.png
class Photo(SQLModel, table=True):
    id: int|None = Field(primary_key=True)
    created_at: int = Field(index=True)
    post_id: int | None = Field(default=None, foreign_key="post.id")
    author_id: int | None = Field(default=None)
    image_src: str | None = Field(default=None)
# '/static/post1-1.jpg'
# GET http://localhost:8000/static/{author_id}/{post_id}/0.png

class PostReq(BaseModel):
    title: str
    body: str
    price: int
    published: bool
    location: str
    files: list[UploadFile]

class PostWithPhoto(BaseModel):
    post: Post
    photo: Photo

class PostWithPhotos(BaseModel):
    post: Post
    photos: list[str] = []

class PostListWithPhoto(BaseModel):
    posts: list[PostWithPhoto] = []
    err_str: str | None = None



@dataclass
class PostResp:
    posts: list[Post]
    err_str: str | None = None
