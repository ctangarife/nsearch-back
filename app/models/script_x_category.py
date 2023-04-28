from datetime import datetime

from app import db_pgl as db

from app.models.script import Script
from app.models.category import Category


class ScriptXCategory(db.Model):
    __table_args__ = {"schema": "nmodules"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_script = db.Column(db.Integer, db.ForeignKey("nmodules.script.id"))
    id_category = db.Column(db.Integer, db.ForeignKey("nmodules.category.id"))
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    # Relaciones
    script_data = db.relationship("Script", foreign_keys=[id_script])
    category_data = db.relationship("Category", foreign_keys=[id_category])

    def __init__(
        self,
        id_script=None,
        id_category=None,
    ):
        self.id_script = id_script
        self.id_category = id_category

    def __repr__(self):
        return "<Scripts {}>".format(self.id)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
