from config.bd import app, db, ma

class alertas(db.Model):
    __tablename__ = "alertas"

    id = db.Column(db.Integer, primary_key = True)
    idusuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    idciclovia = db.Column(db.Integer, db.ForeignKey('ciclovias.id'))
    tipo_alerta = db.Column(db.String(50))
    descripcion = db.Column(db.String(50))
    latitud_alerta = db.Column(db.String(50))
    longitud_alerta = db.Column(db.String(50))
    fecha_hora = db.Column(db.timestamp(50))

    def __init__(self, idusuario, idciclovia, tipo_alerta, descripcion, latitud_alerta, longitud_alerta, fecha_hora):
        self.idusuario =  idusuario
        self.idciclovia = idciclovia
        self.tipo_alerta = tipo_alerta
        self.descripcion = descripcion
        self.latitud_alerta =  latitud_alerta
        self.longitud_alerta = longitud_alerta
        self.fecha_hora = fecha_hora

with app.app_context():
    db.create_all()

class AlertasSchema(ma.Schema):
    class Meta:
        fields = ('id', 'idusuario', 'idciclovias','tipo_alerta','descripcion','latitud_alerta','longitud_alerta','fecha_hora')