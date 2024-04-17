from fastapi import Request, APIRouter
from database.postservice import get_exact_hashtag_db, get_some_hashtags_db
hashtag_router = APIRouter(prefix='/hashtag', tags=['Управление хэштегами'])

# получить хэщтеги
@hashtag_router.get('/api')
async def get_some_hashtags(size: int = 20, page: int = 1):
    pass
# получить хэштег
@app.get('/api/hastag/<str:hashtag_name>')
async def get_exact_hashtag(request: Request):
    pass