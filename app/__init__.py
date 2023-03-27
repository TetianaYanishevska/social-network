from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from .main import bp as main_bp
    app.register_blueprint(main_bp)
    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    return app


app = create_app()
#from .main import routes

