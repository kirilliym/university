from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'schema': 'users'}

    id = Column(Integer, primary_key=True)
    login = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
