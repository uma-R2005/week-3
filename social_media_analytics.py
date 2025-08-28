import logging
from collections import defaultdict

# ------------------ Logging Setup ------------------
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("SocialMediaAnalytics")

# ------------------ Sample Post Data ------------------
posts = [
    {"id": 1, "likes": 1200, "hashtags": ["#AI", "#Python"], "comments": 30},
    {"id": 2, "likes": 500, "hashtags": ["#Food"], "comments": 5},
    {"id": 3, "likes": 1500, "hashtags": ["#Python", "#Data"], "comments": 50},
    {"id": 4, "likes": 200, "hashtags": ["#Travel"], "comments": 2},
    {"id": 5, "likes": 3000, "hashtags": ["#AI", "#ML"], "comments": 100},
]

# ------------------ Comprehensions: Trending & Viral Posts ------------------
trending = [p for p in posts if p['likes'] > 1000]
logger.debug(f"All posts: {posts}")
logger.info(f"Trending posts (>1000 likes): {[p['id'] for p in trending]}")

viral = [p for p in posts if p['likes'] > 2000 or p['comments'] > 80]
logger.info(f"Viral posts (>2000 likes or >80 comments): {[p['id'] for p in viral]}")

# ------------------ Iterators: Group by Hashtags ------------------
hashtags_group = defaultdict(list)
for p in posts:
    for h in p['hashtags']:
        hashtags_group[h].append(p['id'])

logger.info("Posts grouped by hashtags:")
for h, ids in hashtags_group.items():
    logger.info(f"{h}: {ids}")

# ------------------ Warnings for Low Engagement ------------------
for p in posts:
    if p['likes'] < 300:
        logger.warning(f"Post ID {p['id']} has low engagement: {p['likes']} likes")

# ------------------ Summary ------------------
if not posts:
    logger.critical("No post data available!")
else:
    total_likes = sum(p['likes'] for p in posts)
    logger.info(f"Total posts: {len(posts)}, Total likes: {total_likes}, Trending: {len(trending)}, Viral: {len(viral)}")
