from datetime import datetime

from app import db_pgl as db

from app.models.author import Author
from app.models.category import Category


class Scripts(db.Model):
    __table_args__ = {"schema": "nmodules"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    id_author = db.Column(db.Integer, db.ForeignKey("nmodules.author.id"))
    id_category = db.Column(db.Integer, db.ForeignKey("nmodules.category.id"))
    favorite = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )
    # Relaciones
    author_data = db.relationship("Author", foreign_keys=[id_author])
    category_data = db.relationship("Category", foreign_keys=[id_category])

    def __init__(
        self,
        name=None,
        id_author=None,
        id_category=None,
        favourite=None,
    ):
        self.name = name
        self.id_author = id_author
        self.id_category = id_category
        self.favourite = favourite

    def __repr__(self):
        return "<Scripts {}>".format(self.id)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
