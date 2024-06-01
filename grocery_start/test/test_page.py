import pytest
from page import create_app, db
from page.models import Item
from datetime import datetime

# Fixture para crear la aplicación con el contexto de prueba
@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.config['TESTING'] = True  # Configura la aplicación en modo de prueba
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:1234@localhost:5432/grocery_db'
    with app.app_context():
        db.create_all()  # Crea todas las tablas en la base de datos
        yield app  # Proporciona la aplicación a las pruebas
        db.drop_all()  # Elimina todas las tablas después de las pruebas

# Fixture para obtener el cliente de prueba
@pytest.fixture(scope='module')
def client(app):
    return app.test_client()

# Fixture para inicializar la base de datos antes de cada prueba
@pytest.fixture(scope='function')
def init_database(app):
    with app.app_context():
        db.create_all()  # Crea todas las tablas en la base de datos
        # Limpia la base de datos antes de cada prueba para evitar UniqueViolation
        db.session.query(Item).delete()
        # Agrega un ítem inicial a la base de datos
        item1 = Item(sku='A123', name='Apples', description='Fresh apples', price=1.99, quantity=10, expiration_date=datetime(2023, 9, 15))
        db.session.add(item1)
        db.session.commit()
        yield db  # Proporciona la base de datos a las pruebas
        db.session.remove()  # Remueve la sesión de la base de datos
        db.drop_all()  # Elimina todas las tablas después de cada prueba

# Prueba para verificar que la página principal se carga correctamente
def test_index(client, init_database):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Apples' in response.data

# Prueba para agregar un nuevo ítem
def test_add_item(client, init_database):
    response = client.post('/item', json={
        'sku': 'B456',
        'name': 'Bananas',
        'description': 'Fresh bananas',
        'price': 2.99,
        'quantity': 20,
        'expiration_date': '2023-09-16'
    })
    assert response.status_code == 201
    assert b'Bananas' in response.data

# Prueba para obtener un ítem específico por SKU
def test_get_item(client, init_database):
    response = client.get('/item/A123')
    assert response.status_code == 200
    assert b'Apples' in response.data

# Prueba para eliminar un ítem específico por SKU
def test_delete_item(client, init_database):
    response = client.delete('/item/A123', follow_redirects=True)
    assert response.status_code == 204

# Prueba para editar un ítem específico por SKU
def test_edit_item(client, init_database):
    response = client.post('/edit_item?sku=A123', data={
        'name': 'Green Apples',
        'description': 'Fresh green apples',
        'price': '2.99',
        'quantity': '15',
        'expiration_date': '2023-09-20'
    })
    assert response.status_code == 302
    response = client.get('/item/A123')
    assert response.status_code == 200
    assert b'Green Apples' in response.data

