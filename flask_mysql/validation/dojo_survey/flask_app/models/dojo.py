from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_info(cls, id):
        data = {'id': id}
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        results = connectToMySQL('dojo_survey_schema').query_db(query, data)
        # this turns the results into a useable form
        dojos = Dojo(results[0])
        return dojos

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo['name']) == 0:
            flash("The name field is required.")
            is_valid = False
        if len(dojo['location']) == 0:
            flash("The location field is required.")
            is_valid = False
        if len(dojo['language']) == 0:
            flash("The language field is required.")
            is_valid = False
        if len(dojo['comment']) == 0:
            flash("The comment field is required.")
            is_valid = False
        return is_valid

    @classmethod
    def dojo_save(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        return connectToMySQL('dojo_survey_schema').query_db(query, data)
        # this will return the id# of the item added to the database