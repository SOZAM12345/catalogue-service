
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


# Test 1 : récupérer tous les produits
def test_get_products():
    response = client.get("/products")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test 2 : récupérer le produit numéro 1
def test_get_product_by_id():
    response = client.get("/products/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1


# Test 3 : demander un produit inexistant
def test_product_not_found():
    response = client.get("/products/999999")

    assert response.status_code == 404
