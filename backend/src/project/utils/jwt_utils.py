from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

from project.core.config import settings


class JwtUtil:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

    @staticmethod
    def hash_password(password: str) -> str:
        return JwtUtil.pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return JwtUtil.pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def token_from_login(login: str) -> str:
        expire = datetime.now() + timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
        
        expire_str = expire.isoformat()

        return jwt.encode(claims={"login": login, "expire": expire_str}, key=settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

    @staticmethod
    def login_from_token(token: str) -> str:
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            login = decoded_token.get("login")
            return login
        except JWTError:
            return None
