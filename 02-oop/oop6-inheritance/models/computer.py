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

    def display_info(self):
        print(f"Model: {self.model} ({self.year})")
        print(f"Price: {self.price}")
        print(f"RAM usage: {self.ram_use}")

    # Custom methods
    def turn_on(self):
        self.ram_use = 0.5
        print(f"{self.model} is turned on. Using {self.ram_use} RAM")
        return self # optional - to chain the method

    def open_tabs(self, tabs = 1):
        self.ram_use +=  tabs
        print(f"{self.model} is opening another {tabs} tabs.")
        print(f"RAM usage: {self.ram_use} RAM")
        return self # optional - to chain the method

