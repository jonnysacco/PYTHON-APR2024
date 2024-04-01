# 5. List & Tuples
# 5.1 Syntax 

#    idx      0             1         2             3
fav_list = ["travel", "snowboard", "tetris", "fixed the bug"]

# Accessing & Update elements
print(fav_list[1])
fav_list[3] = "stardew valley"
print(fav_list)

# append (push) / pop
fav_list.append("Rice ball")

print(fav_list)

fav_list.pop() # Can do .pop(2) to remove tetris
print(fav_list)

fav_list.insert(2, "ski")
print(fav_list)

# 5.2 Python List Overview
# List can be combined easily in Python 
webfund_skills = ["css", "html"]
python_skills = ["python", "flask", "MySQL"]
all_skills = webfund_skills + python_skills
double_skills = all_skills *2


# List can be nested
#       index     0                1                            2 
cat_details = ["Pepper", ["meowing", "sleeping", "scratching"], 15]
#                   index   0            1           2
print(cat_details[1])
print(cat_details[1][2])

# 5.3 More useful built-in functions (Some are explained, some should be tested by youself)
# Functions that RETURN something (Will not change the original list)
int_list = [ 2, 7, 1, 9, 10]

print(max(int_list))
print(sorted(int_list)) # Only return a sorted list, no change to the original 
print(int_list)
# Function that update the original list but return None
int_list.sort()
print(int_list)

# 5.4 Tuples: List that are immutable (Cannot change)
tuple_data = ('physics', 'chemistry', 1997, 2000)


# 6. Conditionals
happiness = 8

# 6.1 Syntax
if happiness > 9: 
    print("I am very happy")
elif happiness > 5:
    print("I am happy")
else:
    print("Cheer up!")


# 6.2 More logical operators
has_food = False
is_full = False

# print satisfied if I am either full or have food
if has_food or is_full:
    print("I am satisfied")
else:
    print("I am not satisfied")

# print not satisfied if I am not full and don't have food
if not has_food and not is_full:
    print("I am not satisfied!!!!")

if has_food == False and is_full == False:
    print("I am not satisfied!!!!")

# 7. Loops
# 7.1 Loop with range
for i in range(5): # condition: j < 5
    print(i)

#### BEHIND THE SCENE
j = 0 # starting point
while j < 5: # for-loop range condition
    print(j)
    j += 1 # j = j+1

# 7.2 More arguments with for-loop
for i in range(1 , 20, 3):
    print(i)

j = 1 # starting point
while j < 20: # for-loop range condition
    # print(j)
    j += 3 # j = j+3

# 7.3 Loop through String/list
for i in range(len(fav_list)):
    print(i, fav_list[i])

# fav_list = ["travel", "snowboard", "tetris", "fixed the bug"]
"""
    for A in B:
        print(_____)
    A: how you call it as a variable
    B: The list you are looping through
"""
for each_element in fav_list:
    print(each_element)

name = "Pepper"
for each_letter in name:
    print(each_letter)

# 7.4 CONTINUE & BREAK 
