from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models import MonitoredURL, HealthCheck
from app.schemas import (
    URLCreate,
    URLResponse,
    StatusResponse
)

router = APIRouter(
    prefix="/urls",
    tags=["URLs"]
)


@router.post(
    "/",
    response_model=URLResponse
)
def create_url(
    payload: URLCreate,
    db: Session = Depends(get_db)
):
    existing = (
        db.query(MonitoredURL)
        .filter(MonitoredURL.url == str(payload.url))
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="URL already exists"
        )

    url = MonitoredURL(
        url=str(payload.url)
    )

    db.add(url)
    db.commit()
    db.refresh(url)

    return url


@router.get(
    "/",
    response_model=list[URLResponse]
)
def get_urls(
    db: Session = Depends(get_db)
):
    return db.query(MonitoredURL).all()

@router.get(
    "/status",
    response_model=list[StatusResponse]
)
def get_status(
    db: Session = Depends(get_db)
):
    urls = db.query(MonitoredURL).all()

    result = []

    for url in urls:
        latest = (
            db.query(HealthCheck)
            .filter(
                HealthCheck.url_id == url.id
            )
            .order_by(
                HealthCheck.checked_at.desc()
            )
            .first()
        )

        result.append({
            "id": url.id,
            "url": url.url,
            "status_code":
                latest.status_code if latest else None,
            "response_time":
                latest.response_time if latest else None,
            "is_up":
                latest.is_up if latest else False,
            "checked_at":
                latest.checked_at if latest else None
        })

    return result

@router.get("/history/{url_id}")
def get_history(
    url_id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(HealthCheck)
        .filter(
            HealthCheck.url_id == url_id
        )
        .order_by(
            HealthCheck.checked_at.desc()
        )
        .limit(20)
        .all()
    )

@router.delete("/{url_id}")
def delete_url(
    url_id: int,
    db: Session = Depends(get_db)
):
    url = (
        db.query(MonitoredURL)
        .filter(
            MonitoredURL.id == url_id
        )
        .first()
    )

    if not url:
        raise HTTPException(
            status_code=404,
            detail="URL not found"
        )

    db.delete(url)
    db.commit()

    return {
        "message": "URL deleted"
    }