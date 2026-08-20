while True:
    user_input = input("Enter quantity: ")
    
    if user_input.isnumeric():
        quantity = int(user_input)
        print(f"Recorded quantity: {quantity}")
        break
    else:
        print("Error: Input must be a valid number.")