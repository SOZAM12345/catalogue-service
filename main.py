
from pathlib import Path

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlmodel import Session, select

from database import get_session
from models import Product


# 1. Créer notre microservice Catalogue
app = FastAPI(title="Catalogue Microservice")


# 2. Autoriser la communication avec React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


# 3. Rendre les images accessibles via FastAPI
BASE_DIR = Path(__file__).resolve().parent

app.mount(
    "/images",
    StaticFiles(directory=BASE_DIR / "images"),
    name="images"
)


# 4. API REST : récupérer tous les produits
@app.get("/products", response_model=list[Product])
def get_products(
    session: Session = Depends(get_session)
):
    products = session.exec(
        select(Product)
    ).all()

    return products


# 5. API REST : récupérer un produit par son ID
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
