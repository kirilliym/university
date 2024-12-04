from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from project.infrastructure.postgres.database import Base


class User(Base):
    __tablename__ = "users"

    login: Mapped[str] = mapped_column(nullable=False, primary_key=True, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    avatar: Mapped[str] = mapped_column(nullable=True)