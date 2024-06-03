from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Localizacao(db.Model):
    __tablename__ = "infos"
    id = db.Column(db.Integer, primary_key = True)
    longitude = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.String(100), nullable=False)
    altitude = db.Column(db.String(100), nullable=False)
    speed = db.Column(db.String(100), nullable=False)