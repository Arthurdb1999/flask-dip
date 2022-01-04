from app.services.UserService import UserService
from app.tests.ioc import register_ioc

# FIX
def test_get_user_by_kwargs():
    register_ioc()
    service = UserService()
    users = service.get(id=1, name="Arthur")

    assert len(users) == 1
    assert users[0].name == "Arthur"