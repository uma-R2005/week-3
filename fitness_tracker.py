import logging
from collections import defaultdict

# ------------------ Logging Setup ------------------
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("FitnessTracker")

# ------------------ Sample Fitness Data ------------------
users = [
    {"name": "Alice", "steps": 12000, "heart_rate": 75},
    {"name": "Bob", "steps": 4000, "heart_rate": 110},
    {"name": "Charlie", "steps": 8000, "heart_rate": 65},
    {"name": "David", "steps": 3000, "heart_rate": 130},
    {"name": "Eve", "steps": 15000, "heart_rate": 70}
]

# ------------------ Comprehensions: Active & Low Activity ------------------
active_users = [u for u in users if u['steps'] >= 10000]
low_activity = [u for u in users if u['steps'] < 5000]
logger.debug(f"All users: {users}")
logger.info(f"Active users (steps>=10000): {[u['name'] for u in active_users]}")
logger.info(f"Low activity users (steps<5000): {[u['name'] for u in low_activity]}")

# ------------------ Iterators: Group by Heart Rate Category ------------------
hr_group = defaultdict(list)
for u in users:
    category = "High" if u['heart_rate'] > 100 else "Normal"
    hr_group[category].append(u['name'])
logger.info("Users grouped by heart rate category:")
for cat, names in hr_group.items():
    logger.info(f"{cat}: {names}")

# ------------------ Warnings: Unhealthy Heart Rate ------------------
for u in users:
    if u['heart_rate'] > 120:
        logger.warning(f"High heart rate detected: {u['name']} ({u['heart_rate']})")

# ------------------ Summary ------------------
if not users:
    logger.critical("No user data available!")
else:
    avg_steps = sum(u['steps'] for u in users)/len(users)
    logger.info(f"Total users: {len(users)}, Average steps: {avg_steps:.2f}")
