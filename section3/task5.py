followers = {
    "Ali": 1000,
    "Sara": 2500,
    "Mo": 500
}


def get_followers(username, data):
    return data.get(username, "User not found")


print(get_followers("Ali", followers))
print(get_followers("Sara", followers))
print(get_followers("Ahmed", followers))