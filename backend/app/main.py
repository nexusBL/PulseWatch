from fastapi import FastAPI

from app.database import Base, engine

app = FastAPI(
    title="PulseWatch API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)


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