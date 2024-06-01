from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Inicializa la extensión SQLAlchemy

class Item(db.Model):
    __tablename__ = 'items'  # Nombre de la tabla en la base de datos
    
    id = db.Column(db.Integer, primary_key=True)  # Columna ID como clave primaria
    sku = db.Column(db.String(50), unique=True, nullable=False)  # Columna SKU, única y no nula
    name = db.Column(db.String(100), nullable=False)  # Columna Name, no nula
    description = db.Column(db.Text, nullable=True)  # Columna Description, puede ser nula
    price = db.Column(db.Numeric(10, 2), nullable=False)  # Columna Price, no nula
    quantity = db.Column(db.Integer, nullable=False)  # Columna Quantity, no nula
    expiration_date = db.Column(db.Date, nullable=False)  # Columna Expiration Date, no nula
    
    def to_dict(self):
        return {
            'sku': self.sku,
            'name': self.name,
            'description': self.description,
            'price': float(self.price),
            'quantity': self.quantity,
            'expiration_date': self.expiration_date.isoformat()
        }  # Convierte el objeto Item en un diccionario
