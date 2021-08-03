# start by importing flask and template
from flask import Flask, render_template
app = Flask(__name__)

# create route for home
@app.route('/')
def checkerboard(rows = 8, columns = 8, color_d = "black", color_l = "white"):
    return render_template("index.html", rows = rows, columns = columns, color_d = color_d, color_l = color_l)

@app.route('/<int:rows>')
def checkerboard_rows(rows = 8, columns = 8,  color_d = "black", color_l = "white"):
    return render_template("index.html", rows = rows, columns = columns, color_d = color_d, color_l = color_l)

@app.route('/<int:rows>/<int:columns>')
def checkerboard_rows_columns(rows = 8, columns = 8,  color_d = "black", color_l = "white"):
    return render_template("index.html", rows = rows, columns = columns, color_d = color_d, color_l = color_l)

@app.route('/<int:rows>/<int:columns>/<string:color_d>/<string:color_l>')
def checkerboard_rows_columns_colors(rows = 8, columns = 8,  color_d = "black", color_l = "white"):
    return render_template("index.html", rows = rows, columns = columns, color_d = color_d, color_l = color_l)


# always need to be the very end
if __name__=="__main__":    
    app.run(debug=True)