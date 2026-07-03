import time
import requests
from datetime import datetime

from app.config import REQUEST_TIMEOUT
from app.database import SessionLocal
from app.models import MonitoredURL, HealthCheck

def check_all_urls():
    db = SessionLocal()

    try:
        urls = db.query(MonitoredURL).all()

        for monitored_url in urls:
            start = time.perf_counter()

            status_code = None
            response_time = None
            is_up = False

            try:
                response = requests.get(
                    monitored_url.url,
                    timeout=REQUEST_TIMEOUT
                )

                end = time.perf_counter()

                status_code = response.status_code
                is_up = response.ok

                response_time = round(
                    (end - start) * 1000,
                    2
                )

            except Exception:
                pass

            health_check = HealthCheck(
                url_id=monitored_url.id,
                status_code=status_code,
                response_time=response_time,
                is_up=is_up,
                checked_at=datetime.utcnow()
         )

            db.add(health_check)

        db.commit()

    finally:
        db.close()