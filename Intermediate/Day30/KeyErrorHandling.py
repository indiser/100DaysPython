facebook_posts=[
    {
        "Likes":21,
        "Comments":2
    },
    {
        "Likes":13
    },
    {
        "Likes":33,
        "Comments":8,
        "Shares":3
    },
    {
        "Comments":4,
        "Shares":2
    },
    {
        "Likes":100,
        "Comments":12,
        "Shares":1
    }
]

total_likes=0

for post in facebook_posts:
    try:
        total_likes+=post["Likes"]
    except KeyError:
        continue

print(total_likes)