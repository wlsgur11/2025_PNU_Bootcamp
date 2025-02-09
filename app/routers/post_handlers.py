from fastapi import  HTTPException, Depends, APIRouter
from app.services.post_service import PostReq, PostService, PostResp
from app.dependencies.sqlite_db import *
from app.dependencies.redis_db import get_redis
from app.services.redis_service import RedisService
from app.models.post_models import *


router = APIRouter()

@router.post("/posts")
def create_post(post: PostReq, 
                db = Depends(get_db_session), 
                postService: PostService = Depends()):
    resp = postService.create_post(db, post)
    return resp

@router.get('/posts')
def get_post(page: int=1, 
             limit: int=10, 
             db=Depends(get_db_session), 
             postService:PostService = Depends()) -> PostResp:
    if page < 1: page = 1
    if limit < 1: return []
    if limit > 10: limit = 10
    resp = PostResp(posts=[])
    resp.posts = postService.get_posts(db, page, limit)
    return resp

@router.get("/posts/{post_id}")
async def get_post(post_id: int, 
             db=Depends(get_db_session), 
             postService: PostService = Depends(),
             redis=Depends(get_redis),
             redisService=Depends(RedisService)) -> PostResp:
    
    cachedPost = await redisService.get_post(redis, post_id)
    if cachedPost is not None:
        return PostResp([cachedPost])
    
    post = postService.get_post(db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Not Found")
    
    await redisService.add_post(redis, post)
    resp = PostResp(posts=post)
    return resp

@router.put("/posts/{post_id}")
async def update_post(post_id:int, 
            reqBody: PostReq,
            db=Depends(get_db_session),
            postService: PostService = Depends(),
            redis=Depends(get_redis),
            redisService=Depends(RedisService)):
    post, code = postService.update_post(db, post_id, reqBody)
    if code == RESULT_CODE.NOT_FOUND:
        raise HTTPException(status_code=404,
                            detail="Not Found")
    if code == RESULT_CODE.FAILED:
        raise HTTPException(status_code=500,
                            detail="Internal Server Error")
    
    await redisService.delete_post(redis, post)
    return post

@router.delete("/posts/{post_id}")
async def delete_post(post_id: int, 
                      db=Depends(get_db_session), 
                      postService:PostService = Depends(),
                      redis=Depends(get_redis),
                      redisService=Depends(RedisService)):
    
    resultCode = postService.delete_post(db, post_id)
    if resultCode == RESULT_CODE.NOT_FOUND:
        raise HTTPException(status_code=404, detail="Not Found")
    await redisService.delete_post(redis, post_id)
    return {"ok": True}