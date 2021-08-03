from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'randomly generated string!!!' # set a secret key for security purposes



@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    if 'real_views' in session:
        session['real_views'] += 1
    else:
        session['real_views'] = 1
    return render_template('index.html')

@app.route('/add_to_counter', methods=['POST'])
def add_to_counter():
    session['counter'] += 1
    return redirect('/')

@app.route('/counted')
def counted_view():
    session['counter'] += 1
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()		# clears all keys
    # session.pop('key_name')		# clears a specific key
    return redirect('/')

@app.route('/add_value_to_counter', methods = ['POST'])
def add_value():
    session['counter'] += int(request.form['value'])
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    