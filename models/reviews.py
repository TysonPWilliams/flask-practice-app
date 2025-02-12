from app import db

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
