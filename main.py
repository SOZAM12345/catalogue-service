
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select

from database import get_session
from models import Product

# Créer notre microservice Catalogue
app = FastAPI(title="Catalogue Microservice")


# API 1 : récupérer tous les produits
@app.get("/products", response_model=list[Product])
def get_products(
    session: Session = Depends(get_session)
):
    products = session.exec(
        select(Product)
    ).all()

    return products


# API 2 : récupérer un produit par son ID
@app.get("/products/{product_id}", response_model=Product)
def get_product(
    product_id: int,
    session: Session = Depends(get_session)
):
    product = session.get(Product, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Produit introuvable"
        )

    return product
