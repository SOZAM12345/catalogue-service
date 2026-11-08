
from acl.product_adapter import convertir_produit_externe


def test_conversion_produit_externe():

    produit_externe = {
        "productId": 1,
        "productName": "Ordinateur Lenovo",
        "unitPrice": 6500
    }

    resultat = convertir_produit_externe(
        produit_externe
    )

    assert resultat["id"] == 1
    assert resultat["name"] == "Ordinateur Lenovo"
    assert resultat["price"] == 6500
