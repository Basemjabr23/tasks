product = {
    "name": "Laptop",
    "price": 1000,
    "quantity": 2
}


def total_cost(product):
    return product["price"] * product["quantity"]


print(total_cost(product))