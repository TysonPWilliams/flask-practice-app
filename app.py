from flask import Flask, request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)

# DB Connection String
# <protocol>://<user>:<password>@<host>:<port>/<db_name>
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://bookshop_dev:123456@localhost:5432/bookshop_db'

db = SQLAlchemy(app)
ma = Marshmallow(app)


@app.route('/')
def home():
    return 'Home!'

@app.route('/init_db')
def init_db():
    db.create_all()
    return('Created Tables')

