from app import db_pgl as db
from datetime import datetime


class Master(db.Model):
    __table_args__ = {'schema': 'public'}
    __tablename__ = 'masters'
    id = db.Column(db.Integer, primary_key=True)
    master_name = db.Column(db.String(255), nullable=False)
    abbreviation = db.Column(db.String(255), nullable=False)
    master_group = db.Column(db.Integer)

    def __init__(self):
        pass
