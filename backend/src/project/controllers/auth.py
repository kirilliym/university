from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt

from project.core.config import settings
from project.instances.user import IsAdminInstance, UserResponse, UserAuth
from project.instances.token import TokenResponse, Token
from project.core.exceptions import UserNotFound, UserAlreadyExists
from project.controllers.depences import database, user_repo, get_user_from_token, check_for_admin_permissions
from project.utils.jwt_utils import JwtUtil


auth_router = APIRouter()


@auth_router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user_dto: UserAuth) -> TokenResponse:
    try:
        async with database.session() as session:
            user_dto.password = JwtUtil.hash_password(password=user_dto.password)
            new_user = await user_repo.create_user(session=session, user=user_dto)
    except UserAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    token = JwtUtil.token_from_login(user_dto.login)

    return TokenResponse(token=token)


@auth_router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
async def login_user(user_dto: UserAuth) -> TokenResponse:
    async with database.session() as session:
        existing_user = await user_repo.get_user_by_login(session=session, login=user_dto.login)

        if not existing_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        if not JwtUtil.verify_password(plain_password=user_dto.password, hashed_password=existing_user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")

        token = JwtUtil.token_from_login(user_dto.login)

        return TokenResponse(token=token)


@auth_router.get("/isadmin", response_model=IsAdminInstance, status_code=status.HTTP_200_OK)
async def is_admin(user: UserResponse = Depends(get_user_from_token)) -> IsAdminInstance:
    return IsAdminInstance(isadmin=user.isadmin)


@auth_router.post("/setadmin", status_code=status.HTTP_200_OK)
async def set_admin(login: str, flag: bool = True, user: UserResponse = Depends(get_user_from_token)):
    check_for_admin_permissions(user)
    try:
        async with database.session() as session:
            await user_repo.set_admin(session=session, login=login, is_admin=flag)
    except UserNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    


@auth_router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    try:
        async with database.session() as session:
            user = await user_repo.get_user_by_login(session=session, login=form_data.username)
        
        if not user:
            raise UserNotFound(_id=-1)

        if not JwtUtil.verify_password(plain_password=form_data.password, hashed_password=user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Неверный пароль",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except UserNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=e.message,
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    token_data = {"login": user.login}

    to_encode = token_data.copy()
    if access_token_expires:
        expire = datetime.now(timezone.utc) + access_token_expires
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"expire": expire.timestamp()})
    access_token = jwt.encode(
        claims=to_encode,
        key=settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )

    return Token(access_token=access_token, token_type="bearer")