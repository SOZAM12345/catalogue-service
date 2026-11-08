
from acl.product_adapter import convertir_produit_externe

# Exemple d'un produit envoyé par un système externe
produit_externe = {
    "productId": 1,
    "productName": "Ordinateur Lenovo",
    "unitPrice": 6500
}

# Appeler notre ACL
produit_converti = convertir_produit_externe(
    produit_externe
)

print("Produit externe :", produit_externe)
print("Produit après ACL :", produit_converti)
