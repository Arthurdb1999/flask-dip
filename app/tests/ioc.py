import inject

from app.domain.user.user import User
from app.domain.user.user_repository import UserRepository
from app.infrastructure.user.fake_user_repository import FakeUserRepository

def ioc_config(binder):
    binder.bind(UserRepository, FakeUserRepository([
        User(id=1, name="Arthur"),
        User(id=2, name="Pedro"),
        User(id=3, name="João")
    ]))

def register_ioc():
    if not inject.is_configured():
        inject.configure(ioc_config)