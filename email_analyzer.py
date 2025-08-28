import logging
import re
from collections import defaultdict

# ------------------ Setup Logging ------------------
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("EmailAnalyzer")

# ------------------ Sample Emails ------------------
emails = [
    "uma@gmail.com", "info@yahoo.com", "hr@company.com", "test@gmail.com",
    "admin@openai.com", "user123@gmail.com", "contact@company.com",
    "fakeemail@@gmail.com", "hello.world@yahoo.com"
]

# ------------------ Validation ------------------
is_valid = lambda e: re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', e)
valid_emails = [e for e in emails if is_valid(e)]
logger.info(f"Valid Emails: {valid_emails}")

# ------------------ Group by Domain ------------------
domains = defaultdict(list)
for e in valid_emails:
    domains[e.split('@')[1]].append(e)

for domain, group in domains.items():
    logger.info(f"{domain}: {group}")

# ------------------ Gmail Users ------------------
gmail_users = [e for e in valid_emails if e.endswith("@gmail.com")]
logger.info(f"Gmail Users: {gmail_users}")

# ------------------ Summary ------------------
logger.info(f"Total: {len(emails)}, Valid: {len(valid_emails)}, Gmail: {len(gmail_users)}")
