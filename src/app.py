from flask import Flask, redirect, request, jsonify, json, session, render_template
from config.bd import app, db

from API.usuario import ruta_usuario
from API.comunidad import ruta_comunidad
from API.publicaciones import ruta_publicaciones
from API.usu_com import ruta_usu_com
from API.puntos_e import ruta_puntosE
from API.rutas import ruta_rutas


app.register_blueprint(ruta_usuario, url_prefix="/api")
app.register_blueprint(ruta_comunidad, url_prefix="/api")
app.register_blueprint(ruta_publicaciones, url_prefix="/api")
app.register_blueprint(ruta_usu_com, url_prefix="/api")
app.register_blueprint(ruta_puntosE, url_prefix="/api")
app.register_blueprint(ruta_rutas, url_prefix="/api")


@app.route("/")
def index():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True)

