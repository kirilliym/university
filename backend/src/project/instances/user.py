from pydantic import BaseModel, Field, ConfigDict
from datetime import date
from typing import Optional



class UserResponse(BaseModel):
    login: str
    avatar: str | None
    isadmin: bool = False


class UserAuth(BaseModel):
    login: str
    password: str

class IsAdminInstance(BaseModel):
    isadmin: bool