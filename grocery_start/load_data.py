import csv
from datetime import datetime
from page import create_app, db
from page.models import Item

# Función para cargar datos desde un archivo CSV a la base de datos
def load_data_from_csv(filename):
    app = create_app()  # Crea una instancia de la aplicación Flask
    with app.app_context():  # Crea un contexto de aplicación para interactuar con la base de datos
        db.create_all()  # Asegúrate de que las tablas existen antes de intentar cargar los datos
        
        with open(filename, newline='') as csvfile:  # Abre el archivo CSV
            reader = csv.DictReader(csvfile)  # Crea un lector de CSV que interpreta cada fila como un diccionario
            for row in reader:  # Itera sobre cada fila del archivo CSV
                # Crea una instancia de Item con los datos del CSV
                item = Item(
                    sku=row['SKU'],
                    name=row['Name'],
                    description=row['Description'],
                    price=float(row['Price']),
                    quantity=int(row['Quantity']),
                    expiration_date=datetime.strptime(row['Expiration Date'], '%Y-%m-%d')
                )
                db.session.add(item)  # Añade el ítem a la sesión de la base de datos
            db.session.commit()  # Confirma todos los cambios en la base de datos
        print(f'Data loaded successfully from {filename}')  # Imprime un mensaje indicando que los datos fueron cargados exitosamente

# Ejecuta la función de carga de datos si el script se ejecuta directamente
if __name__ == '__main__':
    load_data_from_csv('sample_grocery.csv')
