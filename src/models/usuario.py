from config.bd import app, db, ma

class usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    contraseña = db.Column(db.String(50))

    def __init__(self, nombre, correo, contraseña):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña

with app.app_context():
    db.create_all()

class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'correo','contraseña')