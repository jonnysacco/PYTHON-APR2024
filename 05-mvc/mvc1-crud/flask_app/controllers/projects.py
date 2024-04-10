from flask_app import app
from flask import render_template, request, redirect, session
# import the Project class from the project model file 

# DASHBOARD - SHOW ALL
@app.route("/")
def index():
    pass # REPLACE PASS WITH YOUR OWN CODE
    # 1. call the get all classmethod from ClassName to get all friends
    # 2. return render_template with the list of dictionaries

# CREATE
# Show Create form         
@app.route("/projects/create")
def create_form():
    pass # REPLACE PASS WITH YOUR OWN CODE    
    # return render_template for the form

# Process Create form   
@app.route("/projects/create", methods=["POST"])
def process_create_form():
    pass # REPLACE PASS WITH YOUR OWN CODE    
    # 1. Call the .save method from Project class with request.form as the argument
    # 2. Redirect

# Get One
@app.route("/projects/<int:id>")
def one_project(id):
    pass # REPLACE PASS WITH YOUR OWN CODE
    # 0. Get the id from the route
    # 1. Call the .get_one method from Project class with id as the argument
    # 2. return render_template with the project

# EDIT
# Show Edit form
@app.route("/projects/<int:id>/edit")
def edit_form(id):
    pass # REPLACE PASS WITH YOUR OWN CODE    
    ##### SAME AS one_project #####
    # 0. Get the id from the route
    # 1. Call the .get_one method from Project class with id as the argument
    # 2. return render_template with the project



@app.route("/projects/<int:id>/edit", methods=["POST"])
def edit_project(id):
    pass # REPLACE PASS WITH YOUR OWN CODE
    # 0. Get the id from the route
    # 1. Make sure id is within the dictionary we pass in for the next step
    # 2. Call the .edit_one method from Project class with a dictionary with all form data & id
    # 3. redirect


# Process Delete
@app.route("/projects/<int:id>/delete")
def delete_one(id):
    pass # REPLACE PASS WITH YOUR OWN CODE
    # 0. Get the id from the route
    # 1. Call the .delete_by_id method from project class with id as the argument
    # 2. Redirect