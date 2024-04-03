import utilities
from models.product import Product

results = [ # The response can have more key-value pair in each dictioary
    {"id": 1, "title": "soup dumpling", "price": 3.49},
    {"id": 2, "title": "boba", "price": 5.25},
    {"id": 3, "title": "montior", "price": 400},
    {"id": 4, "title": "ice cream", "price": 4.49},
    {"id": 5, "title": "folder", "price": 1.25}
]

product_details = {"id": 1, "title": "soup dumpling", "price": 3.49}
product1 = Product(product_details)
print(product1)

product_list = []
# 1. loop through the results (the list of dictionaries)
for row in results:
    # 2. when going through each item, create the product instance
    this_product = Product(row)
    # 3. push it to the list
    product_list.append(this_product)

print(product_list)