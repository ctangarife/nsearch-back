from app.models.example import Example
from app import db_pgl as db
from datetime import datetime


class exampleController:
    def insert_example(self, status, start_date, end_date):
        example = example(status, start_date, end_date)
        db.session.add(example)
        db.session.commit()
        return example.uuid

    def update_example(self, uuid, status):
        example = example.query.filter_by(uuid=uuid).first()
        example.status = status
        example.date_ended = datetime.today()
        db.session.commit()
        return example.uuid

    def get_example_by_id(self, uuid):
        return example.query.filter_by(uuid=uuid).first()

    def get_last_example(self):
        return example.query.filter_by(status='P').order_by(example.id.desc()).first()
