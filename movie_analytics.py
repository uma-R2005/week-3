import logging
from collections import defaultdict

# ------------------ Logging Setup ------------------
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("MovieAnalytics")

# ------------------ Sample Movie Data ------------------
movies = [
    {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8, "views": 120000},
    {"title": "Titanic", "genre": "Romance", "rating": 7.8, "views": 90000},
    {"title": "Avengers", "genre": "Action", "rating": 8.0, "views": 150000},
    {"title": "Joker", "genre": "Drama", "rating": 9.0, "views": 80000},
    {"title": "Frozen", "genre": "Animation", "rating": 7.5, "views": 50000}
]

# ------------------ Comprehensions: Top-rated & Popular ------------------
top_rated = [m for m in movies if m['rating'] >= 8.5]
popular = [m for m in movies if m['views'] >= 100000]
logger.debug(f"All movies: {movies}")
logger.info(f"Top-rated movies (>=8.5): {[m['title'] for m in top_rated]}")
logger.info(f"Popular movies (views>=100000): {[m['title'] for m in popular]}")

# ------------------ Iterators: Group by Genre ------------------
genre_group = defaultdict(list)
for m in movies:
    genre_group[m['genre']].append(m['title'])
logger.info("Movies grouped by genre:")
for g, titles in genre_group.items():
    logger.info(f"{g}: {titles}")

# ------------------ Warnings: Low-rated Movies ------------------
for m in movies:
    if m['rating'] < 7.8:
        logger.warning(f"Low-rated movie detected: {m['title']} ({m['rating']})")

# ------------------ Summary ------------------
if not movies:
    logger.critical("No movie data available!")
else:
    avg_rating = sum(m['rating'] for m in movies)/len(movies)
    total_views = sum(m['views'] for m in movies)
    logger.info(f"Total movies: {len(movies)}, Average rating: {avg_rating:.2f}, Total views: {total_views}")
