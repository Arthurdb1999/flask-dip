from abc import ABC, abstractmethod
from app.domains.User import User
from typing import List


class AbstractUserRepository(ABC):
    @abstractmethod  
    def add(self, user: User) -> User:
        raise NotImplementedError
    
    @abstractmethod
    def get(self, column, value) -> List[User]:
        raise NotImplementedError