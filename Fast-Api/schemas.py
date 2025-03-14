from pydantic import BaseModel
from datetime import datetime

class ProductCreate(BaseModel):
    name: str
    category: str
    description: str
    product_image: str
    sku: str
    unit_of_measure: str
    lead_time: int

class ProductUpdate(ProductCreate):
    pass

class ProductResponse(ProductCreate):
    id: int
    created_date: datetime
    updated_date: datetime