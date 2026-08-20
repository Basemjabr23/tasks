post_likes = [1200, 45, 980, 15, 3400, 220, 0, 87, 5600, 12]

if not post_likes:
    print("No posts found.")
else:
    total = sum(post_likes)
    avg = total / len(post_likes)
    
    print(f"Total Likes: {total}")
    print(f"Average Likes: {avg:.1f}")
    
    for likes in post_likes:
        if likes >= 1000:
            category = "Viral"
        elif likes >= 100:
            category = "Popular"
        else:
            category = "Normal"
        print(f"Post with {likes} likes is {category}")
        
    print("Top Post Likes:", max(post_likes))