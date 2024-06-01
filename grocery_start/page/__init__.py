from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_class='config.Config', init_db=False):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    if init_db:
        with app.app_context():
            db.create_all()  # Solo crea las tablas si se especifica

    from . import routes  # Asegúrate de que esta importación no cause problemas
    app.register_blueprint(routes.main)
    return app

