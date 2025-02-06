from fastapi import FastAPI, HTTPException, status, Depends
from dataclasses import dataclass, asdict
from sqlmodel import Field, SQLModel, Session, create_engine, select
import time
from app.services.post_service import PostReq, PostService, PostResp, Post
import os
from dotenv import load_dotenv
from app.dependencies import *

app = FastAPI()
create_db_and_tables()

# handlers

@app.post("/posts")
def create_post(post: PostReq, db = Depends(get_db_session), postService: PostService = Depends()):
    resp = postService.create_post(db, post)
    return resp

@app.get('/posts')
def get_post(page: int=1, limit: int=10, db=Depends(get_db_session), postService:PostService = Depends()) -> PostResp:
    if page < 1: page = 1
    if limit < 1: return []
    if limit > 10: limit = 10
    resp = PostResp(posts=[])
    resp.posts = postService.get_posts(db, page, limit)
    return resp

@app.get("/posts/{post_id}")
def get_post(post_id: int, db=Depends(get_db_session), postService: PostService = Depends()) -> PostResp:
    post = postService.get_post(db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Not Found")
    resp = PostResp(posts=post)
    return resp

@app.put("/posts/{post_id}")
def update_post(post_id: int, reqBody: PostReq, db=Depends(get_db_session), postService:PostService = Depends()):
    oldPost = postService.update_post(db, post_id=post_id, reqBody=reqBody)
    if not oldPost:
        raise HTTPException(status_code=404, detail="Not Found")
    return oldPost

@app.delete("/posts/{post_id}")
def delete_post(post_id: int, db=Depends(get_db_session), postService:PostService = Depends()):
    if not postService.delete_post(db, post_id=post_id):
        raise  HTTPException(status_code=404, detail="Not Found")
    return {"ok": True}