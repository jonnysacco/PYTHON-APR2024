# Steps on creating a modularized MVC Flask Project

## Project Setup
1. Create the project folder and cd into the project folder (Same as before)
   - pipenv install flask pymysql
   - pipenv shell
   - Create server.py (Leave it empty for now)
2. Create a folder : flask_app  ``` mkdir flask_app ```
    - Within flask_app, create "__init__.py" 
    ####  __ init __.py
    ```py
    from flask import Flask
    app = Flask(__name__)
    ```
    #### server.py
    ```py
    from flask_app import app

    # Add controller later

    if __name__ == "__main__":
        app.run(debug=True, host="localhost", port=5500)

    ```
    - Within flask_app, create folders /configs, /controllers, /models, /static, /templates
    ``` cd flask_app ``` and ``` mkdir configs controllers models static templates ```
3. Within configs folder, add [mysqlconnection.py](./flask_app/config/mysqlconnection.py)
   - Refer to the platform (Connecting to Database)
   - Take a closer look in the function name to create the instance

4. Within models folder, create the users.py like what we have learnt in OOP
   - import the sql function from the sqlconnection file 
   - Refer to the [pseudo code](./flask_app/models/user.py)
   - Work on the __init__ & get_all first
   - DO NOT PREBUILD EVERYTHING AND TEST AFTER ALL CRUD!

5. Within controllers. create users.py file
    - import the app, all the dependencies (request, session, render_template etc)
    - import the User class from models.user.py
    - Work on the dashboard first. 
    - DO NOT PREBUILD EVERYTHING AND TEST AFTER ALL CRUD!

6. Build the Corresponding template HTML files
    - Work on the dashboard first. Like HTML Table
    - DO NOT PREBUILD EVERYTHING AND TEST AFTER ALL CRUD!

7. Once Dashboard is done, do the rest function by function 
   - (Refer to [models](./flask_app/models/user.py) & [controller](./flask_app/controllers/users.py) notes)
   - Create Page & Process Create
   - Details Page (Get one) 
   - Edit Page & Process Edit
   - Process Delete 