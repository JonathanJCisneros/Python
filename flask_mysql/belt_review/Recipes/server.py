from flask import Flask
from flask_app import app
from flask_app.controllers import user_controller,recipe_controller

if __name__ == "__main__":
    app.run(debug = True)
app.secret_key = "secret"
DATABASE = "recipes_schema"
