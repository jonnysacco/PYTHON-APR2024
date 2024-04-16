# Code snippets for CRUD
## Table of content
[Route protection & Session](#route-protection--session)
- [1. log /reg session](#1-login--register-session)
- [2. Route protection & Welcome message](#2-route-protection--welcome-message)
- [3. Preventing non-owning users from editing/deleting](#3-preventing-non-owning-users-from-editingdeleting)

[CRUD setup](#1n-class-association)
- [1. Models & erd](#erd)
- [2. SQL examples](#sql-to-be-used-later-in-models-classmethod)

[CRUD Logic](#3-crud-logic)
- [1. Create](#create)
- [2. Dashboard](#dashboard)
- [3. Details](#details)
- [4. Edit](#edit)
- [5. Delete](#delete)

[Testing & Checklist](exam.md)


## Route protection & Session
### 1. Login / Register session
#### Controller - /register
```python
### REGISTER: get the user_id from .save & store it in session
user_id = User.save(updated_form)
session["user_id"] = user_id
```

#### Controller - /login
```python
### LOGIN: get the potential_user and store the id in session if the login credentials are valid
session["user_id"] = potential_user.id
```

#### Controller - /logout
```python
### clear session if it is logged out
session.clear()
```

### 2. Route protection & Welcome message
(Important on dashboard, optional for all other pages)
#### Controller - all other pages
```python
    # If the user_id is not in the session, the user is never logged in.
    if not "user_id" in session:
        return redirect("/")
```
#### Showing Welcome, Pepper on dashboard
```python
    # Option 1:  get the user using the session
    logged_user = User.get_one_by_id(session["user_id"])
    # Option 2: store the name in the session when register/login
    # You could decide on the logic on that
```

### 3. Preventing non-owning users from editing/deleting
#### Controller - Edit / Delete (Backend authentication)
```python
    ## Backend authentication - make sure owner_id is the same as the logged user
    item = Item.get_one_with_owner(id)
    if item.owner_id != session["user_id"]:
        flash("Do not delete someone else's item")
        return redirect("/")
    ###########################
```
#### Templates - Dashboard (Conditional Rendering)
Edit & Delete only shows up if the logged user_id is the same as the owner_id
```html
    {% if each_item.owner_id == session.user_id %}
        <td><a href="/items/{{each_item.id}}/edit">Edit</a></td>
        <td><a href="/items/{{each_item.id}}/delete">Delete</a></td>
    {% endif %}
```

## 1:n class association 
### ERD
- Make sure there is 1:n with a foreign key 
- Make sure primary key checked AI 
- created_at & updated_at should be in DATETIME with default values
- Boolean would be TINYINT (1 as True, 0 as False)
- Date datatype will work very well with input type="date". Do not use DATETIME if you only need the date

### models
- Constructor need to include all the table field attribute
- Both User class & the other class include class association
  ```py
  # CRUD class (like Item class)
  def __init__(self, data):
        # SAME FIELDS FROM DB TABLE
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.owner_id = data["owner_id"]
        #####################################
        # Include the class association  
        self.owner = None 
        ####################################
  ```

### SQL (To be used later in models @classmethod)
- Dashboard & Details need LEFT JOIN (These queries will be in model get_all & get_one)
```SQL
    -- Example of GET ALL query (owner_id is the FK in this case)
    SELECT * FROM items
    LEFT JOIN users ON items.owner_id = users.id;
```

```SQL
    -- Example of GET ONE query (owner_id is the FK in this case)
    SELECT * FROM items
    LEFT JOIN users ON items.owner_id = users.id
    WHERE items.id = 3;
```
- Create requires FK 
```SQL
    -- Example of CREATE query (owner_id is the FK in this case)
    INSERT INTO items (name, description, pickup_date, is_functional, owner_id)
    VALUES ("cat food", "very fishy", "2024-04-15", "1", 1 );
```
- Update does not require FK
```sql
    -- Example of UPDATE query 
    UPDATE items
    SET name = "test name", 
    description = "test description" , 
    pickup_date = "2024-04-01", 
    is_functional = "0"
    WHERE id = 3;
```
- Delete need to add condition
```sql
    -- Example of DELETE query 
    DELETE FROM items
    WHERE id = 3
```

## 3 CRUD logic
### Create
#### Create Page
- Make sure the form has all the input name same as the DB

#### Create Process Route
- [Validation example](./validation.md)
- When executing .save(form_data), make sure that form_data include the foreign key (Either way)
    1. Could add the FK in the form page 
    ```html
        <input type="hidden" name="owner_id" value="{{session.user_id}}" /> 
    ```
    2. Could add the FK before .save
    ```python
        form_data = {
            **request.form,
            "owner_id" : session["user_id"]
        }
    ```
#### Errors
If anything goes wrong, think about where it went wrong
1. The route looks weird after submit ?
   - Check the form action
2. The route looks good but validation doesn't show up? 
   - Check your flash message in template
3. It never bypass in the validation check and stay in the form? 
   - Check your validation method
4. It tried to save but got errors? 
   - Check your query & terminal

### Dashboard
#### Models
- Make sure the get_all query includes LEFT JOIN
- After getting the list of results, think about the logic to create a list of item with user object attached
- Pseudocode for the logic
    ```python
    # results is the list of items (with owner info) 
    # Create the list of item
    items = []
    # loop through the results, and within each row
    for row in results:
        # 1. create the Item instance 
        # 2. create the custom dictionary to create User instance
        # 3. Create a User instance from the custom dict
        # 4. Assign this newly created user to item.owner
        # 5. push the item in
    return items
  ```
- Template file for the dashboard - Using for-loop to display each item
  ```html
    {% for each_item in item_list: %}
    
    {% endfor %}
  ```

### Details
#### Controller
```python
# Make sure the route & method includes id
@app.route("/items/<int:id>")
def details_page(id):

```

#### Models
- It requires SQL injection --> Need to have a dictionary with "id" as one of the keys
- The get_one query includes LEFT JOIN [query example](#sql-to-be-used-later-in-models-classmethod)
- After getting the list of results, think about the logic to create ONE item with user object attached
- Pseudocode for the logic
    ```python
    # results is the list of items (with owner info) 
    # We only need the first row as it is get_one
    row = results[0]
    # 1. create the Item instance 
    # 2. create the custom dictionary to create User instance
    # 3. Create a User instance from the custom dict
    # 4. Assign this newly created user to item.owner
    # 5. Return that item with the owner
  ```
#### Errors
1. The page rendered properly but all details are not shown up? 
   - Check if you passed the data to the template file & Check the variable name!
2. The route broke?
   - If the URL looks weird, it's on the html link
3. The route broke? 
   - If the URL looks good but cannot find route, could be the controller

### Edit
#### Edit page
1. Controller - same as Details page
2. Template file - Can copy from create page with some changes
   - form action needs to include the id
   - all the input need to add the ``` value = "{{item.description}}" ```
   - For textarea, the value will be between ``` <textarea name="description">{{item.description}}</textarea>```
   - For radio button, may need some logic ``` {{ "checked" if item.is_function == 1 }}``` for the True button, oppsoite for the False button
3. Make sure the edit form is pre-populated properly before moving on

#### Edit Process
1. Models 
   - Check the query first ([sample query](#sql-to-be-used-later-in-models-classmethod))
   - Make sure the form_data included the id (could be from hidden input or controller)

2. Controller
   - (Optional) Test if it is valid before saving
   - (Optional) If the user_id from session is not the same owner_id, redirect them back to dashboard [HINT](#3-preventing-non-owning-users-from-editingdeleting)
   - Successful EDIT should work

#### Errors
1. The page broke? 
   - Check the URL & app.route
2. The fields are not pre-populated?
   - Check what data you passed in render_template, did you send in the right info?
3. It broke when I update? 
   - Check the query & terminal

### Delete
1. Create the link/form in the template file
2. Make sure the corresponding route & query is right 






