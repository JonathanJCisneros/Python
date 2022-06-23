from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.controllers import user_controller

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query =  "SELECT * "
        query += "FROM users "
        query += "LEFT JOIN friendships ON users.id = friendships.user_id "
        query += "LEFT JOIN users AS users2 ON friendships.friend_id = users2.id;"

        result = connectToMySQL(DATABASE).query_db(query)
        result = result[0]
        user = cls(result)
        friend_data = {
            **result,
            "friend_id" : result['friend_id'],
            "first_name" : result['users2.first_name'],
            "last_name" : result['users2.last_name']
        }
        friend_info = User(friend_data)
        friend = friend_info
        print(friend)
        return friend