from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models.ninjas_model import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query =  "SELECT * "
        query += "FROM dojos;"

        result = connectToMySQL(DATABASE).query_db(query)
        result_list = []

        for dojo in result:
            result_list.append(cls(dojo))

        return result_list

    @classmethod
    def create(cls, data):
        query =  "INSERT INTO dojos(name) "
        query += "VALUES(%(dname)s)"

        new_dojo = connectToMySQL(DATABASE).query_db(query, data)

        return new_dojo

    @classmethod
    def get_list(cls, data):
        query =  "SELECT * "
        query += "FROM dojos "
        query += "LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id "
        query += "WHERE dojos.id = %(id)s;"

        result = connectToMySQL(DATABASE).query_db(query, data)
        class_list = []

        for students in result:
            class_list.append(Ninja(students))

        return class_list