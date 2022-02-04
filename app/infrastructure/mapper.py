from app.domain.user.user import User
from app.infrastructure.user.sqlalchemy_user_entity import user_table
from app.infrastructure.database import registry

def run_mappers():
    registry.map_imperatively(User, user_table)
