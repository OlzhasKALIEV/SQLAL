from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

db = SQLAlchemy()


class Employee(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    name_user = db.Column(db.String)
    surname_user = db.Column(db.String)
    added = db.Column(db.DateTime, nullable=False, default=func.now())

    def __repr__(self):
        return f'User(fullname={self.name_books})'
