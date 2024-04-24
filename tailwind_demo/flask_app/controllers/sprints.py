from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.project import Project
from flask_app.models.sprint import Sprint

# Create sprint page
@app.route("/sprints/new")
def create_sprint_page():
    project_list = Project.get_all()
    return render_template("sprint_create.html", project_list=project_list)

# Create sprint process
@app.route("/sprints/new/process", methods=["POST"])
def process_sprint_create():
    if not Sprint.validate_sprint(request.form): # if it returns False
       return redirect("/sprints/new")
    # validate before we save
    Sprint.save(request.form)
    return redirect("/projects")