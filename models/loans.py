from app import db

class Loan(db.Model):
    __tablename__ = "loans"

    id = db.Column(db.Integer, primary_key=True)

    customer_id = db.Column(db.Integer, db.ForeignKey("customers.customer_id", ondelete='cascade'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("books.book_id", ondelete='cascade'), nullable = False)
    borrow_date = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable=False)

    customer = db.relationship('Customer', back_populates='loans')
    book = db.relationship('Book', back_populates='loans')
