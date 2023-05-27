from flask import Flask, render_template
from database import db, Employee
from datetime import datetime as DT
from datetime import timedelta
from datali import city, name, surname
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
    for name, surname, index in zip(name(), surname(), city()):  # количество строк
        db.session.add(
            Employee(
                name_user=name,
                surname_user=surname,
                index_user=index,
                added=get_random_date()
            )
        )

    db.session.commit()


@app.route("/")
def all_center():
    return render_template("layout.html")


@app.route("/employee")
def all_employees():
    employees = Employee.query.all()
    return render_template("all_employees.html", employees=employees)


if __name__ == "__main__":
    app.run()
