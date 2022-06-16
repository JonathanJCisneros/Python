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
        session['id'] = result.id
        return redirect("/todos")

@app.route("/display/user/")
def get_user_by_id():
    data = {
        "id" : session['id']
    }
    current_user = User.get_one_with_todos(data)

    if current_user == None:
        user_data = {
            "first_name" : session["first_name"],
            "last_name" : session["last_name"]
        }
    
        current_user = User.get_one(user_data)
    return render_template("userInfo.html", current_user = current_user)