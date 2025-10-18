"""
Main application entry point
FastAPI application for Storage Rental Service
Storage Rental Platform (like Airbnb for storage)
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import storage_units, rentals

# Create FastAPI application
app = FastAPI(
    title="Storage Rental - Storage Units & Rentals Service API",
    description="""
    Microservice for managing storage unit listings and rental bookings in the Storage Rental platform.

    Features:
    - Storage unit listing management (like property listings on Airbnb)
    - Rental booking and management
    - Integration with Users service (owners and renters)
    - Integration with Locations service (storage unit addresses)
    - CRUD operations for storage units and rentals
    - Swagger/OpenAPI-first API design

    This is a Sprint 1 implementation using Swagger-first approach.
    All endpoints return "NOT IMPLEMENTED" responses as placeholders.
    """,
    version="1.0.0",
    contact={
        "name": "Wali + Aashish",
    },
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(storage_units.router)
app.include_router(rentals.router)


@app.get("/", tags=["root"])
async def root():
    """
    Root endpoint - Service information
    """
    return {
        "service": "Storage Rental Service",
        "description": "Storage Rental Platform (like Airbnb for storage)",
        "version": "1.0.0",
        "status": "running",
        "documentation": {
            "swagger": "/docs",
            "redoc": "/redoc",
            "openapi_spec": "/docs/openapi.yaml",
            "openapi_json": "/openapi.json"
        },
        "endpoints": {
            "storage_units": "/api/v1/storage-units",
            "rentals": "/api/v1/rentals"
        }
    }


@app.get("/health", tags=["health"])
async def health_check():
    """
    Health check endpoint
    Returns service health status
    """
    return {
        "status": "healthy",
        "service": "storage-rental-service",
        "version": "1.0.0"
    }