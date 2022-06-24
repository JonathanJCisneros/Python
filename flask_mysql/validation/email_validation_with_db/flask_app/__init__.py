from flask import Flask

app = Flask(__name__)
app.secret_key = "shhh"
DATABASE = "email_schema"