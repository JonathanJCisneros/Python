from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.friend = []

    @classmethod
    def get_all_friendships(cls):
        query =  "SELECT * "
        query += "FROM users "
        query += "LEFT JOIN friendships ON users.id = friendships.user_id "
        query += "LEFT JOIN users AS users2 ON friendships.friend_id = users2.id;"

        result = connectToMySQL(DATABASE).query_db(query)
        
        friends = cls(result[0])

        for friend in result:
            data = {
                "friend_id" : friend['users2.id'],
                "friend_first" : friend['users2.first_name'],
                "friend_last" : friend['users2.last_name'],
                "friend_created_at" : friend['users2.created_at'],
                "friend_updated_at" : friend['users2.updated_at']
            }
            friends.friend.append(User(data))
            return friends
                
