from mysqlconnection import connectToMySQL

class Todo:
    def __init__(self, data):
        self.id = data['id']
        self.todo = data['todo']
        self.status = data['status']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM todos;"

        result = connectToMySQL("todos_scheme").query_db(query)
        list_todos = []

        for todo in result:
            list_todos.append(cls(todo))

        return list_todos

    @classmethod
    def create(cls, data):
        query = "INSERT INTO todos(todo, status, user_id) " 
        query += "VALUES(%(todo)s, %(status)s, %(user_id)s);"

        id_new_todo = connectToMySQL("todos_scheme").query_db(query, data)

        print(id_new_todo)
        return id_new_todo

"""
SELECT:
def get_all()
def get_one()

INSERT
def create()

DELETE
def delete_one()

UPDATE
def update_one()
def edit_one()
"""


