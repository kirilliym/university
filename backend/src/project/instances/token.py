from pydantic import BaseModel


class TokenResponse(BaseModel):
    token: str

class Token(BaseModel):
    access_token: str
    token_type: str