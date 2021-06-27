import sys

sys.path.append('../')
from app.models.example import Dummy

from app import db_pgl as db

if __name__ == '__main__':
    db.create_all()
    db.session.commit()
