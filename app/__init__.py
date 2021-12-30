from flask import Flask
from config import Config
from app.database import db_session, init_db
from app.models import run_mappers

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.cli.command('db_create')
    def db_create():
        init_db()
        run_mappers()
        print('Database created')


    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()


    from app.endpoints import User
    app.register_blueprint(User.bp)


    return app
