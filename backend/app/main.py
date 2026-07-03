from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routers.urls import router as urls_router

app = FastAPI(
    title="PulseWatch API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(urls_router)

@app.get("/")
def root():
    return {
        "message": "PulseWatch API Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }