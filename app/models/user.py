from app import db_pgl as db
from datetime import datetime


class User(db.Model):
    __table_args__ = {'schema': 'turing_py'}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __init__(self):
        pass
