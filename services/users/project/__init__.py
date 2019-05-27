# services/users/project/__init__.py

import os
from flask import Flask
# from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy


# instantiate the app
# app = Flask(__name__)

# api = Api(app)

# set config
# app.config.from_object('project.config.DevelopmentConfig')  # new
# app_settings = os.getenv('APP_SETTINGS')  # new
# app.config.from_object(app_settings)      # new

# instantiate the db
db = SQLAlchemy()  # new

# print(app.config, file=sys.stderr)


def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app

# class UsersPing(Resource):
#     def get(self):
#         return {
#         'status': 'success',
#         'message': 'pong!'
#     }


# api.add_resource(UsersPing, '/users/ping')
