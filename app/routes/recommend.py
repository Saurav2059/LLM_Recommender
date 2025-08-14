from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Product
from app.recommender import recommend_products

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def get_recommendations(query: str, db: Session = Depends(get_db)):
    products = db.query(Product).all()
    recommended = recommend_products(query, products)
    return {"recommendations": [p.name for p in recommended]}