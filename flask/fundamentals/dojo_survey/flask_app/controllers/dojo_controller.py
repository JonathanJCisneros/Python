from flask import session, request, render_template, redirect, flash
from flask_app import app
from flask_app.models.dojo_model import Dojo

@app.route("/")
def lets_start():
    return render_template("form.html")

@app.route("/process", methods = ['POST'])
def new_survey():
    if Dojo.validate_survey(request.form) == True:

        data = {
            "name" : request.form['name'],
            "location" : request.form['location'],
            "language" : request.form['language'],
            "comments" : request.form['comments']
        }
        survey_id = Dojo.add_one(data)

        session["name"] = request.form["name"]
        session["location"] = request.form["location"]
        session["language"] = request.form["language"]
        session["comments"] = request.form["comments"]
        session['survey_id'] = survey_id
        return redirect("/result")
    else:
        return redirect("/")

@app.route("/result")
def result():
    if Dojo.validate_session() == True:
        return render_template("results.html")
    else:
        flash("You must register to see this page", "error_result")
        return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")