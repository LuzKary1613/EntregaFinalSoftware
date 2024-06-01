# Clase de configuración base para la aplicación
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:1234@localhost:5432/grocery_db'  # URI de la base de datos PostgreSQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactiva el seguimiento de modificaciones de SQLAlchemy

# Clase de configuración para pruebas, hereda de Config
class TestConfig(Config):
    TESTING = True  # Activa el modo de prueba
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Usa una base de datos SQLite en memoria para pruebas
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactiva el seguimiento de modificaciones de SQLAlchemy
    SQLALCHEMY_ECHO = True  # Activa el eco de SQLAlchemy para ver las consultas generadas
