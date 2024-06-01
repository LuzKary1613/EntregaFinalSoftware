import pytest
from page import create_app, db
from page.models import Item
from datetime import datetime

@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:1234@localhost:5432/grocery_db'
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture(scope='module')
def client(app):
    return app.test_client()

@pytest.fixture(scope='function')
def init_database(app):
    with app.app_context():
        db.create_all()
        # Clean the database before each test to avoid UniqueViolation
        db.session.query(Item).delete()
        item1 = Item(sku='A123', name='Apples', description='Fresh apples', price=1.99, quantity=10, expiration_date=datetime(2023, 9, 15))
        db.session.add(item1)
        db.session.commit()
        yield db
        db.session.remove()
        db.drop_all()

def test_index(client, init_database):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Apples' in response.data

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

def test_get_item(client, init_database):
    response = client.get('/item/A123')
    assert response.status_code == 200
    assert b'Apples' in response.data

def test_delete_item(client, init_database):
    response = client.delete('/item/A123', follow_redirects=True)
    assert response.status_code == 204


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
