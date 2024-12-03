from project.infrastructure.postgres.repository.user_repo import UserRepository
from project.infrastructure.postgres.database import PostgresDatabase


user_repo = UserRepository()
database = PostgresDatabase()
