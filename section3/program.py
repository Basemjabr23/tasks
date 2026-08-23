orders = [
    {"id": 1, "customer": "Ali", "items": ["shoes", "hat"], "total": 75.98, "status": "delivered"},
    {"id": 2, "customer": "Sara", "items": ["laptop"], "total": 899.99, "status": "shipped"},
    {"id": 3, "customer": "Mo", "items": ["mouse", "keyboard", "monitor"], "total": 220.00, "status": "pending"},
    {"id": 4, "customer": "Lina", "items": ["phone case"], "total": 15.99, "status": "delivered"},
]


def total_revenue(orders):
    total = 0

    for order in orders:
        total += order["total"]

    return total


def count_by_status(orders):
    status_count = {}

    for order in orders:
        status = order["status"]

        status_count[status] = status_count.get(status, 0) + 1

    return status_count


def highest_order(orders):
    highest = orders[0]

    for order in orders:
        if order["total"] > highest["total"]:
            highest = order

    return highest["customer"]


def unique_items(orders):
    items = set()

    for order in orders:
        for item in order["items"]:
            items.add(item)

    return items


print("Total revenue:", total_revenue(orders))
print("Orders by status:", count_by_status(orders))
print("Highest order customer:", highest_order(orders))
print("Unique items:", unique_items(orders))