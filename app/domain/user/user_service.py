from typing import TypedDict
from app.domain.user.user_repository import UserRepository
from app.domain.user.user import User
import inject

class UserService:

    @inject.autoparams()
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register(self, user: User):
        user_exists = self.user_repository.exists(name=user.name)

        if user_exists:
            return None

        insertedUser = self.user_repository.add(user)
        
        db_session.commit()



