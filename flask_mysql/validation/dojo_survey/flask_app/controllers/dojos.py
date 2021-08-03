from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_form():

    # validate with the method in model
    if not Dojo.validate_dojo(request.form):
        # if it fails validation, redirect to home with flash alerts
        return redirect ('/')

    # if it passes validation, take the data and save it in the database
    data = {
            'name': request.form['name'],
            'location': request.form['location'],
            'language': request.form['language'],
            'comment': request.form['comment']
        }
    # the return of the dojo_save method is the ID#; save it as a variable to fstring it into the redirect
    result = Dojo.dojo_save(data)
    return redirect (f'/results/{result}')

@app.route('/results/<int:id>')
def show_results(id):
    # get the info for the id that was redirected
    dojo = Dojo.get_info(id)
    # now you can safely render the results page without duplication
    return render_template('result.html', dojo = dojo)