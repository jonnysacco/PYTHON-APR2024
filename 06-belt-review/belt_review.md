# Code snippets for CRUD


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



