from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, registry
import os

engine = create_engine(f"{os.environ.get('DATABASE_URL')}")
registry = registry()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
def init_db():
    registry.metadata.create_all(bind=engine)