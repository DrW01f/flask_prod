from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Parents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    kids = db.Column()

    def __repr__(self):
        return f'User({self.username}, {self.email})'


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)


class Teachers(db.Model):
    # учителя, фио, предмет, классное руководство
    id = db.Column(db.Integer, primary_key=True)


class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_sub = db.Column(db.String(30), unique=True, nullable=False)
