from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routers.urls import router as urls_router
from contextlib import asynccontextmanager
from app.scheduler import start_scheduler
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    start_scheduler()
    yield


app = FastAPI(
    title="PulseWatch API",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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