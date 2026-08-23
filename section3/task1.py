def apply_discount(price, percent):
    discount = price * percent / 100
    return price - discount


print(apply_discount(100, 10))
print(apply_discount(200, 20))
print(apply_discount(500, 15))