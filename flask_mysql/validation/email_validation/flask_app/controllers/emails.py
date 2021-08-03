from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success/<int:id>')
def dashboard(id):
    data = {'id': id}
    new_email = Email.get_one(data)
    print(new_email)
    all_emails = Email.get_all()
    return render_template('dashboard.html', new_email = new_email, all_emails = all_emails)

@app.route('/submit_email', methods=['POST'])
def process_email():
    if not Email.validate_email(request.form):
            return redirect ('/')
    data = {
        'email': request.form['email']
    }
    result = Email.create_email(data)
    return redirect (f'/success/{result}')