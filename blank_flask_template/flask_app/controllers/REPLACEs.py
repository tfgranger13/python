from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.REPLACE import REPLACE

@app.route('/')
def index():
    return render_template('index.html')