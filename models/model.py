from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Localizacao(db.Model):
    __tablename__ = "infos"
    id = db.Column(db.Integer, primary_key = True)
    sensor_um = db.Column(db.String(100), nullable=False)
    sensor_dois = db.Column(db.String(100), nullable=False)   