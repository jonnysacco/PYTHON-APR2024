# import the function from mysqlconnection
# from flask_app.folder_name.file_name import function_name

class Project:
    def __init__(self, data):
        pass # REPLACE PASS WITH YOUR OWN CODE
        # Make sure you match all the class attributes with database columns
        # Refer to the platform - Database Conecton - Connecting to a database

    @classmethod
    def get_all(cls):
        query = "QUERY_TO_EXECUTE" # 1. Write the SELECT query to execute
        # 2. Call the query by executing the function from import
        results = connect_to_sql("YOUR_OWN_SCHEMA").query_db(query)

        """
            results for get_all query will return a list of dictionary [ { }, { }, { }]
            for more code & logic, refer to the platform OR W1D3 3pm OOP Challenge
        """

    @classmethod
    def save(cls, form_data): # data refers to the form data
        pass # REPLACE PASS WITH YOUR CODE
        # Refer to CRUD - From Form to DB
        # 0. Get the form_data from the parameter
        # 1. Write the INSERT query with %(key_name)s to inject variables from form_data
        # 2. Calling the function with the query and the data



    @classmethod
    def get_one(cls, id):
        pass # REPLACE PASS WITH YOUR CODE
        # 0. Get the id from the parameters
        # 1. Create the data dictionary for SQL injection
        # 2. Write the SELECT query with %(key_name)s to inject id from data
        # 3. Calling the SQL function with the query and the data
        #    The results should be a list of dictionary with only one item in the list
        # 4. return the first item from the results

    @classmethod
    def edit_one(cls, data):
        pass # REPLACE PASS WITH YOUR CODE
        # 0. Get the form_data from the parameter (Could include also id in the form)
        # 1. Write the UPDATE query with %(key_name)s to set all the variables 
        #    Add the condition to make sure the id is right
        # 2. Calling the SQL function with the query and the data
        # 3. Return anything (Nothing is expected )
        

    @classmethod
    def delete_one(cls, id):
        pass # REPLACE PASS WITH YOUR CODE
        # 0. Get the id from the parameters
        # 1. Create the data dictionary with id for SQL injection
        # 2. Write the DELETE query with %(key_name)s for the condition
        # 3. Calling the SQL function with the query and the data
        # 4. Return anything (Nothing is expected )


