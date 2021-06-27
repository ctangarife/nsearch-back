from app import db_pgl as db
from app.models.example import Example
from datetime import datetime


class GetExampleMaster(db.Model):
    __table__ = db.Table(
        'get_example_masters',
        db.metadata,
        db.Column('id', db.Integer, nullable=False, primary_key=True),
        db.Column('id_brief', db.Integer, nullable=False),
        db.Column('id_master', db.Integer, nullable=False),
        db.Column('master_name', db.String(255), nullable=False),
        db.Column('value', db.String(255), nullable=False),
        db.Column('value_field', db.String(255), nullable=False),
        db.Column('alias', db.String(255), nullable=False),
        db.Column('step', db.Integer, nullable=False),
        schema='example',
    )


# """ SELECT mb.id,
#     mb.id_brief,
#     mb.id_master,
#     ( SELECT ma.master_name
#            FROM masters ma
#           WHERE (ma.id = mb.id_master)) AS master_name,
#     mb.value,
#     mb.value_field,
#     ( SELECT mg.alias
#            FROM (masters ma
#              JOIN master_groups mg ON ((mg.id = ma.master_group)))
#           WHERE (ma.id = mb.id_master)) AS alias,
#     mb.step
#    FROM brief.master_x_brief mb
#   ORDER BY mb.step; """