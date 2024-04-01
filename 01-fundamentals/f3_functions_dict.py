
# 8. Functions
# 8.1 Function overview & Syntax
def greet(name): # defining a function/tool to use
    print("Hello,", name)
"""
    name(line 4): parameter - what the function will take in
    "Heidi"(line 10) : argument - what you provide to the function
"""
greet("Heidi")
greet("Pepper")
greet("David")

def get_full_name(first_name, last_name):
    return f"{first_name} {last_name}"

cat_name = get_full_name("Pepper", "Chen")
print(cat_name)

# 8.2 Default parameters & arguments
def greet2(name="Stranger"): # defining a function/tool to use
    print("Hello,", name)

greet2()
"""
    BEHIND THE SCENE
    1. greet2() did not provide any argument
    2. As no argument is given, name = "Strange" following function parameters
    3. Go to line 21 to run the code block
"""
greet2(cat_name)

# 9. Dictionaries 
# 9.1 Syntax : key-value pair
project = {
    "title" : "Hello World",
    "completion": 1,
    "is_core" : False
}

print(project)
# 9.2 Manipulating Dict &  Built-in function
###### ACCESSING 
print(project["title"])
###### REMOVE
project.pop("is_core") # Put the key inside the ()

###### UPDATE
project["completion"] = 0.8
print(project)

project["language"] = "Python"
print(project)

if "owner" not in project: # Checking if project has a key "owner"
    print("There is no owner")

# 9.3 Looping through dictionary
for each_key in project:
    print(each_key)
    print(project[each_key]) # "title", "completion", "language"

# 9.4 Nested loop & Dictionary
project_list = [
    {"title": "Hello World", "completion": 1}, # idx: 0
    {"title": "For loop basic I", "completion": 0.7},  # idx: 1
    {"title": "Nested Dict", "completion": 0}  # idx: 2
]

# update the title of idx 1 ("For Loop basic I")
project_list[1]["title"] = "For loop basic II"
print(project_list)

# each_project: {"title": "For loop basic I", "completion": 0.7}
for each_project in project_list:
    print(each_project)
    for each_key in each_project:
        print(f"{each_key} - {each_project[each_key]}")


resume_data = {
    "skills": ["front-end", "back-end", "database"],
    "languages": ["Python", "JavaScript"],
    "hobbies":["snowboarding", "tetris"]
}

for each_key in resume_data:
    print(each_key)
    print(resume_data[each_key])