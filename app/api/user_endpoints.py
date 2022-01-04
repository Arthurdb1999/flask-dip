from flask import jsonify, request, Blueprint

from app.domain.user.user import User
from app.domain.user.user_service import UserService
from app.infrastructure.user.sqlalchemy_user_serializer import user_schema
from app.infrastructure.database import db_session
from app.infrastructure.user.sqlalchemy_user_repository import SQLAlchemyUserRepository

bp = Blueprint("user_routes", __name__)

@bp.route('/createUser', methods=["POST"])
def create_user():
    service = UserService()
    user = User(id=request.json['id'], name=request.json['name'])

    user_exists = service.get(name=user.name)
    if len(user_exists) > 0:
        return jsonify(error="Usuário já cadastrado!"), 400

    insertedUser = service.add(user)
    db_session.commit()

    serialized_user = user_schema.dump(insertedUser)

    return jsonify(insertedUser=serialized_user)