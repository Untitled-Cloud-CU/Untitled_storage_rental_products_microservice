"""
Storage Units endpoints
Handles all storage unit listing and management operations
"""
from fastapi import APIRouter, HTTPException, status, Query
from typing import List, Optional
from ..models import (
    StorageUnit,
    StorageUnitCreate,
    StorageUnitUpdate,
    StorageUnitSize,
    StorageUnitType,
    StorageUnitWithRentals
)

router = APIRouter(prefix="/api/v1/storage-units", tags=["storage-units"])


@router.get("/", status_code=status.HTTP_501_NOT_IMPLEMENTED)
def list_storage_units(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=100, description="Maximum number of records to return"),
    size: Optional[StorageUnitSize] = Query(None, description="Filter by size"),
    unit_type: Optional[StorageUnitType] = Query(None, description="Filter by type"),
    available: Optional[bool] = Query(None, description="Filter by availability"),
    location_id: Optional[str] = Query(None, description="Filter by location")
):
    """
    Retrieve list of storage units with optional filters
    """
    return {"detail": "Not implemented"}


@router.post("/", status_code=status.HTTP_501_NOT_IMPLEMENTED)
def create_storage_unit(unit: StorageUnitCreate):
    """
    Create a new storage unit listing
    """
    return {"detail": "Not implemented"}


@router.get("/{unit_id}", status_code=status.HTTP_501_NOT_IMPLEMENTED)
def get_storage_unit(unit_id: str):
    """
    Retrieve a specific storage unit by ID
    """
    return {"detail": "Not implemented"}


@router.put("/{unit_id}", status_code=status.HTTP_501_NOT_IMPLEMENTED)
def update_storage_unit(unit_id: str, unit: StorageUnitUpdate):
    """
    Update an existing storage unit
    """
    return {"detail": "Not implemented"}


@router.delete("/{unit_id}", status_code=status.HTTP_501_NOT_IMPLEMENTED)
def delete_storage_unit(unit_id: str):
    """
    Delete a storage unit listing
    """
    return {"detail": "Not implemented"}


@router.get("/{unit_id}/rentals", status_code=status.HTTP_501_NOT_IMPLEMENTED)
def get_storage_unit_with_rentals(unit_id: str):
    """
    Get storage unit with its rental history
    """
    return {"detail": "Not implemented"}


@router.get("/owner/{owner_user_id}", status_code=status.HTTP_501_NOT_IMPLEMENTED)
def get_storage_units_by_owner(owner_user_id: int):
    """
    Get all storage units owned by a specific user (owner_user_id references users.user_id)
    """
    return {"detail": "Not implemented"}


@router.get("/location/{location_id}", status_code=status.HTTP_501_NOT_IMPLEMENTED)
def get_storage_units_by_location(location_id: str):
    """
    Get all storage units at a specific location
    """
    return {"detail": "Not implemented"}