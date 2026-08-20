following = ["tech_news", "daily_memes", "cooking101", "travel_diaries"]

target = input("Account to unfollow: ")

if target in following:
    index = following.index(target)
    following.pop(index)
    print(f"Unfollowed '{target}'. Current list: {following}")
else:
    print(f"'{target}' is not present in your following list.")