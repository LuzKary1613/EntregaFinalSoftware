import csv
from datetime import datetime
from page import create_app, db
from page.models import Item

def load_data_from_csv(filename):
    app = create_app()
    with app.app_context():
        db.create_all()  # Asegúrate de que las tablas existen antes de intentar cargar los datos
        
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item = Item(
                    sku=row['SKU'],
                    name=row['Name'],
                    description=row['Description'],
                    price=float(row['Price']),
                    quantity=int(row['Quantity']),
                    expiration_date=datetime.strptime(row['Expiration Date'], '%Y-%m-%d')
                )
                db.session.add(item)
            db.session.commit()
        print(f'Data loaded successfully from {filename}')

if __name__ == '__main__':
    load_data_from_csv('sample_grocery.csv')

