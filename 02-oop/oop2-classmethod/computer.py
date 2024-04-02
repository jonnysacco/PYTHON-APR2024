class Computer:
    # declare class attributes
    name = "Computer Center"
    all_computers = []
    total_cost = 0

    def __init__(self, model, year, price = 800): # Constructor
        self.model = model
        self.year = year
        self.is_functional = True
        self.ram_use = 0
        self.price = price
        Computer.all_computers.append(self)
        Computer.total_cost += price

    def __str__(self):
    # A human-readable representation of the instance.
        return f"<Computer: {self.model} ({self.year}) RAM usage: {self.ram_use} ${self.price} >"

    def turn_on(self):
        self.ram_use = 0.5
        print(f"{self.model} is turned on. Using {self.ram_use} RAM")
        return self

    def open_tabs(self, tabs = 1):
        if Computer.enough_ram(tabs + self.ram_use):
            self.ram_use +=  tabs
            print(f"{self.model} is opening another {tabs} tabs.")
            print(f"RAM usage: {self.ram_use} RAM")
        else:
            print("You don't have enough RAM to open all the tabs")
        return self

    @classmethod
    def print_all_computers(cls):
        for each_computer in cls.all_computers:
            print(each_computer)
    
    # Check if the RAM is enough
    @staticmethod
    def enough_ram(expected_ram_use): # if the ram usage will be over 50 after opening tabs, return False
        if expected_ram_use > 50:
            return False
        else:
            return True
    

computer1 = Computer("Macbook Pro", 2022, 1200) # Create the instance
computer2 = Computer("Surface Pro", 2023)
computer3 = Computer("PC", 2020)

print(computer1.total_cost)

Computer.print_all_computers()

computer1.turn_on()
computer1.open_tabs(30)
computer1.open_tabs(40)
