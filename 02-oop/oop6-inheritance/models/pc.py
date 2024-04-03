from models.computer import Computer

"""
    PC is a subclass of Computer -- PC inherits from Computer
    What gets inheritted?
    - All the attributes from Computer (model, year, ram_use, price)
    - All the methods from Computer

    What if I need to call the contructor from superclass?
    - super() to specify the superclass

"""


class PC(Computer):
    def __init__(self):
        super().__init__("Gaming PC", 2023)
        self.case_material = "Tempered glass"
        self.case_lighting = False
        
    def turn_on(self):
        self.ram_use = 0.3
        print(f"{self.model} is turned on. Using {self.ram_use} RAM")
        return self # optional - to chain the method
    
    def display_info(self):
        super().display_info() # Calling the superclass method
        print("Case Material:", self.case_material)
