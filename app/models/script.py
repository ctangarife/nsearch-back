from datetime import datetime

from app import db_pgl as db

from app.models.author import Author


class Script(db.Model):
    __table_args__ = {"schema": "nmodules"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    url_download = db.Column(db.String(255), nullable=False)
    id_author = db.Column(db.Integer, db.ForeignKey("nmodules.author.id"))
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )
    # Relaciones
    author_data = db.relationship("Author", foreign_keys=[id_author])

    def __init__(
        self,
        name=None,
        id_author=None,
        url=None,
        url_download=None,
    ):
        self.name = name
        self.id_author = id_author
        self.url = url
        self.url_download = url_download

    def __repr__(self):
        return "<Scripts {}>".format(self.id)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
