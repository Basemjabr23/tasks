status = input("Check order status: ").lower().strip()

if status == "pending":
    print("Status: Order is under processing.")
elif status == "shipped":
    print("Status: Order is on the way.")
elif status == "delivered":
    print("Status: Order delivered successfully.")
elif status == "cancelled" or status == "canceled":
    print("Status: Order was cancelled.")
else:
    print("Status: Unrecognized status.")