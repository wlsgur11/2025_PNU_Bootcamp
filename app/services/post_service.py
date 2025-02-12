from dataclasses import asdict
from sqlmodel import Session, select, col
import time
from app.models.post_models import *
from fastapi import BackgroundTasks, UploadFile


class PostService:
    def get_post(self, db: Session, post_id: int):
        post = db.get(Post, post_id)
        return post
    
    def get_posts(self, db:Session, page: int=1, limit:int=10,search:str|None=None):
        if limit > 10:
            limit = 10
        nOffset = (page-1) * limit
        sql = select(Post)
        if search is not None:
            sql = sql.where(col(Post.title).contains(search))
        sql = sql.offset(nOffset).limit(limit)

        posts = db.exec(sql).all()
        return posts
        
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
        
        dictToUpdate = asdict(post)
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
    
    # def get_myposts(self, db:Session, page: int=1, limit:int=10):
    #     if limit > 10:
    #         limit = 10
    #     nOffset = (page-1) * limit
    #     posts = db.exec(
    #         select(Post).offset(nOffset).limit(limit)
    #         # .filter(userDict.id == author_id)
    #     ).all()
    #     return posts
    