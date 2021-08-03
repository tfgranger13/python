from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    count = int(request.form['apple']) + int(request.form['strawberry']) + int(request.form['raspberry'])
    customer_name = f"{request.form['first_name']} {request.form['last_name']}"
    print(f"Charging {customer_name} for {count} fruits.")
    return render_template("checkout.html", count = count, customer_name = customer_name)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    