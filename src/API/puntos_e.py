from flask import Blueprint, jsonify, request,json
from config.bd import db, app, ma
from models.puntos_e import puntos_e, puntosESchema

ruta_puntosE = Blueprint("ruta_puntosE",__name__)

puntoE_schema = puntosESchema()   
puntosE_schema = puntosESchema(many=True)

@ruta_puntosE.route("/puntosE", methods=["GET"])
def puntosE():
    resultall = puntos_e.query.all()
    result = puntosE_schema.dump(resultall)
    return jsonify(result)

@ruta_puntosE.route("/savepuntosE", methods=["POST"])
def savepuntosE():
    descripcion = request.json['descripcion']
    nombre = request.json['nombre']
    longitud = request.json['longitud']
    latitud = request.json['latitud']
    comentarios = request.json['comentarios']
    new_points = puntos_e(descripcion,nombre,longitud,latitud,comentarios)
    db.session.add(new_points)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_puntosE.route("/updatepuntosE", methods=["PUT"])
def updatepuntosE():
    id = request.json['id']
    descripcion = request.json['descripcion']
    nombre = request.json['nombre']
    longitud = request.json['longitud']
    latitud = request.json['latitud']
    comentarios = request.json['comentarios']
    npuntosE = puntos_e.query.get(id) 
    npuntosE.descripcion = descripcion
    npuntosE.nombre = nombre
    npuntosE.longitud = longitud
    npuntosE.latitud = latitud
    npuntosE.comentarios = comentarios
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_puntosE.route("/deletepuntosE/<id>", methods=["GET"])
def deletepuntosE(id):
    puntosE = puntos_e.query.get(id)
    db.session.delete(puntosE)
    db.session.commit()
    return jsonify(puntoE_schema.dump(puntosE))