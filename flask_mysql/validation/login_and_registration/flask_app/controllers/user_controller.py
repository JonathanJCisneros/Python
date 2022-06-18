from flask import render_template
from flask_app import app
from flask_app.models.user_model import User


@app.route("/")
def display():
    return render_template("home.html")