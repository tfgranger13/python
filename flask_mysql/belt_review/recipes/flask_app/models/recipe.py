from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models.user import User

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.made_at = data['made_at']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def get_all_recipes_from_user(cls, data):
        query = "SELECT * FROM recipes WHERE user_id = %(user_id)s;"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        db_recipes = []
        for user in results:
            db_recipes.append(cls(user))
        return db_recipes

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('recipes_schema').query_db(query)
        db_recipes = []
        for user in results:
            db_recipes.append(cls(user))
        return db_recipes

    @classmethod
    def get_single_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s AND user_id = %(user_id)s;"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        db_single_recipe = Recipe(results[0])
        return db_single_recipe

    @classmethod
    def check_db_for_reg_recipe_name(cls, data):
        query = "SELECT * FROM recipes WHERE name = %(name)s AND user_id = %(user_id)s;"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        db_recipes = []
        for item in results:
            db_recipes.append(Recipe(item))
        return db_recipes

    @classmethod
    def add_recipe_to_db(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, made_at, under_30, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(made_at)s, %(under_30)s, %(user_id)s);"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        return results

    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, made_at = %(made_at)s, under_30 = %(under_30)s WHERE id = %(id)s AND user_id = %(user_id)s;"
        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE user_id = %(user_id)s AND id = %(id)s;"
        connectToMySQL('recipes_schema').query_db(query, data)

    @staticmethod
    def validate_reg_info(data):
        is_valid = True
        if len(data['name'])<3 or len(data['name'])>45:
            flash("Name must be between 3 and 45 letters.", 'name')
            is_valid = False
        if len(Recipe.check_db_for_reg_recipe_name(data)) != 0:
            flash("You already have a recipe with that name. Modify the name to make it unique.", 'name')
            is_valid = False
        if len(data['description'])<3:
            flash("Description must be at least 3 letters.", 'description')
            is_valid = False
        if len(data['instructions'])<3:
            flash("Instructions must be at least 3 letters.", 'instructions')
            is_valid = False
        if data['made_at'] == "":
            flash("You must select a date.", 'date')
            is_valid = False
        if data['under_30'] == "":
            flash("You must select if it is under 30 minutes or not.", 'under_30')
            is_valid = False
        return is_valid

    @staticmethod
    def validate_edit_info(data):
        is_valid = True
        if len(data['name'])<3 or len(data['name'])>45:
            flash("Name must be between 3 and 45 letters.", 'name')
            is_valid = False
        if len(data['description'])<3:
            flash("Description must be at least 3 letters.", 'description')
            is_valid = False
        if len(data['instructions'])<3:
            flash("Instructions must be at least 3 letters.", 'instructions')
            is_valid = False
        if data['made_at'] == "":
            flash("You must select a date.", 'date')
            is_valid = False
        if data['under_30'] == "":
            flash("You must select if it is under 30 minutes or not.", 'under_30')
            is_valid = False
        return is_valid