from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Localizacao(db.Model):
    __tablename__ = "infos"
    id = db.Column(db.Integer, primary_key = True)
    texto = db.Column(db.String(100), nullable=False)   