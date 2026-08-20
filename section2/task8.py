usernames = ["ali_92", "sara_x", "mo_dev", "lina.k"]
is_online = [True, False, True, True]

online_users = []

for idx, status in enumerate(is_online):
    if status:
        online_users.append(usernames[idx])

print("Active Users:", online_users)