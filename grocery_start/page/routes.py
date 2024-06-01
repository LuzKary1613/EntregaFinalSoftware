from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from datetime import datetime
from .models import db, Item
import requests

# Crear un blueprint llamado 'main'
main = Blueprint('main', __name__)

# Ruta para la página principal que muestra la lista de ítems
@main.route('/')
def index():
    currency = request.args.get('currency', 'USD')  # Obtener la moneda seleccionada de los parámetros de la URL
    items = Item.query.all()  # Obtener todos los ítems de la base de datos
    
    if currency != 'USD':
        items = convert_items_currency(items, currency)  # Convertir los precios si la moneda no es USD
        
    return render_template('index.html', items=items)  # Renderizar la plantilla con los ítems

# Función para convertir los precios de los ítems a la moneda seleccionada
def convert_items_currency(items, target_currency):
    api_key = 'b038a7d1fb6144b0aefc8bf6b384a9d9'  # Clave de la API para obtener tasas de cambio
    response = requests.get(f'https://openexchangerates.org/api/latest.json?app_id={api_key}&symbols={target_currency}')
    data = response.json()
    rate = data['rates'].get(target_currency, 1)  # Obtener la tasa de cambio
    
    for item in items:
        item.price = float(item.price) * rate  # Convertir el precio
        item.price = round(item.price, 2)  # Redondear el precio
        
    return items

# Ruta para obtener todos los ítems en formato JSON
@main.route('/item', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])

# Ruta para agregar un nuevo ítem desde una solicitud POST
@main.route('/item', methods=['POST'])
def add_item():
    data = request.json
    item = Item(
        sku=data['sku'],
        name=data['name'],
        description=data['description'],
        price=float(data['price']),
        quantity=int(data['quantity']),
        expiration_date=datetime.strptime(data['expiration_date'], '%Y-%m-%d')
    )
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

# Ruta para obtener un ítem específico por SKU en formato JSON
@main.route('/item/<sku>', methods=['GET'])
def get_item(sku):
    item = Item.query.filter_by(sku=sku).first_or_404()
    return jsonify(item.to_dict())

# Ruta para eliminar un ítem específico por SKU
@main.route('/item/<sku>', methods=['DELETE', 'POST'])
def delete_item(sku):
    item = Item.query.filter_by(sku=sku).first_or_404()
    if request.method == 'DELETE':
        db.session.delete(item)
        db.session.commit()
        return '', 204  # Devuelve sin contenido cuando se elimina
    elif request.method == 'POST' and request.form.get('_method') == 'DELETE':
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for('main.index'))  # Redirige a la página principal cuando se usa un formulario

# Ruta para convertir el precio de un ítem específico a una moneda dada
@main.route('/item/<sku>/convert', methods=['GET'])
def convert_currency(sku):
    currency = request.args.get('currency', 'USD')
    item = Item.query.filter_by(sku=sku).first_or_404()
    converted_price = convert_to_currency(float(item.price), currency)
    return jsonify({'name': item.name, 'price': converted_price, 'currency': currency})

# Función para convertir el precio a una moneda específica
def convert_to_currency(price, target_currency):
    api_key = 'd2afac636cc648438f922e18398c6ed7'
    response = requests.get(f'https://openexchangerates.org/api/latest.json?app_id={api_key}&symbols={target_currency}')
    data = response.json()
    rate = data['rates'].get(target_currency, 1)
    return round(price * rate, 2)

# Ruta para mostrar y procesar el formulario de agregar ítem
@main.route('/add_item', methods=['GET', 'POST'])
def add_item_view():
    if request.method == 'POST':
        sku = request.form['sku']
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        quantity = request.form['quantity']
        expiration_date = request.form['expiration_date']

        item = Item(
            sku=sku,
            name=name,
            description=description,
            price=float(price),
            quantity=int(quantity),
            expiration_date=datetime.strptime(expiration_date, '%Y-%m-%d')
        )
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('main.index'))
    
    return render_template('add_item.html')

# Ruta para mostrar y procesar el formulario de editar ítem
@main.route('/edit_item', methods=['GET', 'POST'])
def edit_item():
    sku = request.args.get('sku')
    item = Item.query.filter_by(sku=sku).first()
    if request.method == 'POST':
        item.name = request.form['name']
        item.description = request.form['description']
        item.price = float(request.form['price'])
        item.quantity = int(request.form['quantity'])
        item.expiration_date = datetime.strptime(request.form['expiration_date'], '%Y-%m-%d')
        db.session.commit()
        return redirect(url_for('main.index'))
    
    return render_template('edit_item.html', item=item)
