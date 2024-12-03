import logging

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from pydantic import BaseModel
from backend.src.models.user import User, Base
from backend.src.config import get_session, engine
from fastapi.middleware.cors import CORSMiddleware




logger = logging.getLogger(__name__)
app = FastAPI()


# проблема с CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth")
SECRET_KEY = "d966aeeb45d5a75e2c2267522d572e1e1d3bbbee3b56098190064e57555bfc25"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# запросы
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

# хэширование пароля
def get_password_hash(password):
    return pwd_context.hash(password)

# проверка пароля
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# создание JWT токена
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# верификация токена и извлечение пользователя
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

# получение пользователя по логину
async def get_user_by_login(db: AsyncSession, login: str) -> dict:
    query = select(User).filter(User.login == login)
    result = await db.execute(query)
    return result.scalars().first()

# cоздаем таблицы в базе данных
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# регистрация пользователя
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
