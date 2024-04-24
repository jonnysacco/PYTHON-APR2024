from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB_NAME
from flask_app.models.sprint import Sprint

class Project:
    def __init__(self, data):
        self.id = data["id"]
        self.idea = data["idea"]
        self.description = data["description"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.sprints = []

    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM projects;
        """
        # call the query and store the return in results
        results = connectToMySQL(DB_NAME).query_db(query)
        #results: a list of dict --> a list of project instance
        projects = []

        for row in results:
            # create a project instance from row (dict)
            new_project = cls(row)
            projects.append(new_project)

        return projects
    
    @classmethod
    def save(cls, form_data):
        query = """
            INSERT INTO projects (idea, description) 
            VALUES (%(idea)s , %(description)s);
        """

        # call the query and store the return in results
        result = connectToMySQL(DB_NAME).query_db(query, form_data) # list of dictionary (with only 1 item)
        # results : [ {idea .....}]
        return result
    
    @classmethod
    def get_one(cls, id): # may need to update the parameters
        # 0. Get the id from the parameters
        # 1. Create the data dictionary for SQL injection
        data = { "id" : id }

        # 2. Write the SELECT query with %(key_name)s to inject id from data
        query = """
            SELECT * FROM projects
            WHERE id = %(id)s;
        """

        # 3. Calling the SQL function with the query and the data
        results = connectToMySQL(DB_NAME).query_db(query, data)
        #    The results should be a list of dictionary with only one item in the list
        # 4. return the first item from the results
        project = cls(results[0])
        return project
    
    @classmethod
    def get_one_with_sprints(cls, id): # may need to update the parameters
        # 0. Get the id from the parameters
        # 1. Create the data dictionary for SQL injection
        data = { "id" : id }

        # 2. Write the SELECT query with %(key_name)s to inject id from data
        query = """
            SELECT * FROM projects
            LEFT JOIN sprints ON projects.id = sprints.project_id
            WHERE projects.id = 1;        
        """

        # 3. Calling the SQL function with the query and the data
        results = connectToMySQL(DB_NAME).query_db(query, data)
        #    The results should be a list of dictionary with only one item in the list
        project = cls(results[0])
        
        for row in results:
            # option 1: (same as the platform)
            sprint_dict = {
                "feature": row["feature"],
                "due_date" : row["due_date"],
                "priority": row["priority"],
                "is_completed": row["is_completed"],
                "project_id": row["project_id"],
                "id" : row["sprints.id"],
                "created_at": row["sprints.created_at"],
                "updated_at": row["sprints.updated_at"]
            }

            #option 2: **row will match all the matching keys
            sprint_dict2 = {
                **row,
                "id" : row["sprints.id"],
                "created_at": row["sprints.created_at"],
                "updated_at": row["sprints.updated_at"]
            }
            each_sprint = Sprint(sprint_dict)
            project.sprints.append(each_sprint)

        # 4. return the first item from the results
        return project