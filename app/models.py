from pydantic import BaseModel
from typing import List, Optional

class Money(BaseModel):
    amount: float
    currency: str = "USD"

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Money
    sku: Optional[str] = None
    stock: int = 0

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: str

class OrderItem(BaseModel):
    product_id: str
    quantity: int
    unit_price: Money

class OrderBase(BaseModel):
    user_id: str
    items: List[OrderItem]
    status: str = "pending"

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: str