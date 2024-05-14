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
    data = request.get_json()
    data_sensor_1 = data.get("sensor1")
    data_sensor_2 = data.get("sensor2")
    if request.method == "POST":
        new_info_um = Localizacao(sensor_um = data_sensor_1)
        new_info_dois = Localizacao(sensor_um = data_sensor_2)
        db.session.add(new_info_um, new_info_dois)
        db.session.commit()
        return jsonify({"sensor_um":data_sensor_1,"sensor_dois":data_sensor_2, "status":200})
    logging.info(f"Dados recebidos {data}")
    return "dados recebidos com sucesso"
