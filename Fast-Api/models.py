from database import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    category = Column(Enum("finished", "semi-finished", "raw"), nullable=False)
    description = Column(String(250))
    product_image = Column(String(250))
    sku = Column(String(100), unique=True)
    unit_of_measure = Column(Enum("mtr", "mm", "ltr", "ml", "cm", "mg", "gm", "unit", "pack"), nullable=False)
    lead_time = Column(Integer)
    created_date = Column(TIMESTAMP, default=datetime.utcnow)
    updated_date = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)  