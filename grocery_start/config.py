class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:1234@localhost:5432/grocery_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Confirmar que esto se está aplicando
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
