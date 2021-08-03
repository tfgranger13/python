from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def new_ninja():
    dojos = Dojo.get_all()
    return render_template('ninjas.html', dojos = dojos)

@app.route('/create_ninja', methods = ['POST'])
def create_ninja():
    data = {
        'first_name': request.form['ninja_first_name'],
        'last_name': request.form['ninja_last_name'],
        'age': int(request.form['ninja_age']),
        'dojo_id': int(request.form['dojo_names'])
    }
    dojo_id = data['dojo_id']
    Ninja.insert_ninja(data)
    return redirect(f'/dojos/{dojo_id}')