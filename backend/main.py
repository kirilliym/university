from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer  # Добавьте этот импорт
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from pydantic import BaseModel
from models import User, Base
from config import get_session, engine
from fastapi.middleware.cors import CORSMiddleware

# Создаем приложение FastAPI
app = FastAPI()


# Разрешаем CORS для определённых источников
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Укажите ваш фронтенд адрес
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все методы (GET, POST, PUT, DELETE и т.д.)
    allow_headers=["*"],  # Разрешаем любые заголовки
)


# Определение схемы Bearer для получения токена
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth")

# Настройки для JWT
SECRET_KEY = "d966aeeb45d5a75e2c2267522d572e1e1d3bbbee3b56098190064e57555bfc25"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Контекст для хэширования паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Pydantic-модели для обработки запросов
class UserCreate(BaseModel):
    login: str
    password: str

class UserLogin(BaseModel):
    login: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    login: str

# Создаем таблицы в базе данных
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Хэширование пароля
def get_password_hash(password):
    return pwd_context.hash(password)

# Проверка пароля
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Создание JWT токена
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Получение пользователя по логину
async def get_user_by_login(db: AsyncSession, login: str):
    query = select(User).filter(User.login == login)
    result = await db.execute(query)
    return result.scalars().first()

# Регистрация пользователя
@app.post("/register", response_model=Token)
async def register(user_data: UserCreate, db: AsyncSession = Depends(get_session)):
    user = await get_user_by_login(db, user_data.login)
    if user:
        raise HTTPException(status_code=400, detail="Пользователь уже существует")

    hashed_password = get_password_hash(user_data.password)
    new_user = User(login=user_data.login, hashed_password=hashed_password)

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    access_token = create_access_token(data={"login": new_user.login})
    return {"access_token": access_token, "token_type": "bearer"}

# Авторизация пользователя
@app.post("/auth", response_model=Token)
async def login(user_data: UserLogin, db: AsyncSession = Depends(get_session)):
    user = await get_user_by_login(db, user_data.login)
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Неверный логин или пароль")

    access_token = create_access_token(data={"login": user.login})
    return {"access_token": access_token, "token_type": "bearer"}

# Верификация токена и извлечение пользователя
async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Не удалось подтвердить учетные данные",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        login: str = payload.get("login")
        if login is None:
            raise credentials_exception
        token_data = TokenData(login=login)
    except JWTError:
        raise credentials_exception

    user = await get_user_by_login(db, token_data.login)
    if user is None:
        raise credentials_exception
    return user

# Пример защищенного маршрута
@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return {"login": current_user.login}
