from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
# from flask_app.models.book_model import Book

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.book_list = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        result = connectToMySQL(DATABASE).query_db(query)
        author_list = []

        for author in result:
            author_list.append(cls(author))

        return author_list

    @classmethod
    def create_author(cls, data):
        query =  "INSERT INTO authors(name) "
        query += "VALUES(%(name)s);"

        result = connectToMySQL(DATABASE).query_db(query,data)

        return result