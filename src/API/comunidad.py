from flask import Blueprint, jsonify, request,json
from config.bd import db, app, ma
from models.comunidad import comunidad, ComunidadSchema

ruta_comunidad = Blueprint("ruta_comunidad",__name__)

comunidad_schema = ComunidadSchema()   
comunidades_schema = ComunidadSchema(many=True)

@ruta_comunidad.route("/comunidad", methods=["GET"])
def comunidad():
    resultall = comunidad.query.all()
    result = comunidad_schema.dump(resultall)
    return jsonify(result)

@ruta_comunidad.route("/savecomunidad", methods=["POST"])
def savecomunidad():
    nombre = request.json['nombre']
    new_communities = comunidad(nombre)
    db.session.add(new_communities)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_comunidad.route("/updatecomunidad", methods=["PUT"])
def updatecomunidad():
    id = request.json['id_comunidad']
    nombre = request.json['nombre']
    ncomunidad = comunidad.query.get(id) 
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_comunidad.route("/deletecomunidad/<id>", methods=["GET"])
def deletecomunidad(id):
    communities = comunidad.query.get(id)
    db.session.delete(communities)
    db.session.commit()
    return jsonify(comunidad_schema.dump(comunidad))

