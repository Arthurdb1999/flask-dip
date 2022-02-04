import inject

from app.domain.user.user_repository import UserRepository
from app.infrastructure.user.sqlalchemy_user_repository import SQLAlchemyUserRepository
from app.infrastructure.database import db_session

def ioc_config(binder):
    binder.bind(UserRepository, SQLAlchemyUserRepository(db_session))


def register_ioc():
    inject.configure(ioc_config)