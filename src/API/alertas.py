from flask import Blueprint, jsonify, request,json
from config.bd import db, app, ma
from models.alertas import alertas, AlertasSchema

alertas_usuario = Blueprint("alertas_usuario",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

alerta_schema = AlertasSchema()   
alertas_schema = AlertasSchema(many=True)

@alerta_usuario.route("/alertas", methods=["GET"])
def alertas():
    resultall = alertas.query.all()
    result = alertas_schema.dump(resultall)
    return jsonify(result)

@alerta_usuario.route("/savealerta", methods=["POST"])
def savealerta():
    idusuario = request.json['idusuario']
    idciclovia = request.json['idciclovia']
    tipo_alerta = request.json['tipo_alerta']
    descripcion = request.json['descripcion']
    latitud_alerta = request.json['latitud_alerta']
    longitud_alerta = request.json['longitud_alerta']
    fecha_hora = request.json['fecha_hora']
    new_alerta = alertas(idusuario,idusuario,tipo_alerta,descripcion,latitud_alerta,longitud_alerta,fecha_hora)
    db.session.add(new_alerta)
    db.session.commit() 
    return "Datos guardados con exitos"

@alerta_usuario.route("/updatealerta", methods=["PUT"])
def updatealerta():
    id = request.json['id']
    idusuario = request.json['idusuario']
    idciclovia = request.json['idciclovia']
    tipo_alerta = request.json['tipo_alerta']
    descripcion = request.json['descripcion']
    latitud_alerta = request.json['latitud_alerta']
    longitud_alerta = request.json['longitud_alerta']
    fecha_hora = request.json['fecha_hora']
    nalertas = alertas.query.get(id) #Select * from usuario where id = id
    nalertas.idusuario = idusuario
    nalertas.idciclovia = idciclovia
    nalertas.tipo_alerta = tipo_alerta
    nalertas.descripcion = descripcion
    nalertas.latitud_alerta = latitud_alerta
    nalertas.longitud_alerta = longitud_alerta
    nalertas.fecha_hora = fecha_hora
    db.session.commit()
    return "Datos Actualizado con exitos"

@alerta_usuario.route("/deletealerta/<id>", methods=["GET"])
def deletealerta(id):
    aler = alertas.query.get(id)
    db.session.delete(aler)
    db.session.commit()
    return jsonify(alerta_schema.dump(aler))
