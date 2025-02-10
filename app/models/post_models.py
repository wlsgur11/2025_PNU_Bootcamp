from dataclasses import dataclass
from sqlmodel import Field, SQLModel
from enum import Enum

class RESULT_CODE(Enum):
    SUCCESS = 1
    NOT_FOUND = -2
    FAILED = -3

class Post(SQLModel, table=True):
    id: int | None= Field(primary_key=True)
    price: int = Field(index=True)
    created_at: int = Field(index=True)
    published: bool = Field(index=True)
    title: str
    body: str
    location: str = Field(index=True)

@dataclass
class PostReq:
    title: str
    body: str
    price: int
    published: bool
    location: str


@dataclass
class PostResp:
    posts: list[Post]
    err_str: str | None = None
