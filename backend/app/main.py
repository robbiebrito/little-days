
from fastapi import FastAPI
from app.core.config import settings
from app.routers import book


app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION
)


app.include_router(book.router)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "application": settings.APP_NAME
    }
