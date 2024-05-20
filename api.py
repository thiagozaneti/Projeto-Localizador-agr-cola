from flask import Blueprint, jsonify, request, render_template
from models.model import db, Localizacao
import logging
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
    
@bp.route("/api/infos/sensores", methods=["POST"])
def receber_sensores():
    if request.method == "POST":
        data = request.get_json()
        data_sensor_1 = data.get("temperature")
        data_sensor_2 = data.get("humidity")
        
        if data_sensor_1 is None or data_sensor_2 is None:
            return jsonify({"error": "Missing data"}), 400
        
        new_infos = Localizacao(sensor_um=data_sensor_1, sensor_dois = data_sensor_2)
        
        db.session.add(new_infos)
        db.session.commit()
        
        return jsonify({"sensor_um": data_sensor_1, "sensor_dois": data_sensor_2, "status": 200})

    return jsonify({"error": "Invalid method"}), 405

@bp.route("/api/infos/sensores/visualizar_logs", methods = ["GET"])
def visualizar_sensores():
    valores = Localizacao.query.all()
    return render_template("valores.html", valores = valores)