from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Product
from schemas import ProductCreate, ProductUpdate, ProductResponse
from typing import List

product_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@product_router.get("/product/list", response_model=List[ProductResponse])
def list_products(db: Session = Depends(get_db), page: int = 1, per_page: int = 10):
    products = db.query(Product).offset((page - 1) * per_page).limit(per_page).all()
    return products

@product_router.get("/product/{pid}/info", response_model=ProductResponse)
def get_product(pid: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == pid).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@product_router.post("/product/add", response_model=ProductResponse)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@product_router.put("/product/{pid}/update", response_model=ProductResponse)
def update_product(pid: int, product: ProductUpdate, db: Session = Depends(get_db)):
    existing_product = db.query(Product).filter(Product.id == pid).first()
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product.dict().items():
        setattr(existing_product, key, value)
    db.commit()
    db.refresh(existing_product)
    return existing_product
