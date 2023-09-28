from config.bd import app, db, ma

class rutas(db.Model):
    __tablename__ = "rutas"

    id_ruta = db.Column(db.Integer, primary_key = True)
    puntos = db.Column(db.Integer, db.ForeignKey('puntos_e.id_puntosE'))
    usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    nombre_ruta = db.Column(db.String(50))
    descripcion_ruta = db.Column(db.String(50))
    longitud_latitud_inicial = db.Column(db.String(50))
    longitud_latitud_final = db.Column(db.String(50))
    fecha_creacion = db.Column(db.Date)
    duracion = db.Column(db.String(10))

    def __init__(self, puntos,usuario,nombre_ruta,descripcion_ruta,longitud_latitud_inicial,longitud_latitud_final):
        self.puntos = puntos
        self.nombre_ruta = nombre_ruta
        self.descripcion_ruta = descripcion_ruta
        self.longitud_latitud_inicial = longitud_latitud_inicial
        self.longitud_latitud_final = longitud_latitud_final

with app.app_context():
    db.create_all()

class RutasSchema(ma.Schema):
    class Meta:
        fields = ('idruta', 'puntos','usuario','nombre_ruta','descripcion_ruta','longitud_latitud_inicial','longitud_latitud_final')