from app.domain.user.user_repository import UserRepository
from app.infrastructure.user.sqlalchemy_user_entity import SQLAlchemyUserEntity
    
class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session):
        self.session = session

    def add(self, user):
        user_entity = SQLAlchemyUserEntity(id=user.id, name=user.name)
        self.session.add(user_entity)
        return user_entity

    def get(self, **kwargs):
        return self.session.query(SQLAlchemyUserEntity).filter_by(**kwargs).all()