# start by importing flask
from flask import Flask
app = Flask(__name__)

# create route for home
@app.route('/')
def hello_world():
    return 'Hello World!'

# have it say "Dojo!"
@app.route('/dojo')
def dojo():
    return 'Dojo!'

# say 'Hi [string (but capitalize first letter?)]!'
@app.route('/say/<string:word>')
def hi_name(word):
    return f"Hi {word}!"

# repeat a word a certain number of times
@app.route('/repeat/<int:number>/<string:word>')
def repeat_word(number, word):
    output = ""
    for x in range(number):
        output += f"{str(word)} "
    return output


# always need to be the very end
if __name__=="__main__":    
    app.run(debug=True)