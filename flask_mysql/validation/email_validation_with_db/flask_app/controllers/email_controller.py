from flask import request, render_template, redirect, flash, session
from flask_app import app
from flask_app.models.email_model import Email

@app.route("/")
def display_form():
    return render_template("emailRegister.html")


@app.route("/new", methods = ['POST'])
def add_email():
    data = {
        "email" : request.form['email']
    }

    if Email.validate_email(data) == True:
        if Email.check_email(data) == None:
            Email.add_email(data)
            session['email'] = request.form['email']
            flash(f"The email {session['email']} is VALID! Thank you!", "email_valid")
            return redirect("/success")
        else:
            flash("Email already exists, please provide another", "error_email_in_use")
            return redirect("/")
    else:
        return redirect("/")
        
@app.route("/success")
def display_list():
    email_list = Email.get_all()
    return render_template("success.html", email_list = email_list)

@app.route("/delete/<int:id>")
def delete_one(id):
    data = {
        "id" : id
    }
    Email.delete_one(data)
    return redirect("/success")