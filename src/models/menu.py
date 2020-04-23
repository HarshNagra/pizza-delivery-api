PIZZAS = [
    {"name": "pepperoni", "size": "l", "price": 10.00, "category": "pizza"},
    {"name": "pepperoni", "size": "m", "price": 7.00, "category": "pizza"},
    {"name": "pepperoni", "size": "s", "price": 7.00, "category": "pizza"},
    {"name": "margherita", "size": "l", "price": 10.00, "category": "pizza"},
    {"name": "margherita", "size": "m", "price": 7.00, "category": "pizza"},
    {"name": "margherita", "size": "s", "price": 7.00, "category": "pizza"},
    {"name": "vegetarian", "size": "l", "price": 10.00, "category": "pizza"},
    {"name": "vegetarian", "size": "m", "price": 7.00, "category": "pizza"},
    {"name": "vegetarian", "size": "s", "price": 7.00, "category": "pizza"},
    {"name": "neapolitan", "size": "l", "price": 10.00, "category": "pizza"},
    {"name": "neapolitan", "size": "m", "price": 7.00, "category": "pizza"},
    {"name": "neapolitan", "size": "s", "price": 7.00, "category": "pizza"},
]

TOPPINGS = [
    {"name": "olives", "size": "s", "price": 0.50, "category": "topping"},
    {"name": "tomatoes", "size": "s", "price": 0.50, "category": "topping"},
    {"name": "mushrooms", "size": "s", "price": 0.50, "category": "topping"},
    {"name": "jalapenos", "size": "s", "price": 0.50, "category": "topping"},
    {"name": "chicken", "size": "s", "price": 0.50, "category": "topping"},
    {"name": "beef", "size": "s", "price": 0.50, "category": "topping"},
    {"name": "pepperoni", "size": "s", "price": 0.50, "category": "topping"},
]

DRINKS = [
    {"name": "coke", "size": "m", "price": 3.00, "category": "drink"},
    {"name": "diet coke", "size": "m", "price": 3.00, "category": "drink"},
    {"name": "coke zero", "size": "m", "price": 3.50, "category": "drink"},
    {"name": "pepsi", "size": "m", "price": 3.50, "category": "drink"},
    {"name": "diet pepsi", "size": "m", "price": 3.50, "category": "drink"},
    {"name": "dr. pepper", "size": "m", "price": 3.50, "category": "drink"},
]

MENU = [
    *PIZZAS,
    *TOPPINGS,
    *DRINKS,
]
