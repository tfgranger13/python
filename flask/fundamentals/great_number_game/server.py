from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'a totally new randomly generated string!!!'

import random

@app.route('/')
def index():
    if 'answer' not in session:
        session['answer'] = random.randint(1, 100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():

    # set counter for how many guesses they've made
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1

    # check if higher than answer
    if (int(request.form['guess']) > session['answer']) and (session['counter']<=5):
        session['result'] = 'Too high!'
    # check else if lower than answer
    elif (int(request.form['guess']) < session['answer']) and (session['counter']<=5):
        session['result'] = 'Too low!'
    # check if they have more than 5 guesses
    elif session['counter'] > 5:
        session['result'] = "I'm sorry, you did not guess the correct answer soon enough. Try again"
        session['play_again'] = True
    # or else they are correct
    else:
        session['result'] = f"Correct! It only took you {session['counter']} guesses!"
        session['play_again'] = True
    return redirect('/')

@app.route('/reset')
def start_over():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)   