from typing import List

from app.domain.user.user_repository import UserRepository
from app.domain.user.user import User

class FakeUserRepository(UserRepository):
    def __init__(self, users: List[User]):
        self._users = list(users)

    def add(self, user: User):
        self._users.append(user)
        return user

    def get(self, **kwargs):
        return [user for user in self._users if all(getattr(user, key) == value for key, value in kwargs.items())]