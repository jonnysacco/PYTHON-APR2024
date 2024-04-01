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