from flask import Blueprint, jsonify, request,json
from config.bd import db, app, ma
from models.usuario import usuario, UsuarioSchema

ruta_usuario = Blueprint("ruta_usuario",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

usuario_schema = UsuarioSchema()   
usuarios_schema = UsuarioSchema(many=True)

@ruta_usuario.route("/usuarios", methods=["GET"])
def usuarios():
    resultall = usuario.query.all()
    result = usuario_schema.dump(resultall)
    return jsonify(result)

@ruta_usuario.route("/saveusuario", methods=["POST"])
def saveusuario():
    nombre = request.json['nombre']
    correo = request.json['correo']
    contraseña = request.json['contraseña']
    new_user = usuario(nombre,correo,contraseña)
    db.session.add(new_user)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_usuario.route("/updateusuario", methods=["PUT"])
def updateusuario():
    id = request.json['id']
    nombre = request.json['nombre']
    correo = request.json['correo']
    contraseña = request.json['contraseña']
    nusuario = usuario.query.get(id) #Select * from usuario where id = id
    nusuario.nombre = nombre
    nusuario.correo = correo
    nusuario.contraseña = contraseña
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_usuario.route("/deleteusuario/<id>", methods=["GET"])
def deleteusuario(id):
    user = usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify(usuario_schema.dump(usuario))

