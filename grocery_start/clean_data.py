import os
from page import create_app, db
from page.models import Item

def clean_database():
    app = create_app()
    with app.app_context():
        if db.engine.dialect.has_table(db.engine.connect(), 'items'):
            db.session.query(Item).delete()
            db.session.commit()
            print('Table "items" cleaned.')
        else:
            print('Table "items" does not exist.')

if __name__ == '__main__':
    clean_database()
