from fastapi import  HTTPException, Depends, APIRouter
from app.services.post_service import PostReq, PostService, PostResp
from app.dependencies import *


router = APIRouter()

@router.post("/posts")
def create_post(post: PostReq, db = Depends(get_db_session), postService: PostService = Depends()):
    resp = postService.create_post(db, post)
    return resp

@router.get('/posts')
def get_post(page: int=1, limit: int=10, db=Depends(get_db_session), postService:PostService = Depends()) -> PostResp:
    if page < 1: page = 1
    if limit < 1: return []
    if limit > 10: limit = 10
    resp = PostResp(posts=[])
    resp.posts = postService.get_posts(db, page, limit)
    return resp

@router.get("/posts/{post_id}")
def get_post(post_id: int, db=Depends(get_db_session), postService: PostService = Depends()) -> PostResp:
    post = postService.get_post(db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Not Found")
    resp = PostResp(posts=post)
    return resp

@router.put("/posts/{post_id}")
def update_post(post_id: int, reqBody: PostReq, db=Depends(get_db_session), postService:PostService = Depends()):
    oldPost = postService.update_post(db, post_id=post_id, reqBody=reqBody)
    if not oldPost:
        raise HTTPException(status_code=404, detail="Not Found")
    return oldPost

@router.delete("/posts/{post_id}")
def delete_post(post_id: int, db=Depends(get_db_session), postService:PostService = Depends()):
    if not postService.delete_post(db, post_id=post_id):
        raise  HTTPException(status_code=404, detail="Not Found")
    return {"ok": True}