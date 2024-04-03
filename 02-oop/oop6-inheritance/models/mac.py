from models.computer import Computer

class Mac(Computer):
    def __init__(self, style, year):
        super().__init__(f"Macbook {style}", year)
