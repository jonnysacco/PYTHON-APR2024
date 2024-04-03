import query_response
from models.user import User

class Product:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.price = data["price"]
        self.seller = None # seller is a User object
        
    @classmethod
    def get_all(cls): # return a list of product based on the results1
        results = query_response.results1
        # results is the list of products (without seller info)
        product_list = []
        # 1. loop through the results (the list of dictionaries)
        for row in results:
            # 2. when going through each item, create the product instance
            this_product = cls(row)
            # 3. push it to the list
            product_list.append(this_product)
        return product_list

    @classmethod
    def get_all_with_seller(cls):
        results = query_response.results2
        # results is the list of products (with seller info) 
        product_list = []
        for row in results:
            this_product = cls(row) # create the Product instance 
            # 1. create the custom dictionary to create User instance
            seller_dict = {
                "id" : row["seller.id"],
                "username": row["username"],
                "email" : row["email"]
            }
            # 2. Create a User instance from the custom dict
            seller_from_row = User(seller_dict)
            
            # 3. Assign this newly created user to this_product.seller
            this_product.seller = seller_from_row
            
            # 4. push the product in
            product_list.append(this_product)
        return product_list

        """
        seller_dict
        {
            "id" : 20,
            "username": "Heidi",
            "email" : "heidi@anything.com"
        }
        """
    
