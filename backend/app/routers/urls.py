from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models import MonitoredURL
from app.schemas import URLCreate, URLResponse

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