from app.repositories.AbstractUserRepository import AbstractUserRepository
from app.repositories.FakeUserRepository import FakeUserRepository
import inject

def ioc_config(binder):
    binder.bind(AbstractUserRepository, FakeUserRepository(
        User(id=1, name="Arthur"),
        User(id=2, name="Pedro"),
        User(id=3, name="João")
    ))

def register_ioc():
    if not inject.is_configured():
        inject.configure(ioc_config)