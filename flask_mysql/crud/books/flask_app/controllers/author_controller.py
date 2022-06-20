from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.author_model import Author

@app.route("/")
@app.route("/authors")
def display_all_authors():
    all_authors = Author.get_all()
    return render_template("authors.html", all_authors = all_authors)

@app.route("/new_author", methods = ['POST'])
def add_author():
    Author.create_author(request.form)
    return redirect("/authors")

@app.route("/authors/<int:id>")
def get_list(id):
    data = {
        "id" : id
    }
    author_info = Author.get_list(data)
    return render_template("author_show.html", author_info = author_info)