from flask import session, render_template, request, redirect
from flask_app import app
from flask_app.models.user_model import User

@app.route("/")
@app.route("/login")
def display_login():
    return render_template("loginRegistration.html")

@app.route("/login", methods = ['POST'])
def user_login():
    result = User.get_one(request.form)
    print(result)

    if result == None:
        return redirect("/login")
    else:
        session['first_name'] = result.first_name
        session['last_name'] = result.last_name
        return redirect("/todos")