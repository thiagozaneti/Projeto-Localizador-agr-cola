from flask_sqlalchemy import SQLAlchemy
class Config():
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/nome_do_banco' #trocar informações do banco
    SQLALCHEMY_TRACK_MODIFICATIONS = False
