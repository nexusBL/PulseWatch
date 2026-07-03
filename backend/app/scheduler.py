from apscheduler.schedulers.background import BackgroundScheduler

from app.config import PING_INTERVAL_SECONDS
from app.services.monitor import check_all_urls

scheduler = BackgroundScheduler()


def start_scheduler():
    scheduler.add_job(
        check_all_urls,
        "interval",
        seconds=PING_INTERVAL_SECONDS
    )

    scheduler.start()