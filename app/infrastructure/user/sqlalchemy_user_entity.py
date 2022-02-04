from sqlalchemy import Table, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from dataclasses import dataclass

from app.infrastructure.database import registry
from app.domain.user.user import User

Base = declarative_base()

user_table = Table(
    'user',
    registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column("active", Boolean)
)

class SQLAlchemyUserEntity(User, Base):
    __table__ = user_table