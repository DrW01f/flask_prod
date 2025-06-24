from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Students(db.Model):
    # главная таблица
    student_id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    class_number = db.Column(db.Integer, nullable=False)
    parents = db.relationship("Parents", backref="kid", lazy=True)

    def __repr__(self):
        return f'User({self.username}, {self.age}, {self.class_number})'


class Parents(db.Model):
    parent_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    kids = db.Column(db.Integer, db.ForeignKey("students.student_id"))

    def __repr__(self):
        return f'User({self.username}, {self.kids})'


class Teachers(db.Model):
    # учителя, фио, предмет, классное руководство
    teacher_id = db.Column(db.Integer, primary_key=True)
    teacher_name = db.Column(db.String(30), nullable=False)


class Subjects(db.Model):
    subject_id = db.Column(db.Integer, primary_key=True)
    name_of_sub = db.Column(db.String(30), unique=True, nullable=False)
