from flask import Flask, redirect, request, jsonify, json, session, render_template
from config.bd import app, db

# from api.Clientes import ruta_cliente
# from api.Ruta import  ruta_ruta
# from api.Alertas import ruta_alertas

# app.register_blueprint(ruta_cliente, url_prefix="/api")
# app.register_blueprint(ruta_ruta, url_prefix="/api")
# app.register_blueprint(ruta_alertas, url_prefix="/api")

@app.route("/")
def index():
    return render_template('layout.html')

if __name__ == "__main__":
    app.run(debug=True)

    #hola