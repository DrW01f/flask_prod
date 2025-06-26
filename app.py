from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db, Parents, Students, Teachers

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return render_template("base.html")


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("OK")


@app.cli.command("auto-fill")
def auto_filling_data_in_db():
    # расширить функционал для заполнения всех таблиц 5 записями
    user = Students(age=9, class_number=3, student_name="Иванов Андрей Алексеевич")
    db.session.add(user)
    db.session.commit()
    print("Auto filling OK")


@app.cli.command("edit-student")
def edit_student():
    # name = input()
    student = Students.query.filter_by(student_name="Иванов Андрей Алексеевич").first()
    student.age += 1
    student.class_number = 1
    db.session.commit()
    print("Edit complete")


@app.cli.command("del-student")
def del_student():
    student = Students.query.filter_by(student_name="Иванов Андрей Алексеевич").first()
    # лучше не удалять, а сделать статус "невидимый" или "удаленный"
    db.session.delete(student)
    db.session.commit()
    print("Delete complete")




if __name__ == '__main__':
    app.run(debug=True)


# 42:00



















