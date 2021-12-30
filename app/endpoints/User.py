from flask import jsonify, request, Blueprint
from app.domains.User import User
from app.serializers.User import user_schema
from app.database import db_session
from app.repositories.SQLAlchemyUserRepository import SQLAlchemyUserRepository

bp = Blueprint("user_routes", __name__)

@bp.route('/createUser', methods=["POST"])
def create_user():
    user = User(id=request.json['id'], name=request.json['name'])

    user_exists = SQLAlchemyUserRepository(db_session).get(name=user.name)
    if len(user_exists) > 0:
        return jsonify(error="Usuário já cadastrado!"), 400

    insertedUser = SQLAlchemyUserRepository(db_session).add(user)
    db_session.commit()

    serialized_user = user_schema.dump(insertedUser)

    return jsonify(insertedUser=serialized_user)