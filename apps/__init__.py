from flask import Flask

from .user import user as user_blueprint
from .lab import lab as lab_blueprint


def create_app(config=None):
    app = Flask(__name__)
    
    app.config.from_envvar('NEU_SETTINGS', silent=True)
    
    if config:
        app.config.from_object(config)

    app.register_blueprint(user_blueprint, url_prefix='/user')
    app.register_blueprint(lab_blueprint, url_prefix='/lab')

    return app