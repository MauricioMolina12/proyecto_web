from config.bd import app, db, ma

class rut_cic(db.Model):
    __tablename__ = "rut_cic"

    id = db.Column(db.Integer, primary_key = True)
    idciclovias = db.Column(db.Integer, db.ForeignKey('ciclovias.id'))
    idrutas = db.Column(db.Integer, db.ForeignKey('rutas.id_ruta'))

    def __init__(self, idciclovias, idrutas):
        self.idciclovias= idciclovias
        self.idrutas = idrutas

with app.app_context():
    db.create_all()

class Rut_CicSchema(ma.Schema):
    class Meta:
        fields = ('id','idciclovias', 'idrutas')