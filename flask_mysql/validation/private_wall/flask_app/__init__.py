from flask import Flask

app = Flask(__name__)
app.secret_key = "secret"
DATABASE = "private_wall_schema"