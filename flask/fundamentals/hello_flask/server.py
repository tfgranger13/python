from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"



@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# we can make multiple routes, access by localhost:5000/another_route
@app.route('/another_route')
def another_function():
    return "I am another route on the server"

@app.route('/multiply/<int:x>/<int:y>')
def multiply(x, y):
    result = x*y
    return f"The product of {x} and {y} is {result}."

@app.route('/is_palindrome/<string:input_string>')
def is_palindrome(input_string):
    for x in range(0, len(input_string)):

        # old method of iterating from the end of a string
        # if input_string[x]!= input_string[len(input_string) - 1 - x]:
        
        # python-only method for iterating from teh end of a string: use -1 at the index/ negative numbers count backwards from the end
        if input_string[x]!= input_string[-1 - x]:
            return f"{input_string} is not a palindrome."
    return f"{input_string} is a palindrome!"

# always need to be the very end
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

