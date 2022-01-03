from app.repositories.AbstractUserRepository import AbstractUserRepository
from app.repositories.SQLAlchemyUserRepository import SQLAlchemyUserRepository
from app.database import db_session
import inject

def ioc_config(binder):
    binder.bind(AbstractUserRepository, SQLAlchemyUserRepository(db_session))


def register_ioc():
    inject.configure(ioc_config)