from app.domain.user.user_repository import UserRepository
from app.domain.user.user import User
import inject

class UserService:

    @inject.autoparams()
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def add(self, user: User):
        return self.user_repository.add(user)

    def get(self, **kwargs):
        return self.user_repository.get(**kwargs)