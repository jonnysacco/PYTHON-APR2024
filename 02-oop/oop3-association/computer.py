class Developer:
    def __init__(self, username, git_account):
        self.username = username
        self.git_account = git_account
        self.languages = ["html", "css", "python", "js"]
        self.computer = Computer("Macbook pro", 2024)

    def display_status(self):
        print("Username:", self.username)
        print("Git account:", self.git_account)
        print("Languages:", self.languages)
        print("===== owned computer ======")
        self.computer.display_info()

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


computer1 = Computer("Macbook Pro", 2022, 1200) # Create the instance
computer2 = Computer("Surface Pro", 2023)
computer3 = Computer("PC", 2020)


computer1.turn_on()
computer1.open_tabs()
computer1.open_tabs(10)

computer1.turn_on().open_tabs().open_tabs(10)


dev1 = Developer("pepper", "peppergit")
print(dev1.computer.model)
dev1.display_status()

"""
    Class: a blueprint of the object
    Instance: the object that is created baesd on the class
    Constructor: the function that gets executed when the instance is created
    Attributes: the properties of the class (what it has)
    Method: the function within the class (What it does)
    self : The respective instance
"""