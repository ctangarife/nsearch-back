import sys

sys.path.append("../")
from app.models.author import Author
from app.models.category import Category
from app.models.script import Script
from app.models.script_data import ScriptData
from app.models.script_x_category import ScriptXCategory

from app import db_pgl as db


def create_schemas():
    db.session.execute("CREATE SCHEMA IF NOT EXISTS nmodules")
    db.session.commit()


if __name__ == "__main__":
    create_schemas()
    db.create_all()
    db.session.commit()
