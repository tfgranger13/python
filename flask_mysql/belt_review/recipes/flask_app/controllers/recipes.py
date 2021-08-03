from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.recipe import Recipe
from datetime import datetime

@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        flash("I'm sorry, you must be logged in to view that page.", "logging")
        return redirect('/')
    return render_template('recipes_new.html')

@app.route('/recipes/submit', methods=['POST'])
def submit_recipe():
    data = {
        'name': request.form['reg_recipe_name'],
        'description': request.form['reg_recipe_description'],
        'instructions': request.form['reg_recipe_instructions'],
        'made_at': request.form['reg_made_at'],
        'under_30': request.form['under_30'],
        'user_id': session['user_id']
    }
    # validate recipe
    if not Recipe.validate_reg_info(data):
        flash("I'm sorry, please check the information you entered and try again.", 'register')
        return redirect('/recipes/new')
    # submit to db
    Recipe.add_recipe_to_db(data)
    flash('Recipe successfully added!')
    return redirect('/dashboard')

@app.route('/recipes/<int:recipe_id>')
def view_recipe(recipe_id):
    data = {
        'id': recipe_id,
        'user_id': session['user_id']
    }
    recipe_info = Recipe.get_single_recipe(data)
    return render_template('recipes_view.html', recipe_info = recipe_info)

@app.route('/recipes/edit/<int:recipe_id>')
def render_edit_recipe(recipe_id):
    data = {
        'id': recipe_id,
        'user_id': session['user_id']
    }
    recipe_info = Recipe.get_single_recipe(data)
    return render_template("recipes_edit.html", recipe_info = recipe_info)

@app.route('/recipes/submit_edit/<int:recipe_id>', methods = ['POST'])
def submit_edit_recipe(recipe_id):
    data = {
        'id': recipe_id,
        'name': request.form['edit_recipe_name'],
        'description': request.form['edit_recipe_description'],
        'instructions': request.form['edit_recipe_instructions'],
        'made_at': request.form['edit_recipe_made_at'],
        'under_30': request.form['edit_recipe_under_30'],
        'user_id': session['user_id']
    }
    if not Recipe.validate_edit_info(data):
        flash("I'm sorry, please check the information you entered and try again.", "logging")
        return redirect (f'/recipes/edit/{recipe_id}')
    Recipe.update_recipe(data)
    flash("Recipe successfully updated!", "logging")
    return redirect('/dashboard')

@app.route('/recipes/delete/<int:recipe_id>')
def delete_recipe_from_db(recipe_id):
    data = {
        'id': recipe_id,
        'user_id': session['user_id']
    }
    Recipe.delete_recipe(data)
    flash("Recipe has been removed.", "logging")
    return redirect('/dashboard')