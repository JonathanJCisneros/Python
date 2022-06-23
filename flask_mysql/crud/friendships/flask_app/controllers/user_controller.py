from flask import request, render_template, redirect
from flask_app import app
from flask_app.models.user_model import User

@app.route("/friendships")
def display_all():
    user_list = User.get_all()
    return render_template("friendships.html", user_list = user_list)