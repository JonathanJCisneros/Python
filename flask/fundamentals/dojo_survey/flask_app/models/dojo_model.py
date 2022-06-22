from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.controllers import dojo_controller
from flask import flash, session

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_one(cls, data):
        query =  "INSERT INTO dojos(name, location, language, comment) "
        query += "VALUES(%(name)s, %(location)s, %(language)s, %(comments)s);"

        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_survey(data):
        isValid = True
        if data['name'] == "":
            flash("You must provide your name.", "error_register_first_name" )
            isValid = False
        if len(data['name']) < 3:
            flash("Your name must have at least 3 characters.", "error_register_first_name" )
            isValid = False
        if data['location'] == "":
            flash("You must choose a location.", "error_register_location" )
            isValid = False
        if data['language'] == "":
            flash("You must choose a language.", "error_register_language")
            isValid = False
        if len(data['comments']) < 3:
            flash("Your comment must be at least 3 characters long.", "error_register_comments")
            isValid = False
        return isValid