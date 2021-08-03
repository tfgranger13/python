from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.user import User

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users = users)

@app.route('/users')
def users():
    return redirect('/')

@app.route('/users/new')
def new_user():
    return render_template('new.html')

@app.route('/users/create', methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email" : request.form["email"]
    }
    # set a variable for the user id that is returned from the mysql connector in the User.save() method
    user_id = User.save(data)
    return redirect(f'/users/{user_id}')

@app.route('/users/<int:user_id>')
def view_user(user_id):
    data = {'id': user_id}
    user = User.view(data)
    return render_template('user.html', user = user)

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    data = {'id': user_id}
    user = User.view(data)
    return render_template('edit_user.html', user = user)

@app.route('/users/<int:user_id>/update', methods=['POST'])
def update_user(user_id):
    data = {
        "id": user_id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email" : request.form["email"]
    }
    User.update(data)
    id = data['id']
    return redirect(f'/users/{id}')
    # return render_template('user.html', user = user)

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    data = {'id': user_id}
    User.delete(data)
    return redirect('/')