from flask import Flask, redirect, request, jsonify, json, session, render_template
from config.bd import app, db

@app.route("/")
def index():
    
    return "Hola mundo"

if __name__ == "__main__":
    app.run(debug=True)