from flask import Flask, request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow


app = Flask(__name__)

# DB Connection String
# <protocol>://<user>:<password>@<host>:<port>/<db_name>
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://bookshop_dev:123456@localhost:5432/bookshop_db'

db = SQLAlchemy(app)
# ma = Marshmallow(app)


# Model
class Book(db.Model):
    __tablename__ = "books"

    book_id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(60), nullable=False)
    stock_available = db.Column(db.Integer, db.CheckConstraint('stock_available >= 0'), default=1)

    loans = db.relationship('Loan', back_populates='book', cascade='all, delete')
    reviews = db.relationship('Review', back_populates='book', cascade='all, delete')

class Author(db.Model):
    __tablename__ = "authors"

    author_id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50))
    bio = db.Column(db.Text)

class Customer(db.Model):
    __tablename__ = "customers"

    customer_id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(12), nullable=False, unique=True)

    loans = db.relationship('Loan', back_populates='customer', cascade='all, delete')
    reviews = db.relationship('Review', back_populates='customer', cascade='all, delete')
    addresses = db.relationship('Address', back_populates='customer', cascade='all, delete')

class Loan(db.Model):
    __tablename__ = "loans"

    id = db.Column(db.Integer, primary_key=True)

    customer_id = db.Column(db.Integer, db.ForeignKey("customers.customer_id", ondelete='cascade'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("books.book_id", ondelete='cascade'), nullable = False)
    borrow_date = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable=False)

    customer = db.relationship('Customer', back_populates='loans')
    book = db.relationship('Book', back_populates='loans')

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)

    book_id = db.Column(db.Integer, db.ForeignKey("books.book_id", ondelete='cascade'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.customer_id", ondelete='cascade'), nullable=False)
    rating = db.Column(db.Integer, db.CheckConstraint('rating >= 0'), db.CheckConstraint('rating <= 5'), nullable=False)
    comment = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.author_id", ondelete='cascade'), nullable=False)

    author = db.relationship('Author', back_populates='reviews')

class Genre(db.Model):
    __tablename__ = 'genres'

    genre_id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(20), nullable=False)

class Address(db.Model):
    __tablename__ = "addresses"

    id = db.Column(db.Integer, primary_key=True)

    street_number = db.Column(db.Integer)
    street_name = db.Column(db.String(70))
    suburb = db.Column(db.String(50), nullable=False)
    postcode = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.customer_id", ondelete='cascade'), nullable=False)

    customer = db.relationship('Customer', back_populates='addresses')

# End of models


@app.route('/')
def home():
    return 'Home!'

@app.route('/init_db')
def init_db():
    db.create_all()
    return('Created Tables')

