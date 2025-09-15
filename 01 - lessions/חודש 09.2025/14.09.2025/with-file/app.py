from datetime import datetime
import os

LOG_DIR = "./logs"
LOG_FILE = os.path.join(LOG_DIR, "file.txt")

# Ensure the logs directory exists
os.makedirs(LOG_DIR, exist_ok=True)

with open(LOG_FILE, "a") as file:
    now = datetime.now()
    file.write(f"now : {now}\n")

with open(LOG_FILE, "r") as file:
    content = file.read()
    print(f"content : {content}")
