results1 = [ # The response can have more key-value pair in each dictioary
    {"id": 1, "title": "soup dumpling", "price": 3.49},
    {"id": 2, "title": "boba", "price": 5.25},
    {"id": 3, "title": "montior", "price": 400},
    {"id": 4, "title": "ice cream", "price": 4.49},
    {"id": 5, "title": "folder", "price": 1.25}
]

results2 = [ # The response can have more key-value pair in each dictioary
    {"id": 1,   # product: id
     "title": "soup dumpling",  # product: title
     "price": 3.49,  # product: price
     "seller.id": 20, # User: id
     "username": "Heidi", # User: username
     "email": "heidi@anything.com"}, # User: email
    
    {"id": 2, "title": "boba", "price": 5.25, "seller.id": 23, "username": "Pepper", "email": "pepper@cat.com"},
    {"id": 3, "title": "montior", "price": 400, "seller.id": 20, "username": "Heidi", "email": "heidi@anything.com"},
    {"id": 4, "title": "ice cream", "price": 4.49, "seller.id": 20, "username": "shawn", "email": "shawn@jokes.com"},
    {"id": 5, "title": "folder", "price": 1.25, "seller.id": 20, "username": "shawn", "email": "shawn@jokes.com"}
]