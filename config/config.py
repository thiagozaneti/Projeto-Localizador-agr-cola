from flask_sqlalchemy import SQLAlchemy
class Config():
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:5e5i#123@localhost/projeto' #trocar informações do banco
    SQLALCHEMY_TRACK_MODIFICATIONS = False
