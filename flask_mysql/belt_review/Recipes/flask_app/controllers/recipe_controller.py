from flask import session, request, render_template, redirect, flash
from flask_app import app
from flask_app.models.recipe_model import Recipe

@app.route("/display/recipe")
def display_recipe():
    return render_template("recipe.html")

@app.route("/recipe/new", methods = ['POST'])
def create_recipe():
    data = {
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instructions" : request.form['instructions'],
        "created_at" : request.form['created_at'],
        "under_thirty" : request.form['under_thirty'],
        "user_id" : session['user_id']
    }
    Recipe.create(data)
    return redirect("/dashboard")

@app.route("/dashboard")
def display_recipes():
    recipes = Recipe.get_all()
    return render_template("dashboard.html", recipes = recipes)

@app.route("/recipe/<int:id>")
def recipe_get_one(id):
    data = {
        "id" : id
    }

    recipe = Recipe.get_one(data)
    return render_template("displayRecipe.html", recipe = recipe)

@app.route("/recipe/delete/<int:id>")
def recipe_delete(id):
    data = {
        "id" : id
    }
    Recipe.delete(data)
    return redirect("/dashboard")

@app.route("/recipe/edit/<int:id>")
def something():
    pass