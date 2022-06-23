from flask import redirect, render_template, request
from flask_app import app
from flask_app.models.user_model import User


@app.route("/")
@app.route("/friendships")
def display_all():
    user_list = User.get_all_friendships()
    return render_template("friendships.html", user_list = user_list)
