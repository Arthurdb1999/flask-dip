from app.repositories.AbstractUserRepository import AbstractUserRepository
from app.entities.User import UserEntity
    
class SQLAlchemyUserRepository(AbstractUserRepository):
    def __init__(self, session):
        self.session = session

    def add(self, user):
        user_entity = UserEntity(id=user.id, name=user.name)
        self.session.add(user_entity)
        return user_entity

    def get(self, **kwargs):
        return self.session.query(UserEntity).filter_by(**kwargs).all()