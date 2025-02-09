from dataclasses import asdict
from sqlmodel import Session, select
import time
from app.models.post_models import *


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