from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_URL = f"sqlite:///{BASE_DIR}/pulsewatch.db"

PING_INTERVAL_SECONDS = 10
REQUEST_TIMEOUT = 10