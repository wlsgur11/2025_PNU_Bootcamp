from app.models.post_models import Post

POST_EXPIRE = 100

'''
Type : Hashes
Key: POST#1
'''

class RedisService:
    def make_post_key(self, post_id: int) -> str:
        return f"POST#{post_id}"

    # 게시물을 캐시에서 가져오는 함수
    async def get_post(self, redis, post_id: int) -> Post | None:
        post = await redis.hgetall(self.make_post_key(post_id))
        if post is None or len(post) < 1:
            return None

        cachedPost = Post(id=0, price=0, created_at=0, published=False, title='', body='', location='')
        cachedPost.id = int(post.get('id', 0))
        cachedPost.price = int(post.get('price', 0))
        cachedPost.created_at = int(post.get('created_at', 0))
        cachedPost.published = post.get('published', '1') == '1'
        cachedPost.title = post.get('title', '')
        cachedPost.body = post.get('body', '')
        cachedPost.location = post.get('location', '')
        return cachedPost

    # 게시물을 캐시에 추가하는 함수
    async def add_post(self, redis, post: Post) -> Post:
        strKey = self.make_post_key(post.id)
        await redis.hset(strKey, "id", post.id)
        await redis.hset(strKey, "price", post.price)
        await redis.hset(strKey,"title", post.title)
        await redis.hset(strKey,"body", post.body)
        await redis.hset(strKey,"created_at", post.created_at)
        await redis.hset(strKey, "location", post.location)

        nPublished = 0
        if post.published:
            nPublished = 1
        await redis.hset(strKey,"published", nPublished)

        # await redis.hexpire(strKey, POST_EXPIRE)

    async def delete_post(self, redis, post_id: int) -> Post:
        strKey = self.make_post_key(post_id)
        await redis.delete(strKey)