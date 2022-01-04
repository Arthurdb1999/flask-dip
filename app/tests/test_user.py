from app.services.UserService import UserService
from app.repositories.FakeUserRepository import FakeUserRepository
from app.domains.User import User
from app import create_app
import pytest


@pytest.fixture(scope="session")
def client():
    app = create_app({'TESTING': True})

    with app.test_client() as client:
        yield client

def test_get_user_by_kwargs(client):
    service = UserService()
    users = service.get(id=1, name="Arthur")

    assert len(users) == 1
    assert users[0].name == "Arthur"

def test_add_user(client):
    service = UserService()
    user = service.add(User(id=4, name="Lucas", active=False))

    assert user.name == "Lucas" and user.id == 4
    assert len(service.get(name="Lucas")) == 1

