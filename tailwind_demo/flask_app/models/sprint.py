from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB_NAME
from flask import flash
import re	# the regex module
# create a regular expression object that we'll use later   
NO_SPECIAL_CHARACTER_REGEX = re.compile(r'^[a-zA-Z0-9 ]*$') 

class Sprint:
    def __init__(self, data):
        self.id = data["id"]
        self.feature = data["feature"]
        self.due_date = data["due_date"]
        self.is_completed = data["is_completed"]
        self.priority = data["priority"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.project_id = data["project_id"]
        

    @classmethod
    def save(cls, form_data):
        query ="""
            INSERT INTO sprints (feature, due_date, is_completed, priority, project_id)
            VALUES(%(feature)s, %(due_date)s, %(is_completed)s, %(priority)s,%(project_id)s);
        """
        result = connectToMySQL(DB_NAME).query_db(query, form_data) # list of dictionary (with only 1 item)
        return result
    
    @staticmethod
    def validate_sprint(data):
        is_valid = True 

        # check the length of a string
        if len(data["feature"]) < 3:
            flash("Feature must be at least 3 characters")
            is_valid = False

        # Check number (turn the string to int)
        if data["priority"] and int(data["priority"]) < 0:
            flash("Priority must be positive")
            is_valid = False

        # Check if the key is in the form
        if not "is_completed" in data:
            flash("Is it completed?")
            is_valid = False

        # Check if priority is null
        if not data["priority"]:
            flash("Priority is required")
            is_valid = False

        # Check if the feature is following regex pattern
        if not NO_SPECIAL_CHARACTER_REGEX.match(data['feature']): 
            flash("Feature cannot have special characters")
            is_valid = False

        return is_valid