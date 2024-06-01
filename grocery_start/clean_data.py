import os
from page import create_app, db
from page.models import Item

# Función para limpiar la base de datos
def clean_database():
    app = create_app()  # Crea una instancia de la aplicación Flask
    with app.app_context():  # Crea un contexto de aplicación para interactuar con la base de datos
        if db.engine.dialect.has_table(db.engine.connect(), 'items'):  # Verifica si la tabla 'items' existe
            db.session.query(Item).delete()  # Elimina todos los registros de la tabla 'items'
            db.session.commit()  # Confirma los cambios en la base de datos
            print('Table "items" cleaned.')  # Imprime un mensaje indicando que la tabla fue limpiada
        else:
            print('Table "items" does not exist.')  # Imprime un mensaje si la tabla no existe

# Ejecuta la función de limpieza de la base de datos si el script se ejecuta directamente
if __name__ == '__main__':
    clean_database()
