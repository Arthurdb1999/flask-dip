from app.repositories.UserRepository import UserRepository
from app.entities.User import UserEntity
    
class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session):
        self.session = session

    def add(self, user):
        print(user)
        user_entity = UserEntity(user)
        print(user_entity)
        self.session.add(user_entity)

    def get(self, **kwargs):
        return self.session.query(UserEntity).filter_by(**kwargs).all()