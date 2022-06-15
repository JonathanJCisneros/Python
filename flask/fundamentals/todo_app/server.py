from flask import Flask, render_template, request, redirect, session
from todo import Todo

app = Flask(__name__)
app.secret_key = "secret"


@app.route("/")
@app.route("/todos")
def get_all_todos():
    if "num_of_visits" in session:
        session["num_of_visits"] += 1
    else:
        session["num_of_visits"] = 1

    list_of_todos = Todo.get_all()
    return render_template("index.html", first_name = "Alexander", list_of_todos = list_of_todos)

@app.route("/todo/new")
def display_create_todo():
    return render_template("todoForm.html")

@app.route("/todo/new", methods = ['POST'])
def create_todo():
    Todo.create(request.form)
    return redirect("/todos")


# "http://127.0.0.1:5000"

if __name__ == "__main__":
    app.run(debug = True)

"""
GET - read and display
URL of the route to display all: the name of the list or dictionary that we are about to display
Example: "/todos"
Example: "/users"

Function: get_all_todos()

URL of the route to display one: the name of the list in singular that we are about to display follow by the id
Example: "/todo/<int:id>"
Example: "/user/<int:id>"

Function: get_todo_by_id(id)

POST - create
URL of the route to create something new: name of the list in singular that we are about to create followed by the keyword /new
Example: "/todo/new"
Example: "/user/new"

Function: create_todo()

PUT - update
URL of the route to update something already existing: the name of the list in singular that we are about to update, followed by the id, followed by the keyword /update / edit
Example: "/todo/<int:id>/update"
Example: "/user/<int:id>/update"

Function: update_todo_by_id(id)

DELETE - remove
URL of the route to delete something already existing: the name of the list in singular that we are about to update, followed by the id, followed by the keyword /delete /remove
Example: "/todo/<int:id>/delete"
Example: "/user/<int:id>/delete"

Function: delete_todo_by_id(id)

"""