from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_one(cls, data):
        query = "SELECT * "
        query += "FROM users "
        query += "WHERE first_name=%(first_name)s AND last_name=%(last_name)s;"

        results = connectToMySQL(DATABASE).query_db(query,data)

        if len(results) > 0:
            return cls(results[0])
        else:
            return None