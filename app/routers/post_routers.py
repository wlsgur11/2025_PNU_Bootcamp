from fastapi import  HTTPException, Depends, APIRouter, Header, UploadFile, BackgroundTasks, Form
from app.services.post_service import PostReq, PostService, PostResp
from app.dependencies.sqlite_db import *
from app.dependencies.redis_db import get_redis
from app.services.redis_service import RedisService
from app.models.post_models import *
from app.dependencies.jwt_utils import JWTUtil
from typing import Annotated
import os
import time
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get('/photos/static/{author_id}/{post_id}')
async def get_post_photos(author_id: int, post_id: int) -> list[str]:
    photo_directory = f"./static/{author_id}/{post_id}"
    if not os.path.exists(photo_directory):
        raise HTTPException(status_code=404, detail="Not Found")

    photos = [f for f in os.listdir(photo_directory) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    if not photos:
        raise HTTPException(status_code=404, detail="No photos found")
    photo_paths = [f"/static/{author_id}/{post_id}/{photo}" for photo in photos]
    return JSONResponse(content=photo_paths)


def save_file(db: Session, files: dict[str, bytes], post_id: int, author_id: int):
    # 경로 설정
    base_path = os.path.join('static', str(author_id), str(post_id))
    
    # 폴더가 존재하지 않으면 생성
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    cnt = 0
    for filename in files:
        fileData = files[filename]
        exp = filename.split(".")[-1]
        strPath = os.path.join(base_path, f"{cnt}.{exp}")  # cnt.exp 형식으로 저장
        cnt += 1
        try:
            with open(strPath, 'wb') as f:
                f.write(fileData)
                photo = Photo(image_src=strPath, author_id=author_id, post_id=post_id, created_at=int(time.time()))
                db.add(photo)
            
        except Exception as e:
            print(e)
            continue
    db.commit()


@router.post("/posts")
def create_post(post: Annotated[PostReq, Form()], 
                back_tasks: BackgroundTasks,
                db = Depends(get_db_session), 
                postService: PostService = Depends(),
                Authorization: Annotated[str, Header()] = None,
                jwtUtil: JWTUtil = Depends()
                ):
    if Authorization is None:
        raise HTTPException(status_code=401, detail="bye")
    
    token = Authorization.replace('Bearer ', '')
    userDict = jwtUtil.decode_token(token)
    if userDict is None:
        raise HTTPException(status_code=401, detail="bye")
    
    resp = postService.create_post(db, post, userDict)

    if resp is not None:
        filesToSave: dict[str, bytes] = {}
        for file in post.files:
            if len(file.filename) < 1:
                continue
            filesToSave[file.filename] = file.file.read()
            back_tasks.add_task(save_file, db, filesToSave, post_id=resp.id, author_id=resp.author_id)
    return resp

@router.get('/posts')
def get_post(page: int=1, 
             limit: int=10, 
             keyword: str|None=None,
             db=Depends(get_db_session), 
             postService:PostService = Depends()) -> PostResp:
    if page < 1: page = 1
    if limit < 1: return []
    if limit > 10: limit = 10
    resp = PostResp(posts=[])
    resp.posts = postService.get_posts(db, page, limit, keyword)
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
            reqBody: Annotated[PostReq, Form()],
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

@router.put("/posts/like/{post_id}")
async def like_post(post_id:int, 
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
    
    post, code = postService.like_post(db, post_id)
    if code == RESULT_CODE.NOT_FOUND:
        raise HTTPException(status_code=404,
                            detail="Not Found")
    if code == RESULT_CODE.FAILED:
        raise HTTPException(status_code=500,
                            detail="Internal Server Error")
    
    await redisService.delete_post(redis, post_id)
    return post

@router.put("/posts/unlike/{post_id}")
async def unlike_post(post_id:int, 
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
    
    post, code = postService.unlike_post(db, post_id)
    if code == RESULT_CODE.NOT_FOUND:
        raise HTTPException(status_code=404,
                            detail="Not Found")
    if code == RESULT_CODE.FAILED:
        raise HTTPException(status_code=500,
                            detail="Internal Server Error")
    
    await redisService.delete_post(redis, post_id)
    return post

@router.get("/posts/like/{post_id}")
async def get_like(post_id: int, 
             db=Depends(get_db_session), 
             postService: PostService = Depends(),
             redis=Depends(get_redis),
             redisService=Depends(RedisService)):
    
    cachedPost = await redisService.get_post(redis, post_id)
    if cachedPost is not None:
        return PostResp([cachedPost])
    
    post = postService.get_post(db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Not Found")
    
    await redisService.add_post(redis, post)
    return post.like


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