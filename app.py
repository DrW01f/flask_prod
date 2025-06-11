from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db, User

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


if __name__ == '__main__':
    app.run(debug=True)
