from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']

    @classmethod
    def get_all(cls):
        query =  "SELECT * "
        query += "FROM emails;"

        result = connectToMySQL(DATABASE).query_db(query)

        email_list = []

        for email in result:
            email_list.append(cls(email))
        return email_list


    @classmethod
    def add_email(cls, data):
        query =  "INSERT INTO emails(email) "
        query += "VALUES(%(email)s);"

        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def check_email(cls, data):
        query =  "SELECT * "
        query += "FROM emails "
        query += "WHERE email = %(email)s;"

        result = connectToMySQL(DATABASE).query_db(query, data)

        if len(result) > 0:
            return cls(result[0])
        else:
            return None

    @classmethod
    def delete_one(cls, data):
        query =  "DELETE FROM emails WHERE id = %(id)s;"

        result = connectToMySQL(DATABASE).query_db(query,data)

        return result

    @staticmethod
    def validate_email(data):
        isValid = True
        if data['email'] == "":
            flash("Please enter an email", "error_email")
            isValid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Please enter a valid email", "error_email_valid")
            isValid = False
        return isValid
