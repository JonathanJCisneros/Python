from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        result = connectToMySQL(DATABASE).query_db(query)
        book_list = []

        for book in result:
            book_list.append(cls(book))

        return book_list

    @classmethod
    def create_book(cls, data):
        query =  "INSERT INTO books(title, num_of_pages) "
        query += "VALUES(%(title)s, %(num_of_pages)s);"

        result = connectToMySQL(DATABASE).query_db(query,data)

        return result