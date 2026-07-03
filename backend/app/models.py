from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class MonitoredURL(Base):
    __tablename__ = "monitored_urls"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    health_checks = relationship(
        "HealthCheck",
        back_populates="monitored_url",
        cascade="all, delete-orphan"
    )


class HealthCheck(Base):
    __tablename__ = "health_checks"

    id = Column(Integer, primary_key=True, index=True)

    url_id = Column(
        Integer,
        ForeignKey("monitored_urls.id"),
        nullable=False
    )

    status_code = Column(Integer)
    response_time = Column(Float)
    checked_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    monitored_url = relationship(
        "MonitoredURL",
        back_populates="health_checks"
    )