# page/routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from datetime import datetime
from .models import db, Item
import requests

main = Blueprint('main', __name__)

@main.route('/')
def index():
    currency = request.args.get('currency', 'USD')
    items = Item.query.all()
    
    if currency != 'USD':
        items = convert_items_currency(items, currency)
        
    return render_template('index.html', items=items)

def convert_items_currency(items, target_currency):
    api_key = 'd2afac636cc648438f922e18398c6ed7'
    response = requests.get(f'https://openexchangerates.org/api/latest.json?app_id={api_key}&symbols={target_currency}')
    data = response.json()
    rate = data['rates'].get(target_currency, 1)
    
    for item in items:
        item.price = float(item.price) * rate
        item.price = round(item.price, 2)
        
    return items

@main.route('/item', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])

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

@main.route('/item/<sku>', methods=['GET'])
def get_item(sku):
    item = Item.query.filter_by(sku=sku).first_or_404()
    return jsonify(item.to_dict())

#@main.route('/item/<sku>', methods=['DELETE', 'POST'])
#def delete_item(sku):
#    item = Item.query.filter_by(sku=sku).first_or_404()
#    if request.method == 'POST' and request.form.get('_method') == 'DELETE':
#        db.session.delete(item)
#        db.session.commit()
#    return redirect(url_for('main.index'))

@main.route('/item/<sku>', methods=['DELETE', 'POST'])
def delete_item(sku):
    item = Item.query.filter_by(sku=sku).first_or_404()
    if request.method == 'DELETE':
        db.session.delete(item)
        db.session.commit()
        return '', 204  # Return no content when actually deleting
    elif request.method == 'POST' and request.form.get('_method') == 'DELETE':
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for('main.index'))  # Only redirect when using forms




@main.route('/item/<sku>/convert', methods=['GET'])
def convert_currency(sku):
    currency = request.args.get('currency', 'USD')
    item = Item.query.filter_by(sku=sku).first_or_404()
    converted_price = convert_to_currency(float(item.price), currency)
    return jsonify({'name': item.name, 'price': converted_price, 'currency': currency})

def convert_to_currency(price, target_currency):
    api_key = 'd2afac636cc648438f922e18398c6ed7'
    response = requests.get(f'https://openexchangerates.org/api/latest.json?app_id={api_key}&symbols={target_currency}')
    data = response.json()
    rate = data['rates'].get(target_currency, 1)
    return round(price * rate, 2)

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
