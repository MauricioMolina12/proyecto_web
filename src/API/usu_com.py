from flask import Blueprint, jsonify, request,json
from config.bd import db, app, ma
from models.usu_com import usu_com, usu_comSchema

ruta_usu_com = Blueprint("ruta_usu_com",__name__)

usu_com_schema = usu_comSchema()   
usu_comu_schema = usu_comSchema(many=True)

@ruta_usu_com.route("/usu_com", methods=["GET"])
def usu_com():
    resultall = usu_com.query.all()
    result = usu_comu_schema.dump(resultall)
    return jsonify(result)

@ruta_usu_com.route("/saveusu_com", methods=["POST"])
def saveusu_com():
    comunidad = request.json['comunidad']
    usuario = request.json['usuario']
    new_usu_com = usu_com(comunidad,usuario)
    db.session.add(new_usu_com)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_usu_com.route("/updateusu_com", methods=["PUT"])
def updateusu_com():
    comunidad = request.json['comunidad']
    usuario = request.json['usuario']
    nusu_com = usu_com.query.get(id) 
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_usu_com.route("/deleteusu_com/<id>", methods=["GET"])
def deleteusu_com(id):
    usu_com = usu_com.query.get(id)
    db.session.delete(usu_com)
    db.session.commit()
    return jsonify(usu_comu_schema.dump(usu_com))