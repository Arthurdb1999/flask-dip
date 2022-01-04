from abc import ABC, abstractmethod
from app.domain.user.user import User
from typing import List


class UserRepository(ABC):
    @abstractmethod  
    def add(self, user: User) -> User:
        raise NotImplementedError
    
    @abstractmethod
    def get(self, column, value) -> List[User]:
        raise NotImplementedError