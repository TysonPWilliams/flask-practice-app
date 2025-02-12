from app import db

class Address(db.Model):
    __tablename__ = "addresses"

    id = db.Column(db.Integer, primary_key=True)

    street_number = db.Column(db.Integer)
    street_name = db.Column(db.String(70))
    suburb = db.Column(db.String(50), nullable=False)
    postcode = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.customer_id", ondelete='cascade'), nullable=False)

    customer = db.relationship('Customer', back_populates='addresses')