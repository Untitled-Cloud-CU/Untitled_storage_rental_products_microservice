"""
Main application entry point
FastAPI application for Storage Rental Service
Storage Rental Platform (like Airbnb for storage)
"""
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from app.db.config import get_db, engine     # <── CORRECT imports
from app.routers import storage_units, rentals

# Create FastAPI application
app = FastAPI(
    title="Storage Rental - Storage Units & Rentals Service API",
    description="""
    Microservice for managing storage unit listings and rental bookings in the Storage Rental platform.
    """,
    version="1.0.0",
    contact={"name": "Wali + Aashish"},
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(storage_units.router)
app.include_router(rentals.router)

# Root
@app.get("/", tags=["root"])
async def root():
    return {
        "service": "Storage Rental Service",
        "status": "running",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "storage_units": "/api/v1/storage-units",
            "rentals": "/api/v1/rentals"
        },
    }

# Health check that tests DB connection
@app.get("/health", tags=["health"])
async def health_check():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "healthy", "db": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "db_error": str(e)}