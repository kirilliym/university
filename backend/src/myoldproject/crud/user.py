from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.project.models.user import User

async def get_user_by_login(db: AsyncSession, login: str):
    query = select(User).filter(User.login == login)
    result = await db.execute(query)
    return result.scalars().first()
