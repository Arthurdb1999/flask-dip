from flask import jsonify, request, Blueprint
from app.domains.User import User
from app.entities.User import user_schema
from app.database import db_session

bp = Blueprint("user_routes", __name__)

@bp.route('/createUser', methods=["POST", "GET"])
def create_user():
    user = User(id=request.json['id'], name=request.json['name'])

    user_exists = db_session.query(User).filter_by(name=user.name).all()
    if len(user_exists) > 0:
        return jsonify(error="Usuário já cadastrado!"), 400

    db_session.add(user)
    db_session.commit()

    serialized_user = user_schema.dump(user)

    return jsonify(insertedUser=serialized_user)