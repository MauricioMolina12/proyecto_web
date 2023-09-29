from flask import Blueprint, jsonify, request,json
from config.bd import db, app, ma
from models.rut_cic import rut_cic, Rut_CicSchema

rut_cic_usuario = Blueprint("rut_cic_usuario",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

rut_cic_schema = Rut_CicSchema()   
rut_cics_schema = Rut_CicSchema(many=True)

@rut_cic_usuario.route("/rut_cic", methods=["GET"])
def rur_cic():
    resultall = rut_cic.query.all()
    result = rut_cics_schema.dump(resultall)
    return jsonify(result)

@rut_cic_usuario.route("/saverut_cic", methods=["POST"])
def saverut_cic():
    idciclovias = request.json['idciclovias']
    idrutas = request.json['idrutas']
    new_rut_cic = rut_cic(idciclovias,idrutas)
    db.session.add(new_rut_cic)
    db.session.commit() 
    return "Datos guardados con exitos"

@rut_cic_usuario.route("/updaterut_cic", methods=["PUT"])
def updaterut_cic():
    id = request.json['id']
    idciclovias = request.json['idciclovias']
    idrutas = request.json['idrutas']
    nrut_cic = rut_cic.query.get(id) #Select * from usuario where id = id
    nrut_cic.idciclovias = idciclovias
    nrut_cic.idrutas = idrutas
    db.session.commit()
    return "Datos Actualizado con exitos"

@rut_cic_usuario.route("/deleterut_cic/<id>", methods=["GET"])
def deleterut_cic(id):
    rut_c = rut_cic.query.get(id)
    db.session.delete(rit_c)
    db.session.commit()
    return jsonify(rut_cic_schema.dump(rut_c))