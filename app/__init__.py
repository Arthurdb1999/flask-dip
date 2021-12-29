from flask import Flask
from config import Config
from app.database import db_session, init_db
from app.models import run_mappers

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db()
    run_mappers()


    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()


    from app.routes import User
    app.register_blueprint(User.bp)


    return app
