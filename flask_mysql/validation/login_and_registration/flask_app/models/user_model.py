from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash, session
from flask_bcrypt import Bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_info(cls, data):
        query =  "SELECT * "
        query += "FROM users "
        query += "WHERE email = %(email)s;"
        
        result = connectToMySQL(DATABASE).query_db(query,data)

        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def register(cls, data):
        query =  "INSERT INTO users(first_name, last_name, email, password) "
        query += "VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);"

        new_user = connectToMySQL(DATABASE).query_db(query, data)
        return new_user

    @staticmethod
    def validate_login(data):
        is_valid = True
        if data['email'] == "":
            flash("Please provide your email.", "error_email" )
            isValid = False
        if data['password'] == "":
            flash("Please provide your password.", "error_password")
            isValid = False
        return is_valid

    @staticmethod
    def validate_session():
        if "id" in session:
            return True
        else:
            flash("You must be logged in to see the infromation on this page.", "error_not_logged_in")
            return False

    @staticmethod
    def validate_registration(data):
        isValid = True
        if len(data['first_name']) < 2:
            flash("First name must be at least 2 characters long, letters only!", "error_register_first_name" )
            isValid = False
        if len(data['last_name']) < 2:
            flash("Last name must be at least 2 characters long, letters only!", "error_register_last_name" )
            isValid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Please provide a valid email.", "error_register_email")
            isValid = False
        if len(data['password']) < 8:
            flash("Password must be at least 8 characters long!", "error_register_password")
            isValid = False
        if data['password_confirmation'] != data['password']:
            flash("Your password confirmationan doesn't match.", "error_register_password_confirmation")
        
        return isValid