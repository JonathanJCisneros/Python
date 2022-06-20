from flask import Flask

app = Flask(__name__)
app.secret_key = "hi"
DATABASE = "books_schema"