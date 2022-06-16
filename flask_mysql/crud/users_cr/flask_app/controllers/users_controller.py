from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.users_model import User

@app.route("/")
def home():
    users_list = User.read_all()
    return render_template("read.html", users_list = users_list)

@app.route("/form")
def open_form():
    return render_template("create.html")

@app.route("/new", methods = ['POST'])
def new_user():
    User.sign_up(request.form)
    return redirect("/")