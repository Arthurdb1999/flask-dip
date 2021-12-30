from sqlalchemy import Table, Column, Integer, String, Boolean
from app.database import registry
from sqlalchemy.orm import declarative_base
from app.domains.User import User
from dataclasses import dataclass

Base = declarative_base()

user_table = Table(
    'user',
    registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column("ativo", Boolean)
)

@dataclass
class UserEntity(User, Base):
    __table__ = user_table