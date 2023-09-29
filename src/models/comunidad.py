from config.bd import app, db, ma

class comunidad(db.Model):
    __tablename__ = "comunidad"

    id_comunidad = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))

    def __init__(self, nombre):
        self.nombre = nombre

with app.app_context():
    db.create_all()

class ComunidadSchema(ma.Schema):
    class Meta:
        fields = ('id_comunidad', 'nombre')