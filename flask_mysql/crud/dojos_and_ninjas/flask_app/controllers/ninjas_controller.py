from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.ninjas_model import Ninja
from flask_app.models.dojos_model import Dojo

@app.route("/ninjas")
def register_form():
    new_dojo = Dojo.get_all()
    return render_template("new_ninja.html", new_dojo = new_dojo)

@app.route("/new_ninja", methods = ['POST'])
def register_ninja():
    Ninja.create_ninja(request.form)
    num = request.form['dojo_id']
    return redirect(f"/dojos/{num}")