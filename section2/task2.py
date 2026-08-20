followers_list = ["ali_92", "sara_x", "mo_dev", "lina.k"]

user = input("Enter username to check: ")

if user in followers_list:
    print(f"{user} is already following you.")
else:
    followers_list.append(user)
    print(f"Added {user} to your followers!")