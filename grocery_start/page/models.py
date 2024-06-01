# page/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)
    
    def to_dict(self):
        return {
            'sku': self.sku,
            'name': self.name,
            'description': self.description,
            'price': float(self.price),
            'quantity': self.quantity,
            'expiration_date': self.expiration_date.isoformat()
        }