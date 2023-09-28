from config.bd import app, db, ma

class publicaciones(db.Model):
    __tablename__ = "publicaciones"

    id_publicaciones = db.Column(db.Integer, primary_key = True)
    comunidad = db.Column(db.Integer, db.ForeignKey('comunidad.id_comunidad'))
    usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    mensaje = db.Column(db.Text)

    def __init__(self, comunidad,usuario,mensaje):
        self.comunidad = comunidad
        self.usuario = usuario
        self.mensaje = mensaje

with app.app_context():
    db.create_all()

class PublicacionesSchema(ma.Schema):
    class Meta:
        fields = ('id_publicaciones', 'comunidad','usuario','mensaje')