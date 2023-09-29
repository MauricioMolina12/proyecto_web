from config.bd import app, db, ma

class ciclovias(db.Model):
    __tablename__ = "ciclovias"

    id = db.Column(db.Integer, primary_key = True)
    idpunto_e = db.Column(db.Integer, db.ForeignKey('punto_e.id'))
    nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(50))
    longitud_latitud_inicial = db.Column(db.String(50))
    longitud_latitud_final = db.Column(db.String(50))

    def __init__(self, idpunto_e, nombre, descripcion, longitud_latitud_inicial, longitud_lotitud_final):
        self.idpunto_e = idpunto_e
        self.nombre = nombre
        self.descripcion = descripcion
        self.longitud_latitud_inicial =  longitud_latitud_inicial
        self.longitud_latitud_final = longitud_latitud_final

with app.app_context():
    db.create_all()

class CicloviasSchema(ma.Schema):
    class Meta:
        fields = ('id', 'idpunto_e', 'nombre','descripcion','longitud_latitud_inicial','longitud_latitud_final')