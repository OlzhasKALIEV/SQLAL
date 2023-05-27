from flask import Flask, render_template
from database import db, Employee
from datetime import datetime as DT
from datetime import timedelta
from datali import spisok_name, spisok_surname, city
import random

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)


def get_random_date():
    delta = DT.strptime('01.01.2023', '%d.%m.%Y') - DT.strptime('01.01.2017', '%d.%m.%Y')
    return DT.strptime('01.01.2016', '%d.%m.%Y') + timedelta(random.randint(0, delta.days))


count = 0


with app.app_context():
    db.drop_all()
    db.create_all()
    for i in range(5):
        index_1 = random.randint(1, len(spisok_name)-1)
        index_2 = random.randint(1, len(spisok_surname) - 1)
        db.session.add(
            Employee(
                name_user=spisok_name[index_1],
                surname_user=spisok_surname[index_2],
                index_user=city(),
                added=get_random_date()
            )
        )

    db.session.commit()


@app.route("/")
def all_center():
    return "<h1 align=center > Hello world </h1>"


@app.route("/employee")
def all_employees():
    employees = Employee.query.all()
    return render_template("all_employees.html", employees=employees)


if __name__ == "__main__":
    app.run()
