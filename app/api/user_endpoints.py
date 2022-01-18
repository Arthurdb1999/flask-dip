from flask import jsonify, request, Blueprint

from app.domain.user.user import User
from app.domain.user.user_service import UserService
from app.infrastructure.user.sqlalchemy_user_serializer import user_schema
from app.infrastructure.database import db_session
from app.infrastructure.user.sqlalchemy_user_repository import SQLAlchemyUserRepository

bp = Blueprint("user_routes", __name__)

@bp.route('/createUser', methods=["POST"])
def create_user():
    user = UserDto.load_from(request)
    controller = UserController()
    return controller.create_user(user)
  

@dataclass
class UserDto(object):
    id: int
    name: str
    active: bool

    @classmethod
    def load_from (request):
        return User(id=request.json['id'], name=request.json['name'])


class UserController():
    def __init__(self, service: UserService):
        self.__service = service

    def create_user(self, userDto:UserDto):
        inserted_user = self.__service.register(user)
        if not inserted_user:
            return jsonify(error="Usuário já cadastrado!"), 400

        serialized_user = user_schema.dump(inserted_user)

        return jsonify(insertedUser=serialized_user)
    