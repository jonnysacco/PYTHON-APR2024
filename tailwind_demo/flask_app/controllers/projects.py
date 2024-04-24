from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.project import Project

# project main (dashboard & create )
@app.route("/")
@app.route("/projects")
def project_main_page():
    project_list = Project.get_all()
    return render_template("project_main.html", project_list=project_list)

# project create process
@app.route("/projects/new/process", methods=["POST"])
def process_project_create():
    Project.save(request.form)
    return redirect("/projects")

# project details : /projects/3
@app.route("/projects/<int:id>")
def project_details(id):
    project = Project.get_one_with_sprints(id)
    return render_template("project_details.html", project=project)