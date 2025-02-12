from fastapi import  HTTPException, Depends, APIRouter, Header
from app.services.post_service import PostReq, PostService, PostResp
from app.dependencies.sqlite_db import *
from app.dependencies.redis_db import get_redis
from app.services.redis_service import RedisService
from app.models.post_models import *
from app.dependencies.jwt_utils import JWTUtil
from typing import Annotated

router = APIRouter()

@router.post("/posts")
def create_post(post: PostReq, 
                db = Depends(get_db_session), 
                postService: PostService = Depends(),
                Authorization: Annotated[str, Header()] = None,
                jwtUtil: JWTUtil = Depends()):
    if Authorization is None:
        raise HTTPException(status_code=401, detail="bye")
    
    token = Authorization.replace('Bearer ', '')
    userDict = jwtUtil.decode_token(token)
    if userDict is None:
        raise HTTPException(status_code=401, detail="bye")
    
    resp = postService.create_post(db, post, userDict)
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
    resp = PostResp(posts=[post])
    return resp

@router.put("/posts/{post_id}")
async def update_post(post_id:int, 
            reqBody: PostReq,
            db=Depends(get_db_session),
            postService: PostService = Depends(),
            redis=Depends(get_redis),
            redisService=Depends(RedisService),
            Authorization: Annotated[str, Header()] = None,
            jwtUtil: JWTUtil = Depends()):
    if Authorization is None:
        raise HTTPException(status_code=401, detail="bye")

    token = Authorization.replace('Bearer ', '')
    userDict = jwtUtil.decode_token(token)
    if userDict is None:
        raise HTTPException(status_code=401, detail="bye")
    
    post, code = postService.update_post(db, post_id, reqBody, userDict)
    if code == RESULT_CODE.NOT_FOUND:
        raise HTTPException(status_code=404,
                            detail="Not Found")
    if code == RESULT_CODE.FAILED:
        raise HTTPException(status_code=500,
                            detail="Internal Server Error")
    if code == RESULT_CODE.USER_FAIL:
        raise HTTPException(status_code=404,
                            detail="Not Your Post")
    
    await redisService.delete_post(redis, post_id)
    return post

@router.delete("/posts/{post_id}")
async def delete_post(post_id: int, 
                      db=Depends(get_db_session), 
                      postService:PostService = Depends(),
                      redis=Depends(get_redis),
                      redisService=Depends(RedisService),
                      Authorization: Annotated[str, Header()] = None,
                      jwtUtil: JWTUtil = Depends()):
    
    if Authorization is None:
        raise HTTPException(status_code=401, detail="bye")

    token = Authorization.replace('Bearer ', '')
    userDict = jwtUtil.decode_token(token)
    if userDict is None:
        raise HTTPException(status_code=401, detail="bye")


    resultCode = postService.delete_post(db, post_id, userDict)
    if resultCode == RESULT_CODE.NOT_FOUND:
        raise HTTPException(status_code=404, detail="Not Found")
    if resultCode == RESULT_CODE.USER_FAIL:
        raise HTTPException(status_code=404,
                            detail="Not Your Post")
    await redisService.delete_post(redis, post_id)
    return {"ok": True}


@router.put("/posts/pullup/{post_id}")
async def pullup_post(post_id:int, 
            db=Depends(get_db_session),
            postService: PostService = Depends(),
            redis=Depends(get_redis),
            redisService=Depends(RedisService),
            Authorization: Annotated[str | None, Header()]=None,
            jwtUtil: JWTUtil = Depends()):

    if Authorization is None:
        raise HTTPException(status_code=401, detail="bye")

    token = Authorization.replace('Bearer ', '')
    userDict = jwtUtil.decode_token(token)
    if userDict is None:
        raise HTTPException(status_code=401, detail="bye")

    post, code = postService.pullup_post(db, post_id)
    if code == RESULT_CODE.NOT_FOUND:
        raise HTTPException(status_code=404,
                            detail="Not Found")
    if code == RESULT_CODE.FAILED:
        raise HTTPException(status_code=500,
                            detail="Internal Server Error")
    if code == RESULT_CODE.USER_FAIL:
        raise HTTPException(status_code=404,
                            detail="Not Your Post")
    
    await redisService.delete_post(redis, post_id)
    return post

# @router.get('/myposts')
# def get_post(page: int=1, 
#              limit: int=10, 
#              db=Depends(get_db_session), 
#              postService:PostService = Depends(),
#              Authorization: Annotated[str, Header()],
#              jwtUtil: JWTUtil = Depends()) -> PostResp:
    
#     token = Authorization.replace('Bearer ', '')
#     userDict = jwtUtil.decode_token(token)
#     if userDict is None:
#         raise HTTPException(status_code=401, detail="bye")
    

#     if page < 1: page = 1
#     if limit < 1: return []
#     if limit > 10: limit = 10
#     resp = PostResp(posts=[])
#     resp.posts = postService.get_posts(db, page, limit)
#     return resp