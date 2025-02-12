from app import db

class Customer(db.Model):
    __tablename__ = "customers"

    customer_id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(12), nullable=False, unique=True)

    loans = db.relationship('Loan', back_populates='customer', cascade='all, delete')
    reviews = db.relationship('Review', back_populates='customer', cascade='all, delete')
    addresses = db.relationship('Address', back_populates='customer', cascade='all, delete')
