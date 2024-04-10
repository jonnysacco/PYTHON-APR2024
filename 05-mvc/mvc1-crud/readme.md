# Steps on creating a modularized MVC Flask Project

## Project Setup
0. Look at the wireframe and create the ERD & Schema
   - ERD: id is AI, required items are NN, created_at & updated_at have default TIMESTAMP
   - Forward engineer
   - Insert a few rows to test it

1. Create the project folder and cd into the project folder (Same as before)
   - pipenv install flask pymysql
   - pipenv shell
   - Create server.py (Leave it empty for now)

2. Folder structure
   - Create a folder : flask_app  ``` mkdir flask_app ```
   - Within flask_app, create "__init__.py" 
   - Within flask_app, create folders /configs, /controllers, /models, /static, /templates
    ``` cd flask_app ``` and ``` mkdir configs controllers models static templates ```
    - add models/project.py, controllers/projects.py, configs/mysqlconnection.py
    - add all the corresponding html template files (According to the wireframe)

    ####  __ init __.py
    ```py
    from flask import Flask
    app = Flask(__name__)

    app.secret_key = "shhhhhhhhhhh"
    DB_NAME = "projects_schema"
    ```
    #### server.py
    ```py
    from flask_app import app
    from flask_app.controllers import projects

    if __name__ == "__main__":
        app.run(debug=True, port=5001)
    ```
    
3. Within configs folder, add [mysqlconnection.py](./flask_app/config/mysqlconnection.py)
   - Refer to the platform (Connecting to Database)

4. Within models folder, create the projects.py like what we have learnt in OOP
   - import the sql function from the sqlconnection file 
   - import the DB_NAME from app
   - Refer to the [pseudo code](./flask_app/models/project.py)
   - Work on the constructor & get_all & placeholder method first
   - DO NOT PREBUILD EVERYTHING!

5. Within controllers. create projects.py file
    - import the app, all the dependencies (request, session, render_template etc)
    - import the Project class from models.project.py
    - Work on the dashboard & add some placeholder method first. 
    - DO NOT PREBUILD EVERYTHING!

6. Complete the Corresponding template HTML files
    - Work on the dashboard first. Like HTML Table
    - DO NOT PREBUILD EVERYTHING!

7. Once Dashboard is done, do the rest function by function 
   - (Refer to [models](./flask_app/models/project.py) & [controller](./flask_app/controllers/projects.py) notes)
   - Create Page & Process Create
   - Details Page (Get one) 
   - Edit Page & Process Edit
   - Process Delete 