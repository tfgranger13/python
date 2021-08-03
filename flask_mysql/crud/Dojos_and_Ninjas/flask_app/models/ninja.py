from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls, dojos_id):
        data = {'dojo_id': dojos_id}
        query = "SELECT *, ninjas.id AS ninja_id FROM ninjas JOIN dojos ON dojos.id = ninjas.dojo_id WHERE dojo_id = %(dojo_id)s"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        print(result)
        ninjas = []
        for ninja in result:
            ninjas.append(Ninja(ninja))
        return ninjas

    @classmethod
    def insert_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)