class Product:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.price = data["price"]
        
    def __str__(self):
        return f"<Product {self.id} {self.title} {self.price}>"