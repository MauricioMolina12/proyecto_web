from config.bd import app, db, ma

class puntos_e(db.Model):
    __tablename__ = "puntos_e"

    id_puntosE = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.Text)
    nombre = db.Column(db.String(50))
    longitud = db.Column(db.String(20))
    latitud = db.Column(db.String(20))
    comentarios = db.Column(db.Text)

    def __init__(self, descripcion,nombre,longitud,latitud,comentarios):
        self.descripcion = descripcion
        self.nombre = nombre
        self.longitud = longitud
        self.latitud = latitud
        self.comentarios = comentarios

with app.app_context():
    db.create_all()

class puntosESchema(ma.Schema):
    class Meta:
        fields = ('id_puntosE','descripcion','nombre','longitud','latitud','comentarios')