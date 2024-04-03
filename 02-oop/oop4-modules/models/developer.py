# import computer file from models folder
from models import computer  # computer.Computer()

# import Computer class from models.computer file
from models.computer import Computer 

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