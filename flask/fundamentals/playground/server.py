from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def play(multiples = 3, colors = "blue"):
    return render_template("index.html", multiples = multiples, colors = colors)

@app.route('/play/<int:multiples>')
def play_multiples(multiples = 3, colors = "blue"):
    return render_template("index.html", multiples = multiples, colors = colors)

@app.route('/play/<int:multiples>/<string:colors>')
def play_multiples_colors(multiples = 3, colors = "blue"):
    return render_template("index.html", multiples = multiples, colors = colors)


if __name__=="__main__":
    app.run(debug=True)