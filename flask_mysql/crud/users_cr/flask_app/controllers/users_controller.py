from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.users_model import User

@app.route("/")
@app.route("/users")
def home():
    users_list = User.read_all()
    return render_template("read.html", users_list = users_list)

@app.route("/user/new")
def open_form():
    return render_template("create.html")

@app.route("/new", methods = ['POST'])
def new_user():
    User.sign_up(request.form)
    return redirect("/users")

@app.route("/users/<int:id>")
def show_user(id):
    data = {
        "id" : id
    }
    user_info = User.get_one(data)
    return render_template("readone.html", user_info = user_info)

@app.route("/users/<int:id>/edit")
def edit(id):
    data ={ 
        "id": id
    }

    users = User.get_one(data)
    return render_template("edit.html",users=users)

@app.route("/user/destroy/<int:id>")
def destroy(id):
    data ={
        "id": id
    }
    User.delete(data)
    return redirect("/users")

@app.route("/user/update/<int:id>", methods=['POST'])
def update(id):
    data = {
        **request.form,
        "id" : id
    }
    User.update(data)
    return redirect("/users")