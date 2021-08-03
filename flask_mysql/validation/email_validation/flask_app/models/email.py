from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails"
        results = connectToMySQL('email_validation').query_db(query)
        emails = []
        for email in results:
            emails.append(cls(email))
        return emails

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM emails WHERE id = %(id)s;"
        results = connectToMySQL('email_validation').query_db(query, data)
        emails = Email(results[0])
        return emails

    @classmethod
    def check_for_email_in_use(cls, data):
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL('email_validation').query_db(query, data)
        emails = []
        for email in results:
            emails.append(Email(email))
        return emails

    @classmethod
    def create_email(cls, data):
        query = 'INSERT INTO emails (email) VALUES (%(email)s);'
        return connectToMySQL('email_validation').query_db(query, data)

    @staticmethod
    def validate_email(email):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(email['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(email['email']) > 255:
            flash("Email address is too long! It must be less than 255 characters!")
            is_valid = False
        if len(Email.check_for_email_in_use({'email': email['email']})) !=0:
            flash("Email address is already in use! Enter a different email address!")
            is_valid = False
        return is_valid