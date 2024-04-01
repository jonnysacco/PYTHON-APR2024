import random
# 1. Intro to Python 

# 1.1 Indentation & code block
# 1.2 Comments : # or """

# 2. Python Syntax
# 2.1 print on screen
print("Hello World")

# 2.2 Naming Conventions: snake_case (file names, variables, function names)
# Class : Pascal Case 

# 2.3 Declaring variables & Datatypes 
"""
LEFT-HAND-SIDE: Variable name, like a box to store documents
RIGHT-HAND-SIDE: Values , like the document inside
"""

# 2.4 Primitive data types & Composite data types
"""
    Primitive: basic building block of a language. (numbers, boolean, strings)
    Composite: Collections of data (tuples, list, dictionary)
    Built-in functions to confirm datatype: type(var_name)
"""

# 3 Boolean & Number 
# 3.1 Syntax
is_hungry = True # False

total_assignment = 16 # int
happiness = 9.8 #float

# 3.2 Conversion / Casting - Converting datatype 
int_num = 15
int_to_float = float(int_num)

# 3.3 Random number 
print(random.randint(1, 100))

# 4. Strings
# 4.1 Syntax - single quote or double quote. Pick one and stick with it. 
first_name = "Pepper"
last_name = "Chen"

age = 15

# 4.2 Concatenating String (combine 2 strings together)
print(first_name + last_name) # + concat without space

print(first_name, last_name) # , concat with a space

print(first_name, age) # , could concat string with number

print(first_name + str(age)) # + cannot concat string with number

# 4.3 F-String (Literal String interpolation)
print("My cat is",first_name, last_name, "She is", age, "years old" )

print(f"My cat is {first_name} {last_name}. She is {age} years old" ) # My preference

print("My cat is {} {}. She is {} years old".format(first_name, last_name, age))