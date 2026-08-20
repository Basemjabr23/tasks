likes = [45, 230, 12, 987, 56, 1200, 3]


popular_posts = sum(1 for like in likes if like > 100)

print(f"Total popular posts (>100 likes): {popular_posts}")