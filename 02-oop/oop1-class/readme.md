# 0. OOP Glossary
| Term | Explanation |
|------|-------------|
| Class | The blueprint/definition of the object|
| Instance|the object that is created based on the class|
|Attributes| The properties of the class (What it has)
|Methods |  The functions of the class (What it can do)
|Constructor|The function that gets executed when the instance is created |
| self | self - The respective instance |


# 1. Class & Instances
## Class Naming Convention: PascalCase
```py
class Computer: # Specify the class blueprint
   pass # Just a placeholder to fill in later

computer1 = Computer() # Creating the instance 
```

# 2. Attribute & Constructor
```py
class Computer: # Specify the class blueprint
    def __init__(self, model, year): # A method that will execute whenever the instance is instantiated
        self.model = model 
        self.year = year
        self.is_functional = True
        self.ram_use = 0
    computer1 = Computer("PC", 2020) # Creating the instance 
```
### BEHIND THE SCENE
    1. Create a variable "computer1" 
    2. When executing Computer("PC", 2020), it runs the __init__ function (constructor)
    3. Assign different keys & value to this computer1 (model, year, etc)
    4. computer1 is now a Computer object with model, year, etc
