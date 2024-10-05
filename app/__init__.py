from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from app.routes import auth, main, story_map, project
    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)
    app.register_blueprint(story_map.bp)
    app.register_blueprint(project.bp)

    return app

# This should be at the end to avoid circular imports
from app import models
