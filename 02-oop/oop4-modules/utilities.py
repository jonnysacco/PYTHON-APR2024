import random

model_list = ["Macbook Air", "Surface Pro", "Dell Chromebook", "Lenovo Ideapad", "Acer VivoBook"]

def random_model():
    return random.choice(model_list)

def random_year():
    return random.randint(2019, 2024)