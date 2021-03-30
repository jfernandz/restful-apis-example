from .database_conn import db, ma
from marshmallow import fields


# Equipment class model
class Equipment(db.Model):
    __tablename__ = 'equipments'

    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    status = db.Column(db.Boolean)
    exec_path = db.Column(db.String(200))
    url = db.Column(db.String(200))

    def __init__(self, name, description, status, exec_path, url):
        self.name = name
        self.description = description
        self.status = status
        self.exec_path = exec_path
        self.url = url


class EquipmentSchema(ma.Schema):
    _id = fields.Int(dump_only=True)
    name = fields.Str()
    description = fields.Str()
    status = fields.Bool()
    exec_path = fields.Str()
    url = fields.Str()

    class Meta:
        fields = ('_id', 'name', 'description', 'status', 'exec_path', 'url')
