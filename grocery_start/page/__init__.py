from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Inicializa la extensión SQLAlchemy

def create_app(config_class='config.Config', init_db=False):
    app = Flask(__name__)  # Crea una instancia de la aplicación Flask
    app.config.from_object(config_class)  # Carga la configuración desde un objeto de configuración
    db.init_app(app)  # Inicializa la aplicación Flask con la extensión SQLAlchemy

    if init_db:
        with app.app_context():
            db.create_all()  # Solo crea las tablas si se especifica

    from . import routes  # Asegúrate de que esta importación no cause problemas
    app.register_blueprint(routes.main)  # Registra el blueprint de las rutas en la aplicación
    return app  # Devuelve la instancia de la aplicación Flask
