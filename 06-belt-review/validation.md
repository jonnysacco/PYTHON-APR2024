# Validation

## models/sprint.py

```py
    ## Added the static method for validation

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

```
### For pattern validation 
```py
    # added the following before class Sprint:
    import re	
    # Allow only letter/number/space
    NO_SPECIAL_CHARACTER_REGEX = re.compile(r'^[a-zA-Z0-9 ]*$')  
```