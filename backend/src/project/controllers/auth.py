from fastapi import APIRouter, HTTPException, status, Depends

from project.instances.user import UserResponse, UserAuth
from project.instances.token import TokenResponse
from project.core.exceptions import UserNotFound, UserAlreadyExists
from project.controllers.depences import database, user_repo
from project.utils.jwt_utils import JwtUtil

auth_router = APIRouter()


@auth_router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user_dto: UserAuth) -> TokenResponse:
    try:
        async with database.session() as session:
            # Хеширование пароля
            user_dto.password = JwtUtil.hash_password(password=user_dto.password)
            # Создание нового пользователя
            new_user = await user_repo.create_user(session=session, user=user_dto)
    except UserAlreadyExists as error:
        # Обработка ошибки, если пользователь уже существует
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    # Генерация JWT токена
    token = JwtUtil.token_from_login(user_dto.login)

    # Возвращаем объект, который соответствует TokenResponse
    return TokenResponse(token=token)


@auth_router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
async def login_user(user_dto: UserAuth) -> TokenResponse:
    async with database.session() as session:
        # Проверяем, существует ли пользователь с таким логином
        existing_user = await user_repo.get_user_by_login(session=session, login=user_dto.login)

        if not existing_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        # Проверяем, совпадает ли введённый пароль с хешированным паролем в базе данных
        if not JwtUtil.verify_password(plain_password=user_dto.password, hashed_password=existing_user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")

        # Генерация JWT токена для аутентифицированного пользователя
        token = JwtUtil.token_from_login(user_dto.login)

        # Возвращаем объект TokenResponse с токеном
        return TokenResponse(token=token)

