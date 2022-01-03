from flask import jsonify, request, Blueprint
from app.domains.User import User
from app.serializers.User import user_schema
from app.database import db_session
from app.repositories.SQLAlchemyUserRepository import SQLAlchemyUserRepository
from app.services.UserService import UserService

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