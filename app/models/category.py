from datetime import datetime

from app import db_pgl as db


class Category(db.Model):
    __table_args__ = {"schema": "nmodules"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )
    # Relaciones
    
    def __init__(
        self,
        name=None,
        url=None,
    ):
        self.name = name
        self.url = url

    def __repr__(self):
        return "<Scripts {}>".format(self.id)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}