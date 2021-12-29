from dataclasses import dataclass
from app.database import db_session

@dataclass
class User(object):
    query = db_session.query_property()

    id: int
    name: str
    ativo: bool = True