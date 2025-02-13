from dataclasses import asdict
from sqlmodel import Session, select, col
import time
from app.models.post_models import *
from app.models.user_models import *
from fastapi import BackgroundTasks, UploadFile, HTTPException
import os
from fastapi.responses import JSONResponse

class PostService:
    def get_post(self, db: Session, post_id: int):
        # post = db.get(Post, post_id)
        sql = select(Post, User).join(User).group_by(Post.id).where(Post.id==post_id)
        post, user = db.exec(sql).first()
        post.author_name = user.name
        return post

    def get_photos(self, db:Session, post_id: int, author_id: int) -> list[str]:
        photo_directory = f"./static/{author_id}/{post_id}"
        if not os.path.exists(photo_directory):
            raise HTTPException(status_code=404, detail="Not Found")

        photos = [f for f in os.listdir(photo_directory) if f.endswith(('.png', '.jpg', '.jpeg', '.gif', 'webp'))]
        if not photos:
            raise HTTPException(status_code=404, detail="No photos found")
        photo_paths = [f"/static/{author_id}/{post_id}/{photo}" for photo in photos]
        return photo_paths
            
    def get_posts(self, db:Session, page: int=1, limit:int=10,search:str|None=None):
        if limit > 10:
            limit = 10
        nOffset = (page-1) * limit
        sql = select(Post, Photo, User).join(Photo).join(User).group_by(Post.id)
        if search is not None:
            sql = sql.where(col(Post.title).contains(search))
        sql = sql.order_by(Post.updated_at.desc())
        sql = sql.offset(nOffset).limit(limit)

        posts = db.exec(sql).all()
        pwpList = PostListWithPhoto()
        for post, photo, user in posts:
            post.author_name = user.name
            pwpList.posts.append(PostWithPhoto(post=post, photo=photo))
            # print(post)
            # print()
            # print(photo)
            # print('\n\n' + ('=' * 10))

        return pwpList
        
    def create_post(self, db:Session, post: PostReq, userDict: dict):
        postModel = Post()
        postModel.title = post.title
        postModel.body = post.body
        postModel.price = post.price
        postModel.published = post.published
        postModel.created_at = int(time.time())
        postModel.location = post.location
        postModel.updated_at = postModel.created_at
        postModel.like = 0
        
        author_name = userDict.get('name', '')
        postModel.author_name = author_name

        user_id = userDict.get('id', 0)
        postModel.author_id = user_id

        db.add(postModel)
        db.commit()
        db.refresh(postModel)
        return postModel
    
    def update_post(self, db:Session, 
                    post_id: int, post: PostReq, userDict: dict) -> tuple[Post|None,RESULT_CODE]:
        oldPost = db.get(Post, post_id)
        if not oldPost:
            return (None,RESULT_CODE.NOT_FOUND)
        
        user_id = userDict.get('id', 0)

        if user_id != oldPost.author_id:
            return (None, RESULT_CODE.USER_FAIL)
        # print(post)
        # print(type(post))
        # dictToUpdate = asdict(post)
        dictToUpdate = post.dict()
        oldPost.sqlmodel_update(dictToUpdate)
        try:
            db.add(oldPost)
            db.commit()
            db.refresh(oldPost)
        except:
            return (None, RESULT_CODE.FAILED)
        return (oldPost, RESULT_CODE.SUCCESS)
    
    def delete_post(self, db: Session, post_id: int, userDict: dict) -> RESULT_CODE:
        post = db.get(Post, post_id)
        if not post:
            return RESULT_CODE.NOT_FOUND
        user_id = userDict.get('id', 0)
        if post.author_id != user_id:
            return RESULT_CODE.USER_FAIL
        try:
            db.delete(post)
            db.commit()
        except:
            return RESULT_CODE.FAILED
        return RESULT_CODE.SUCCESS
    
    def pullup_post(self, db:Session, 
                        post_id: int, userDict:dict) -> tuple[Post|None,RESULT_CODE]:
            oldPost = db.get(Post, post_id)
            if not oldPost:
                return (None,RESULT_CODE.NOT_FOUND)
            
            post = db.get(Post, post_id)
            user_id = userDict.get('id', 0)
            if post.author_id != user_id:
                return RESULT_CODE.USER_FAIL

            dictToUpdate = {
                'updated_at': int(time.time())
            }
            oldPost.sqlmodel_update(dictToUpdate)
            try:
                db.add(oldPost)
                db.commit()
                db.refresh(oldPost)
            except:
                return (None, RESULT_CODE.FAILED)
            return (oldPost, RESULT_CODE.SUCCESS)
    
    def like_post(self, db:Session, 
                        post_id: int) -> tuple[Post|None,RESULT_CODE]:
            oldPost = db.get(Post, post_id)
            if not oldPost:
                return (None,RESULT_CODE.NOT_FOUND)
            
            post = db.get(Post, post_id)
            # user_id = userDict.get('id', 0)
            # if post.author_id != user_id:
            #     return RESULT_CODE.USER_FAIL

            dictToUpdate = {
                'like': oldPost.like + 1
            }
            oldPost.sqlmodel_update(dictToUpdate)
            try:
                db.add(oldPost)
                db.commit()
                db.refresh(oldPost)
            except:
                return (None, RESULT_CODE.FAILED)
            return (oldPost, RESULT_CODE.SUCCESS)
    def unlike_post(self, db:Session, 
                        post_id: int) -> tuple[Post|None,RESULT_CODE]:
            oldPost = db.get(Post, post_id)
            if not oldPost:
                return (None,RESULT_CODE.NOT_FOUND)
            
            post = db.get(Post, post_id)
            # user_id = userDict.get('id', 0)
            # if post.author_id != user_id:
            #     return RESULT_CODE.USER_FAIL

            dictToUpdate = {
                'like': oldPost.like - 1
            }
            oldPost.sqlmodel_update(dictToUpdate)
            try:
                db.add(oldPost)
                db.commit()
                db.refresh(oldPost)
            except:
                return (None, RESULT_CODE.FAILED)
            return (oldPost, RESULT_CODE.SUCCESS)
    
    def get_region_posts(self, db:Session, page: int=1, limit:int=10,search:str|None=None):
        if limit > 10:
            limit = 10
        nOffset = (page-1) * limit
        sql = select(Post)
        if search is not None:
            sql = sql.where(col(Post.location).contains(search))
        sql = sql.order_by(Post.updated_at.desc())
        sql = sql.offset(nOffset).limit(limit)

        posts = db.exec(sql).all()
        return posts
    
    # def get_myposts(self, db:Session, page: int=1, limit:int=10):
    #     if limit > 10:
    #         limit = 10
    #     nOffset = (page-1) * limit
    #     posts = db.exec(
    #         select(Post).offset(nOffset).limit(limit)
    #         # .filter(userDict.id == author_id)
    #     ).all()
    #     return posts
    