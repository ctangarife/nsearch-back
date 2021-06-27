from datetime import datetime

from app import db_pgl as db
from app.models.user import User


class Dummy(db.Model):
    __table_args__ = {'schema': 'example'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey(User.id))
    field_varchar = db.Column(db.String(255), nullable=False)
    field_text = db.Column(db.Text, nullable=False)
    field_date = db.Column(db.DateTime)
    field_bool = db.Column(db.Boolean, nullable=False)
    field_float = db.Column(db.Float, nullable=False)
    field_int = db.Column(db.Integer, nullable=False)
    field_enum = db.Column(
        db.Enum('P', 'A', 'F', name='example_status'), nullable=False, server_default='P'
    )
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )
    # Relaciones
    user_data = db.relationship('User', foreign_keys=[id_user])

    def __init__(
        self,
        id_user=None,
        field_varchar=None,
        field_text=None,
        field_date=None,
        field_bool=None,
        field_float=None,
        field_int=None,
        field_enum=None,


    ):
        self.id_user = id_user
        self.field_varchar = field_varchar
        self.field_text = field_text
        self.field_date = field_date
        self.field_bool = field_bool
        self.field_float = field_float
        self.field_int = field_int
        self.field_enum = field_enum

    def __repr__(self):
        return '<Example {}>'.format(self.id)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def calculate_advance(self):
        return round((self.step * 100) / 6)
