from flask import Blueprint, jsonify, request, render_template
from models.model import db, Localizacao
bp = Blueprint("api", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/api/infos", methods = ["GET"])
def infos():
    if request.method == "GET":
        texto = request.args.get("texto")
        new_info = Localizacao(texto = texto)
        db.session.add(new_info)
        db.session.commit()
        variavel = ({"message":"texto adicionado com sucesso", "status":200}) 
        return render_template("text.html")
    else:
       return render_template("text.html")
