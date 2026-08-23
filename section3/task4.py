def cart_total(*prices, discount_percent=0):
    total = sum(prices)
    discount = total * discount_percent / 100
    return total - discount


print(cart_total(100, 50, 25))
print(cart_total(100, 50, 25, discount_percent=10))