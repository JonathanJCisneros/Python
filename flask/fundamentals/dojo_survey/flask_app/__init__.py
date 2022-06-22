from flask import Flask

app = Flask(__name__)
app.secret_key = "Maybe important info.."
DATABASE = "dojo_survey_schema"