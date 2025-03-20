from flask_sqlalchemy import SQLAlchemy 
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# class Figlio(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(20), unique=True, nullable=False)
#     data_nascita = db.Column(db.Date, nullable=False)
#     madre_id = db.Column(db.Integer, db.ForeignKey('madre.id'), nullable=False)

# class Madre(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(20), unique=True, nullable=False)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_of_message = db.Column(db.String(20), unique=False, nullable=False)
    text =db.Column(db.String(160), unique=False, nullable=False)
    created_date =db.Column(db.DateTime,default=datetime.now)
    status =db.Column(db.String(20), unique=False, nullable=False)
