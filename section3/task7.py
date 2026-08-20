cart = [15.99, 42.50, 9.75, 60.00]

subtotal = sum(cart)
shipping_fee = 0.0 if subtotal >= 100 else 5.99
final_amount = subtotal + shipping_fee

print(f"Cart Subtotal: ${subtotal:.2f}")
print(f"Shipping Fee: ${shipping_fee:.2f}")
print(f"Grand Total: ${final_amount:.2f}")