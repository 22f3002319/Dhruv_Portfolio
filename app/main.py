"""
FastAPI application for backend engineer portfolio.
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers import pages

app = FastAPI(
    title="Dhruv - Backend Engineer Portfolio",
    description="Portfolio showcasing backend engineering expertise in trading systems",
    version="1.0.0"
)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routers
app.include_router(pages.router)

