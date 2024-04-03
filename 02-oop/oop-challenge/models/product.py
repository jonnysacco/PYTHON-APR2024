import query_response
from models.user import User

class Product:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.price = data["price"]
        self.seller = None # seller is a User object
        
    @classmethod
    def get_all(cls):
        results = query_response.results1
        # results is the list of products (without seller info)
        # YOUR CODE HERE       

    @classmethod
    def get_all_with_seller(cls):
        results = query_response.results2
        # results is the list of products (with seller info) 
        # YOUR CODE HERE
    
