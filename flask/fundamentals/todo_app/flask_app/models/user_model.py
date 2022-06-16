from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models.todo_model import Todo

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

        result = connectToMySQL(DATABASE).query_db(query,data)

        if len(result) > 0:
            return cls(result[0])
        else:
            return None

    @classmethod
    def get_one_with_todos(cls, data):
        query =  "SELECT * "
        query += "FROM users "
        query += "JOIN todos ON users.id = todos.ser_id "
        query += "WHERE users.id = %(id)s;"

        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) > 0:
            current_user = cls(result[0])
            for row in result:
                current_todo = {
                    "id" : row["todos.id"],
                    "todo" : row["todo"],
                    "status" : row["status"],
                    "created_at" : row["created_at"],
                    "updated_at" : row["updated_at"],
                    "user_id" : row["user_id"]
                }
                todo = Todo(current_todo)
                list_todos.append(todo)
            current_user.list_todos = list_todos
            return current_user
        return None