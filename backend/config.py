import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# Получение URL базы данных из переменных окружения
DATABASE_URL = os.getenv("DATABASE_URL")

# Создание асинхронного движка SQLAlchemy
engine = create_async_engine(DATABASE_URL, echo=True)

# Создание фабрики сессий
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Получение сессии
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
