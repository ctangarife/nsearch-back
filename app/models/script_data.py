from datetime import datetime

from app import db_pgl as db

from app.models.script import Script


class ScriptData(db.Model):
    __table_args__ = {"schema": "nmodules"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_script = db.Column(db.Integer, db.ForeignKey("nmodules.script.id"))
    scipt_type = db.Column(db.String(255))
    argument = db.Column(db.Text)
    usage = db.Column(db.Text)
    output = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )
    # Relaciones
    author_data = db.relationship("Script", foreign_keys=[id_script])


    def __init__(
        self,
        id_script=None,
        scipt_type=None,
        argument=None,
        usage=None,
        output=None,
    ):
        self.id_script = id_script
        self.scipt_type = scipt_type
        self.argument = argument
        self.usage = usage
        self.output = output

    def __repr__(self):
        return "<Scripts {}>".format(self.id)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
