from app.domains.User import User
from app.entities.User import user_table
from app.database import registry

def run_mappers():  
    registry.map_imperatively(User, user_table)
