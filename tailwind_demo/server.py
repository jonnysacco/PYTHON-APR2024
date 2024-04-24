from flask_app import app

from flask_app.controllers import projects
from flask_app.controllers import sprints

if __name__ == "__main__":
    app.run(debug=True, port=5001)