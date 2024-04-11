# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from fastapi import APIRouter, Depends, HTTPException, Request
# from pydantic import BaseModel
# from typing import List, Dict
# from database.userservice import register_user_db, login_user_db
# from ..users_api import RegisterValidator
from fastapi import Request, APIRouter
from pydantic import BaseModel
from typing import List, Dict
from database.userservice import register_user_db, check_user_db, check_user_password_db, change_user_data, profile_info_db

import re
user_router = APIRouter(prefix='/users', tags=['Управления с пользователями'])

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
#
#
# # Запрос для регистрации
# @user_router.post('/register')
# async def register_user(data: RegisterValidator):
#     result = register_user_db(**data.model_dump())
#
#     if result:
#         return {'message': result}
#     else:
#         return {'message': 'Такой пользователь уже имеется'}
#
#
# # Запрос для логина
# # main.py
# @user_router.post('/login')
# async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = login_user_db(form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(status_code=401, detail='Неверный номер или пароль')
#     else:
#         return user
regex = re.compile(r'([A-za-z0-9]+[.-_])*[A-za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z]a-z]{2,})+')

def mail_checker(email):
    if re.fullmatch(regex, email):
        return True
    return False
class User(BaseModel):
    username: str
    email: str
    phone_number: str
    password: str
    user_city: str
@user_router.post("/api/registration")
def register_user(user_model: User):
    user_data = dict(user_model)
    mail_validation = mail_checker(user_model.email)
    if mail_validation:
        try:
            reg_user = register_user_db(**user_data)
            return {"status": 1, "user_id": reg_user}
        except Exception as e:
            return {"status":0, "message": e}
    return {"status":0, "message": "Invalid email"}








