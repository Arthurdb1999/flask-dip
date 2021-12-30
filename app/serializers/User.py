
from flask_marshmallow import Marshmallow

ma = Marshmallow()

# Classe utilizada para serializar um ResultSet, que vem de uma query, para JSON.
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'ativo')


users_schema = UserSchema(many=True)
user_schema = UserSchema()