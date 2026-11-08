
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select

from database import get_session
from models import Product

# Créer notre microservice Catalogue
app = FastAPI(title="Catalogue Microservice")

# Autoriser la communication avec React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


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
