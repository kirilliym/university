from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.instances.user import UserResponse, UserAuth
from project.infrastructure.postgres.models import User
from project.core.exceptions import UserNotFound, UserAlreadyExists


class UserRepository:
    _collection: Type[User] = User

    async def check_connection(self, session: AsyncSession) -> bool:
        query = "select 1;"
        result = await session.scalar(text(query))
        return True if result else False

################################################################################################

    async def get_user_by_login(
        self,
        session: AsyncSession,
        login: str,
    ) -> User:
        query = select(self._collection).where(self._collection.login == login)
        user = await session.scalar(query)

        return user


################################################################################################

    async def create_user(self, session: AsyncSession, user: UserAuth) -> None:
        query = (
            insert(self._collection)
            .values(user.model_dump())
            .returning(self._collection)
        )
        try:
            await session.execute(query)
            await session.commit()
        except IntegrityError:
            raise UserAlreadyExists(login=user.login)
        
  ################################################################################################

    async def is_admin(
        self,
        session: AsyncSession,
        login: str,
    ) -> bool:
        query = select(self._collection.isadmin).where(self._collection.login == login)
        result = await session.scalar(query)
        if result is None:
            raise UserNotFound(login=login)
        return result

    ################################################################################################

    async def set_admin(
        self,
        session: AsyncSession,
        login: str,
        is_admin: bool = True,
    ) -> None:
        query = (
            update(self._collection)
            .where(self._collection.login == login)
            .values(isadmin=is_admin)
        )
        result = await session.execute(query)
        if result.rowcount == 0:
            raise UserNotFound(_id=-1)
        await session.commit()