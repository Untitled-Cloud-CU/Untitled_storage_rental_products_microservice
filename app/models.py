"""
Data models for Storage Rental Service
Defines the structure of Storage Units and Rental resources for storage rental platform
"""
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum


class StorageUnitSize(str, Enum):
    """Storage unit size categories"""
    small = "small"           # 5x5, 5x10
    medium = "medium"         # 10x10, 10x15
    large = "large"           # 10x20, 10x30
    extra_large = "extra_large"  # 20x20+


class StorageUnitType(str, Enum):
    """Storage unit type categories"""
    indoor = "indoor"
    outdoor = "outdoor"
    climate_controlled = "climate_controlled"
    vehicle = "vehicle"
    warehouse = "warehouse"


class RentalStatus(str, Enum):
    """Rental status"""
    pending = "pending"
    confirmed = "confirmed"
    active = "active"
    completed = "completed"
    cancelled = "cancelled"


class Money(BaseModel):
    """Money representation with currency"""
    amount: float = Field(..., ge=0, description="Amount in the specified currency")
    currency: str = Field(default="USD", description="Currency code (e.g., USD, EUR)")


class StorageUnitBase(BaseModel):
    """Base storage unit model"""
    name: str = Field(..., description="Storage unit name/title")
    description: Optional[str] = Field(None, description="Detailed description")
    size: StorageUnitSize = Field(..., description="Size category")
    unit_type: StorageUnitType = Field(..., description="Type of storage unit")
    dimensions: Optional[str] = Field(None, description="Dimensions (e.g., '10x10x8')")
    location_id: str = Field(..., description="Reference to addresses.id in location service")
    owner_user_id: int = Field(..., description="Reference to users.user_id in users service")
    price_per_month: Money = Field(..., description="Monthly rental price")
    available: bool = Field(default=True, description="Availability status")
    features: Optional[List[str]] = Field(default=[], description="Features (e.g., 24/7 access, security)")


class StorageUnitCreate(StorageUnitBase):
    """Model for creating a storage unit"""
    pass


class StorageUnitUpdate(BaseModel):
    """Model for updating storage unit"""
    name: Optional[str] = None
    description: Optional[str] = None
    size: Optional[StorageUnitSize] = None
    unit_type: Optional[StorageUnitType] = None
    dimensions: Optional[str] = None
    price_per_month: Optional[Money] = None
    available: Optional[bool] = None
    features: Optional[List[str]] = None


class StorageUnit(StorageUnitBase):
    """Complete storage unit model"""
    id: str = Field(..., description="Unique storage unit ID")
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class RentalBase(BaseModel):
    """Base rental model"""
    storage_unit_id: str = Field(..., description="ID of the storage unit being rented")
    renter_user_id: int = Field(..., description="Reference to users.user_id (renter)")
    start_date: datetime = Field(..., description="Rental start date")
    end_date: Optional[datetime] = Field(None, description="Rental end date (None for ongoing)")
    monthly_rate: Money = Field(..., description="Agreed monthly rate")
    status: RentalStatus = Field(default=RentalStatus.pending, description="Current rental status")
    notes: Optional[str] = Field(None, description="Additional notes")


class RentalCreate(RentalBase):
    """Model for creating a rental"""
    pass


class RentalUpdate(BaseModel):
    """Model for updating rental"""
    end_date: Optional[datetime] = None
    status: Optional[RentalStatus] = None
    notes: Optional[str] = None


class Rental(RentalBase):
    """Complete rental model"""
    id: str = Field(..., description="Unique rental ID")
    owner_user_id: int = Field(..., description="Reference to users.user_id (owner)")
    total_paid: Optional[Money] = Field(None, description="Total amount paid so far")
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class RentalWithDetails(Rental):
    """Rental with embedded storage unit details"""
    storage_unit: StorageUnit


class StorageUnitWithRentals(StorageUnit):
    """Storage unit with rental history"""
    active_rental: Optional[Rental] = None
    rental_history: List[Rental] = []