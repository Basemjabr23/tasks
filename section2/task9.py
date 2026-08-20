raw_orders = ["4", "two", "0", "-1", "10", ""]
valid_orders = []

for item in raw_orders:
    if item.isdigit():
        count = int(item)
        if count > 0:
            valid_orders.append(count)

total_quantity = sum(valid_orders)
total_cost = total_quantity * 20

print(f"Valid Order Quantities: {valid_orders}")
print(f"Total Quantity: {total_quantity}")
print(f"Total Cost: ${total_cost}")