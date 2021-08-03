from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    dojos = Dojo.get_all()
    return render_template("index.html", dojos = dojos)

@app.route('/dojos/<int:dojos_id>')
def show_dojo(dojos_id):
    ninjas = Ninja.get_all(dojos_id)
    id = dojos_id
    dojos = Dojo.get_info(id)
    return render_template('dojos.html', ninjas = ninjas, dojos = dojos)

@app.route('/new_dojo', methods=['POST'])
def new_dojo():
    data = {'name': request.form['new_dojo_name']}
    Dojo.create(data)
    return redirect ('/')