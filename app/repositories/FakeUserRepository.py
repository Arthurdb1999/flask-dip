from app.repositories.AbstractUserRepository import AbstractUserRepository
from app.domains.User import User
from typing import List

class FakeUserRepository(AbstractUserRepository):
    def __init__(self, users: List[User]):
        self._users = list(users)

    def add(self, user: User):
        self._users.append(user)
        return user

    def get(self, **kwargs):
        return [user for user in self._users if all(getattr(user, key) == value for key, value in kwargs.items())]