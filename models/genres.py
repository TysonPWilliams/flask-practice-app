from app import db

class Genre(db.Model):
    __tablename__ = 'genres'

    genre_id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(20), nullable=False)
