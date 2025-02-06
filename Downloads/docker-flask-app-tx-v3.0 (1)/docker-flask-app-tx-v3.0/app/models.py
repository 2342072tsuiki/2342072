import uuid
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Work(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created = db.Column(db.Text, nullable=False)
    hourly_wage = db.Column(db.Text, nullable=False)
    people = db.Column(db.Text, nullable=False)
    


