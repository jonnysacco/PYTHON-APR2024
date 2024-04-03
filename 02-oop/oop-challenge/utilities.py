def show_list(list):
    for row in list:
        print(f"ID: {row.id} | Title: {row.title} | Price: {row.price}")
        if row.seller:
            print(f"Seller ID: {row.seller.id} | username: {row.seller.username} | Email: {row.seller.email}")
