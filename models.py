from datetime import datetime
from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    color = db.Column(db.String(10), nullable=False)
    text =  db.Column(db.Text)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'{self.title}'

db.create_all()
