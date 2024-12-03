import logging

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from src.project.services.auth import get_current_user, create_access_token, get_password_hash, verify_password
from src.project.models.user import User
from src.project.schemas.user import UserCreate, UserLogin, Token
from src.project.crud.user import get_user_by_login
from src.project.config import get_session

app = FastAPI()

# проблема с CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    # Здесь можно инициализировать базу данных, если нужно
    pass

# зарегистрировать пользователя
@app.post("/register", response_model=Token)
async def register(user_data: UserCreate, db: AsyncSession = Depends(get_session)):
    user = await get_user_by_login(db, user_data.login)
    if user:
        raise HTTPException(status_code=409, detail="Пользователь уже существует")

    hashed_password = get_password_hash(user_data.password)
    new_user = User(login=user_data.login, hashed_password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    access_token = create_access_token(data={"login": new_user.login})
    return {"access_token": access_token, "token_type": "bearer"}

# авторизация пользователя
@app.post("/auth", response_model=Token)
async def login(user_data: UserLogin, db: AsyncSession = Depends(get_session)):
    user = await get_user_by_login(db, user_data.login)
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Неверный логин или пароль")

    access_token = create_access_token(data={"login": user.login})
    return {"access_token": access_token, "token_type": "bearer"}
