from flask import Flask
from config import Config

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    if test_config:
        from app.tests.ioc import register_ioc
        register_ioc()
        app.config.update(test_config)
    else:
        from app.ioc import register_ioc
        from app.database import db_session, init_db
        from app.mapper import run_mappers

        register_ioc()

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
