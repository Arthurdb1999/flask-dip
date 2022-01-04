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
        from app.infrastructure.ioc import register_ioc
        from app.infrastructure.database import db_session, init_db
        from app.infrastructure.mapper import run_mappers

        register_ioc()

        @app.cli.command('db_create')
        def db_create():
            init_db()
            run_mappers()
            print('Database created')


        @app.teardown_appcontext
        def shutdown_session(exception=None):
            db_session.remove()


        from app.api import user_endpoints
        app.register_blueprint(user_endpoints.bp)

    return app
