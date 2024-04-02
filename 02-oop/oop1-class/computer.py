# 1. Class & Instance
# Class Naming convention : PascalCase
class Computer:
    def __init__(self, model, year, price = 800): # Constructor
        self.model = model
        self.year = year
        self.is_functional = True
        self.ram_use = 0
        self.price = price

    def __str__(self):
    # A human-readable representation of the instance.
        return f"<Computer: {self.model} ({self.year}) RAM usage: {self.ram_use} ${self.price} >"

    def turn_on(self):
        self.ram_use = 0.5
        print(f"{self.model} is turned on. Using {self.ram_use} RAM")

    def open_tabs(self, tabs = 1):
        self.ram_use +=  tabs
        print(f"{self.model} is opening another {tabs} tabs.")
        print(f"RAM usage: {self.ram_use} RAM")



    

computer1 = Computer("Macbook Pro", 2022, 1200) # Create the instance
computer2 = Computer("Surface Pro", 2023)
computer3 = Computer("PC", 2020)



print(computer1) 
print(computer2) 
print(computer3) 

computer1.turn_on()
computer1.open_tabs()
computer1.open_tabs(10)
print(computer1)

"""
    Class: a blueprint of the object
    Instance: the object that is created baesd on the class
    Constructor: the function that gets executed when the instance is created
    Attributes: the properties of the class (what it has)
    Method: the function within the class (What it does)
    self : The respective instance
"""