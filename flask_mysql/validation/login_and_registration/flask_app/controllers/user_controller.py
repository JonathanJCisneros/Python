from flask import render_template, request, redirect, flash, session
from flask_app import app
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route("/")
def display():
    return render_template("home.html")

@app.route("/login", methods = ['POST'])
def login():
    if User.validate_login(request.form) == False:
        return redirect("/")
    else:
        data = {
            "email" : request.form['email']
        }
        user_in_db = User.get_info(request.form)

        if not user_in_db:
            flash("Wrong cridentials! Please try again", "error_login")
            return redirect("/")
        if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
            flash("Wrong cridentials! Please try again", "error_login")
            return redirect("/")
        
        else:
            session['first_name'] = user_in_db.first_name
            session['last_name'] = user_in_db.last_name
            session['email'] = user_in_db.email
            session['id'] = user_in_db.id
            return redirect("/dashboard")


@app.route("/dashboard")
def current_user():
    if User.validate_session() == False:
        return redirect("/")
    else:
        data = {
            "id" : session['id']
        }

        return render_template("logged_in.html")


@app.route("/logout")
def user_logout():
    session.clear()
    flash("Log Out is successful!", "logout")
    return redirect("/")


@app.route("/register", methods = ['POST'])
def register_one():
    if User.validate_registration(request.form) == False:
        return redirect("/")
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data = {
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "email" : request.form['email'],
            "password" : pw_hash
        }
        user_id = User.register(data)
        session['first_name'] = request.form['first_name']
        session['last_name'] = request.form['last_name']
        session['email'] = request.form['email']
        session['user_id'] = user_id
        return redirect("/dashboard")