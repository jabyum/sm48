from fastapi import Request, APIRouter
from database.postservice import get_all_or_exact_post_db, change_post_text_db, delete_exact_post_db
post_router = APIRouter(prefix='/post', tags=['Управление постами'])

# получить определенный или все посты
@post_router.get('/api/posts')
async def get_all_or_exact_post(post_id:int=0):
    pass
# изменить пост
@post_router.put('/api/posts')
async def change_user_post(request: Request):
    pass
# удалить пост
@post_router.delete('/api/posts')
async def delete_user_post(request: Request):
    pass

