from pydantic import BaseModel, Field, ConfigDict




class UserResponse(BaseModel):
    password: str
    login: str
    avatar: str | None


class UserAuth(BaseModel):
    login: str
    password: str
