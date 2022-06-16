from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    @classmethod
    def read_all(cls):
        query = "SELECT * FROM users;"

        list = connectToMySQL(DATABASE).query_db(query)
        user_list = []

        for user in list:
            user_list.append(cls(user))

        return user_list

    
    @classmethod
    def sign_up(cls, data):
        query =  "INSERT INTO users(first_name, last_name, email) "
        query += "VALUES(%(fname)s, %(lname)s, %(email)s);"

        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
