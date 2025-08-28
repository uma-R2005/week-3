import logging
from collections import defaultdict

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("WeatherAnalyzer")

temps = [30, 32, 28, 35, 36, 31, 29, 33, 34, 40, 27, 38]

# Comprehensions for hot and cold days
hot_days = [t for t in temps if t >= 34]
cold_days = [t for t in temps if t < 34]
logger.debug(f"All temperatures: {temps}")
logger.info(f"Hot days (>=34°C): {hot_days}")
logger.info(f"Cold days (<34°C): {cold_days}")

# Extreme temperatures
for t in temps:
    if t >= 38: logger.warning(f"Extreme hot: {t}°C")
    elif t <= 28: logger.warning(f"Extreme cold: {t}°C")

# Group by 5-degree ranges
groups = defaultdict(list)
for t in temps: groups[f"{t//5*5}-{t//5*5+4}"].append(t)
logger.info("Temperatures grouped by 5-degree ranges:")
for k,v in groups.items(): logger.info(f"{k}°C: {v}")

# Summary
if not temps: logger.critical("No temperature data available!")
else:
    avg=sum(temps)/len(temps)
    logger.info(f"Average Temp: {avg:.2f}°C | Total: {len(temps)}, Hot: {len(hot_days)}, Cold: {len(cold_days)}")
