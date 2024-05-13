from flask import Blueprint, jsonify, request, render_template
from models.model import db
bp = Blueprint("api", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/api/infos", methods = ["GET"])
def infos():
    if request.method == "POST":
        texto = request.form.get("texto")
        db.session.add(texto)
        db.session.commit()
        return jsonify({"message":"texto adicionado com sucesso", "status":200}) 
    else:
       return render_template("text.html")
