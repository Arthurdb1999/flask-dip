from sqlalchemy import Table, Column, Integer, String, Boolean
from app.database import registry
from flask_marshmallow import Marshmallow

ma = Marshmallow()
user_table = Table(
    'user',
    registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column("ativo", Boolean)
)

# Classe utilizada para serializar um ResultSet, que vem de uma query, para JSON.
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'ativo')


users_schema = UserSchema(many=True)
user_schema = UserSchema()