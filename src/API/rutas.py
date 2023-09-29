from flask import Blueprint, jsonify, request,json
from config.bd import db, app, ma
from models.rutas import rutas, RutasSchema

ruta_rutas = Blueprint("ruta_rutas",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

ruta_schema = RutasSchema()   
rutas_schema = RutasSchema(many=True)

@ruta_rutas.route("/rutas", methods=["GET"])
def ruta():
    resultall = rutas.query.all()
    result = rutas_schema.dump(resultall)
    return jsonify(result)

@ruta_rutas.route("/saverutas", methods=["POST"])
def saverutas():
    puntos = request.json['puntos']
    usuario = request.json['usuario']
    nombre_ruta = request.json['nombre_ruta']
    descripcion_ruta = request.json['descripcion_ruta']
    longitud_latitud_inicial = request.json['longitud_latitud_inicial']
    longitud_latitud_final = request.json['longitud_latitud_final']
    fecha_creacion = request.json['fecha_creacion']
    duracion = request.json['duracion']
    new_rout = rutas(puntos,usuario,nombre_ruta,descripcion_ruta,longitud_latitud_inicial,longitud_latitud_final,fecha_creacion,duracion)
    db.session.add(new_rout)
    db.session.commit() 
    return "Datos guardados con exitos"

@ruta_rutas.route("/updaterutas", methods=["PUT"])
def updaterutas():
    id = request.json['id']
    puntos = request.json['puntos']
    usuario = request.json['usuario']
    nombre_ruta = request.json['nombre_ruta']
    descripcion_ruta = request.json['descripcion_ruta']
    longitud_latitud_inicial = request.json['longitud_latitud_inicial']
    longitud_latitud_final = request.json['longitud_latitud_final']
    fecha_creacion = request.json['fecha_creacion']
    duracion = request.json['duracion']
    nrutas = rutas.query.get(id)
    nrutas.puntos = puntos
    nrutas.usuario = usuario
    nrutas.nombre_ruta = nombre_ruta
    nrutas.descripcion_ruta = descripcion_ruta
    nrutas.longitud_latitud_inicial = longitud_latitud_inicial
    nrutas.longitud_latitud_final = longitud_latitud_final
    nrutas.fecha_creacion = fecha_creacion
    nrutas.duracion = duracion
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_rutas.route("/deleterutas/<id>", methods=["GET"])
def deleterutas(id):
    rout = rutas.query.get(id)
    db.session.delete(rout)
    db.session.commit()
    return jsonify(ruta_schema.dump(rout))