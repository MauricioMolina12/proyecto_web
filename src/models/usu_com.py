from config.bd import app, db, ma

class usu_com(db.Model):
    __tablename__ = "usu_com"

    id_usu_comu = db.Column(db.Integer, primary_key = True)
    comunidad = db.Column(db.Integer, db.ForeignKey('comunidad.id_comunidad'))
    usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    def __init__(self, comunidad,usuario):
        self.comunidad = comunidad
        self.usuario = usuario

with app.app_context():
    db.create_all()

class usu_comSchema(ma.Schema):
    class Meta:
        fields = ('id_usu_comu', 'comunidad','usuario')