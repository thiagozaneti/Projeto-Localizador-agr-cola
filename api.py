from flask import Blueprint, jsonify, request, render_template
from models.model import db, Localizacao
import logging
bp = Blueprint("api", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/api/infos", methods=["GET"])
def infos():
    texto = request.args.get("texto")
    if texto:
        new_info = Localizacao(texto=texto)
        db.session.add(new_info)
        db.session.commit()
        return jsonify({"message": "texto adicionado com sucesso", "status": 200})
    else:
        return jsonify({"error": "Missing texto parameter"}), 400

@bp.route("/api/infos/sensores", methods=["POST", "GET"])
def receber_sensores():
    if request.method == "POST":
        data = request.get_json()
        if not data:
            return jsonify({"error": "Sem data enviada"}), 400
        
        data_sensor_1 = data.get("temperature")
        data_sensor_2 = data.get("humidity")
        
        if data_sensor_1 is None or data_sensor_2 is None:
            return jsonify({"error": "Sem data"}), 400
        
        new_infos = Localizacao(sensor_um=data_sensor_1, sensor_dois=data_sensor_2)
        db.session.add(new_infos)
        db.session.commit()
        
        return jsonify({"sensor_um": data_sensor_1, "sensor_dois": data_sensor_2, "status": 200})
    if request.method == "GET":
        valores = Localizacao.query.all()
        return jsonify([{"id": valor.id, "sensor_um": valor.sensor_um, "sensor_dois": valor.sensor_dois} for valor in valores])
    return jsonify({"error"})

@bp.route("/api/infos/sensores/visualizar_logs", methods=["GET"])
def visualizar_sensores():
    valores = Localizacao.query.all()
    return render_template("valores.html", valores=valores)
