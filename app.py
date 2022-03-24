from flask import Flask, render_template, url_for, flash, redirect
from forms import StudentLoginForm
from sqlalchemy.sql import delete, insert, update, select
from database import user, meta, engine

app = Flask("__name__")
app.config["SECRET_KEY"] = "dlksdldlk44829sl4lellddskdls"

@app.route("/", methods=["post", "get"])
def index():
    form = StudentLoginForm()
    if form.validate_on_submit():
       meta.create_all(engine)
       ins = user.insert().values(username=form.username.data, password=form.password.data)
       engine.connect().execute(ins)
    #    user.drop(engine)
       flash(f'Logged in successfully as {form.username.data}!', 'success')
    return render_template("student_login.html", form=form)


@app.route("/display")
def retrive():
    students = engine.connect().execute(user.select()).fetchall()
    return render_template('display.html', students = students)














if "__name__" == "__main__":
    app.run(debug=True)

