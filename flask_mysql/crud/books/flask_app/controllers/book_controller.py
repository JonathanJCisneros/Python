from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.book_model import Book

@app.route("/books")
def display_all_books():
    all_books = Book.get_all()
    return render_template("books.html", all_books = all_books)

@app.route("/new_book", methods = ['POST'])
def add_book():
    Book.create_book(request.form)
    return redirect("/books")