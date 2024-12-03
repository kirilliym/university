from pydantic import BaseModel

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
