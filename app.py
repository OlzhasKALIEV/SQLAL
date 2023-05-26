import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
db.init_app(app)

if __name__ == "__main__":
    app.run()
