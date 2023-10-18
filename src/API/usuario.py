from flask import Blueprint, jsonify, request,json,redirect,session,render_template
from config.bd import db, app, ma
from models.usuario import usuario, UsuarioSchema

ruta_usuario = Blueprint("ruta_usuario",__name__)

usuario_schema = UsuarioSchema()   
usuarios_schema = UsuarioSchema(many=True)


@app.route('/ingresar', methods=['POST'])
def ingresar():
    user = request.form['user']
    password = request.form['password']
    Usuario = usuario.query.filter_by(nombre=user, contraseña=password).first() 
    if Usuario:
        session['user'] = {'id': Usuario.id, 'nombre': Usuario.nombre}
        return render_template('homepage.html', Usuario = session['user']['nombre']), session    
    else:
        return "Usuario o contraseña incorrectos"   

@app.route('/cerrar')
def cerrar():
    session.pop('user',None)
    return redirect('/')


@app.route('/add_user', methods = ['POST'])
def add_user():
    if request.method == 'POST':
        nombre = request.form['user']
        correo = request.form['email']
        contraseña = request.form['password']
        ccontraseña = request.form['Cpassword']
        Usuario = usuario.query.filter_by(nombre=nombre).first()
        if Usuario is None and contraseña==ccontraseña: 
            new_user = usuario(nombre, correo,contraseña)
            db.session.add(new_user)
            db.session.commit()  
            
    user_exists = True 
    
    if user_exists:
        response = {
            "success": False,
            "message": "Este usuario ya existe"
        }
    else:
        response = {
            "success": True,
            "message": "Usuario registrado exitosamente"
        }
        return redirect('/login')
    
    return jsonify(response)


@ruta_usuario.route("/usuarios", methods=["GET"])
def usuarios():
    resultall = usuario.query.all()
    result = usuarios_schema.dump(resultall)
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
    db.session.delete(user)
    db.session.commit()
    return jsonify(usuario_schema.dump(user))

