from flask import Blueprint, jsonify, request,json
from config.bd import db, app, ma
from models.ciclovias import ciclovias, CicloviasSchema

ciclovia_usuario = Blueprint("ruta_ciclovias",__name__)

ciclovia_schema = CicloviasSchema()   
ciclovias_schema = CicloviasSchema(many=True)

@ciclovia_usuario.route("/ciclovias", methods=["GET"])
def ciclovia():
    resultall = ciclovias.query.all()
    result = ciclovias_schema.dump(resultall)
    return jsonify(result)

@ciclovia_usuario.route("/saveciclovias", methods=["POST"])
def saveciclovias():
    idpunto_e = request.json['idpunto_e']
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    longitud_latitud_inicial = request.json['longitud_latitud_inicial']
    longitud_latitud_final = request.json['longitud_latitud_final']
    new_ciclovia = ciclovias(idpunto_e,nombre,descripcion,longitud_latitud_inicial,longitud_latitud_final)
    db.session.add(new_ciclovia)
    db.session.commit() 
    return "Datos guardados con exitos"

@ciclovia_usuario.route("/updateciclovia", methods=["PUT"])
def updateciclovia():
    id = request.json['id']
    idpunto_e = request.json['idpunto_e']
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    longitud_latitud_inicial = request.json['longitud_latitud_inicial']
    longitud_latitud_final = request.json['longitud_latitud_final']
    nciclovias = ciclovias.query.get(id) 
    nciclovias.idpunto_e = idpunto_e
    nciclovias.nombre = nombre
    nciclovias.descripcion = descripcion
    nciclovias.longitud_latitud_inicial = longitud_latitud_inicial
    nciclovias.longitud_latitud_final = longitud_latitud_final
    db.session.commit()
    return "Datos Actualizado con exitos"

@ciclovia_usuario.route("/deleteciclovia/<id>", methods=["GET"])
def deleteciclovia(id):
    ciclo = ciclovias.query.get(id)
    db.session.delete(ciclo)
    db.session.commit()
    return jsonify(ciclovia_schema.dump(ciclo))