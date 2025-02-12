from app import db

class Book(db.Model):
    __tablename__ = "books"

    book_id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(60), nullable=False)
    stock_available = db.Column(db.Integer, db.CheckConstraint('stock_available >= 0'), default=1)

    loans = db.relationship('Loan', back_populates='book', cascade='all, delete')
    reviews = db.relationship('Review', back_populates='book', cascade='all, delete')