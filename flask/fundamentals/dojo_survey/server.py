from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'dhfoiuwhiofhwioehfiowhEWGFWEFWE'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_form():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    return render_template ('result.html')

if __name__=='__main__':
    app.run(debug=True)