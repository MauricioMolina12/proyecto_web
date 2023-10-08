from flask import Flask, redirect, request, jsonify, json, session, render_template
from config.bd import app, db

from API.usuario import ruta_usuario
from API.comunidad import ruta_comunidad
from API.publicaciones import ruta_publicaciones
from API.usu_com import ruta_usu_com
from API.puntos_e import ruta_puntosE
from API.rutas import ruta_rutas
from API.ciclovias import ciclovias_usuario
from API.alertas import alertas_usuario
from API.rut_cic import rut_cic_usuario


app.register_blueprint(ruta_usuario, url_prefix="/api")
app.register_blueprint(ruta_comunidad, url_prefix="/api")
app.register_blueprint(ruta_publicaciones, url_prefix="/api")
app.register_blueprint(ruta_usu_com, url_prefix="/api")
app.register_blueprint(ruta_puntosE, url_prefix="/api")
app.register_blueprint(ruta_rutas, url_prefix="/api")
app.register_blueprint(ciclovias_usuario, url_prefix="/api")
app.register_blueprint(alertas_usuario, url_prefix="/api")
app.register_blueprint(rut_cic_usuario, url_prefix="/api")


app = Flask(__name__)
    
@app.route("/")
def index():
    return render_template('homepage.html')

@app.route("/login")
def login():
    return render_template('Login.html')

@app.route("/register")
def register():
    return render_template('Register.html')


@app.route("/map")
def maps():
    return render_template('maps.html')


if __name__ == "__main__":
    app.run(debug=True)

