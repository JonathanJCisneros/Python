from flask import Flask
from flask_app import app
from flask_app.controllers import users_controller



if __name__=="__main__":
    app.run(debug=True)

# "http://127.0.0.1:5000"