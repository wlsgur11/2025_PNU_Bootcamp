from fastapi import FastAPI, HTTPException, status, Depends
from dataclasses import dataclass, asdict
from sqlmodel import Field, SQLModel, Session, create_engine, select
import time

class Post(SQLModel, table=True):
    id: int | None= Field(primary_key=True)
    price: int = Field(index=True)
    created_at: int = Field(index=True)
    published: bool = Field(index=True)
    title: str
    body: str

@dataclass
class PostReq:
    title: str
    body: str
    price: int
    published: bool


@dataclass
class PostResp:
    posts: list[Post]
    err_str: str | None = None


class PostService:
    def get_post(self, db: Session, post_id: int):
        nPostid = 0
        try:
            nPostid = int(post_id)
        except:
            return None
        post = db.get(Post, post_id)
        return post
    
    def get_posts(self, db:Session, page: int=1, limit:int=10):
        nOffset = (page-1) * limit
        posts = db.exec(
            select(Post).offset(nOffset).limit(limit)
        ).all()
        return posts
        
    def create_post(self, db:Session, post: PostReq):
        postModel = Post()
        postModel.title = post.title
        postModel.body = post.body
        postModel.price = post.price
        postModel.published = post.published
        postModel.created_at = int(time.time())
        db.add(postModel)
        db.commit()
        db.refresh(postModel)
        return postModel
    
    def update_post(self, db:Session, post_id: int, reqBody: PostReq):
        oldPost = db.get(Post, post_id)
        if not oldPost:
            raise False
        
        dictToUpdate = asdict(reqBody)
        oldPost.sqlmodel_update(dictToUpdate)
        db.add(oldPost)
        db.commit()
        db.refresh(oldPost)
        return oldPost
    
    def delete_post(self, db:Session, post_id: int):
        post = db.get(Post, post_id)
        if not post:
            return False
        db.delete(post)
        db.commit()
        return True