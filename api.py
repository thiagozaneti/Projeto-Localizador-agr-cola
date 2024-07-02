from flask import Blueprint, jsonify, request, render_template
from models.model import db, Localizacao
import logging
bp = Blueprint("api", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/desenhar")
def desenhar_mapa():
    return render_template("map.html")

@bp.route("/api/infos/sensores", methods=["POST", "GET"])
def receber_sensores():
    if request.method == "POST":
        data = request.get_json()
        if not data:
            return jsonify({"error": "Sem data enviada"}), 400
        
        latitude = data.get("latitude")
        longitude = data.get("longitude")
        altitude = data.get("altitude")
        speed = data.get("speed")
        
        if latitude is None or longitude is None or altitude is None or speed is None:
            return jsonify({"error": "Sem data"}), 400
        
        new_infos = Localizacao(latitude=latitude, longitude = longitude, altitude = altitude, speed = speed)
        db.session.add(new_infos)
        db.session.commit()
        
        return jsonify({"lat": latitude , "long": longitude, "altitude":altitude, "speed": speed , "status": 200})
    if request.method == "GET":
        valores = Localizacao.query.all()
        return jsonify([{"lat": latitude , "long": longitude, "altitude":altitude, "speed": speed , "status": 200} for valor in valores])
    return jsonify({"error"})

@bp.route("/api/coordenadas", methods = ["GET"])
def get_coordernadas():
    coordenadas = Localizacao.query.order_by(Localizacao.id.desc()).limit(10).all()
    lista_coordenadas = [{"longitude":coord.longitude, "latitude": coord.latitude}for coord in coordenadas]
    return lista_coordenadas

@bp.route("/api/infos/sensores/visualizar_logs", methods=["GET"])
def visualizar_sensores():
    valores = Localizacao.query.all()
    return render_template("valores.html", valores=valores)
