from flask import Blueprint, jsonify, request,json,session,redirect,render_template
from config.bd import db, app, ma
from models.usuario import usuario
from models.publicaciones import publicaciones, PublicacionesSchema

ruta_publicaciones = Blueprint("ruta_publicaciones",__name__)

publicacion_schema = PublicacionesSchema()   
publicaciones_schema = PublicacionesSchema(many=True)

@app.route("/publicar", methods=["POST"])
def savepublicacion():
    if 'user' in session:
        nombre_usuario = session['user']['nombre']
        id_usuario = session['user']['id']
        usuario = id_usuario
        mensaje = request.form['message']
        new_publication = publicaciones(usuario,mensaje)
        db.session.add(new_publication)
        db.session.commit()
        return redirect ('/comunidad')
    else:
        return redirect ('/login')


@app.route("/comunidad", methods=["GET"])
def publicacion():
    datos = db.session.query(publicaciones, usuario.nombre).join(usuario, publicaciones.usuario == usuario.id).all()
    return render_template('comunidad.html', datos=datos)


@ruta_publicaciones.route("/publicacion", methods=["GET"])
def publicacion():
    resultall = publicaciones.query.all()
    result = publicaciones_schema.dump(resultall)
    return jsonify(result)

@ruta_publicaciones.route("/savepublicacion", methods=["POST"])
def savepublicacion():
    usuario = request.json['usuario']
    mensaje = request.json['mensaje']
    new_publication = publicaciones(usuario,mensaje)
    db.session.add(new_publication)
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_publicaciones.route("/updatepublicacion", methods=["PUT"])
def updatepublicacion():
    id = request.json['id']
    usuario = request.json['usuario']
    mensaje = request.json['mensaje']
    npublication = publicaciones.query.get(id) 
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