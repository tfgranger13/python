from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session

import re
NAME_REGEX = re.compile(r'^[a-zA-Z]')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('login_and_registration_schema').query_db(query)
        db_users = []
        for user in results:
            db_users.append(cls(user))
        return db_users

    @classmethod
    def get_single_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('login_and_registration_schema').query_db(query, data)
        db_single_user = User(results[0])
        return db_single_user

    @staticmethod
    def get_user_by_email(data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('login_and_registration_schema').query_db(query, data)
        db_single_user = User(results[0])
        return db_single_user

    @classmethod
    def check_db_for_reg_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('login_and_registration_schema').query_db(query, data)
        db_emails = []
        for item in results:
            db_emails.append(User(item))
        return db_emails

    @classmethod
    def add_to_db(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        results = connectToMySQL('login_and_registration_schema').query_db(query, data)
        return results

    @staticmethod
    def validate_reg_info(data, reg_confirm_password):
        is_valid = True
        if len(data['first_name'])<2 or len(data['first_name'])>45:
            flash("First name must be between 2 and 45 letters.", 'first_name')
            is_valid = False
        if not NAME_REGEX.match(data['first_name']):
            flash("First name must be written with only letters.", 'first_name')
            is_valid = False
        if len(data['last_name'])<2 or len(data['last_name'])>45:
            flash("Last name must be between 2 and 45 letters.", 'last_name')
            is_valid = False
        if not NAME_REGEX.match(data['last_name']):
            flash("Last name must be written with only letters.", 'last_name')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address.", 'email')
            is_valid = False
        if len(User.check_db_for_reg_email({'email': data['email']})) != 0:
            flash("Email address is already in use.", 'email')
            is_valid = False
        if len(data['password'])<8:
            flash("Password must be at least 8 characters.", 'password')
            is_valid = False
        if data['password'] != reg_confirm_password:
            flash("Password does not match Confirm Password.", 'confirm_password')
            is_valid = False
        return is_valid

