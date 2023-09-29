from flask import Blueprint, jsonify, request,json
from config.bd import db, app, ma
from models.publicaciones import publicaciones, PublicacionesSchema

ruta_publicaciones = Blueprint("ruta_publicaciones",__name__)

publicacion_schema = PublicacionesSchema()   
publicaciones_schema = PublicacionesSchema(many=True)

@ruta_publicaciones.route("/publicacion", methods=["GET"])
def publicacion():
    resultall = publicaciones.query.all()
    result = publicaciones_schema.dump(resultall)
    return jsonify(result)

@ruta_publicaciones.route("/savepublicacion", methods=["POST"])
def savepublicacion():
    comunidad = request.json['comunidad']
    usuario = request.json['usuario']
    mensaje = request.json['mensaje']
    new_publication = publicaciones(comunidad,usuario,mensaje)
    db.session.add(new_publication)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_publicaciones.route("/updatepublicacion", methods=["PUT"])
def updatepublicacion():
    id = request.json['id']
    comunidad = request.json['comunidad']
    usuario = request.json['usuario']
    mensaje = request.json['mensaje']
    npublication = publicaciones.query.get(id) 
    npublication.comunidad = comunidad
    npublication.usuario = usuario
    npublication.mensaje = mensaje
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_publicaciones.route("/deletepublicacion/<id>", methods=["GET"])
def deletepublication(id):
    publication = publicaciones.query.get(id)
    db.session.delete(publication)
    db.session.commit()
    return jsonify(publicacion_schema.dump(publication))