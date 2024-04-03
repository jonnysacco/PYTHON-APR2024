import utilities
from models.product import Product

# Test 1
product_list1 = Product.get_all()
utilities.show_list(product_list1)

# Test 2
product_list2 = Product.get_all_with_seller()
utilities.show_list(product_list2)