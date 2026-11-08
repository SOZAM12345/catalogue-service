
def convertir_produit_externe(produit_externe):
    """
    Convertit les données d'un système externe
    vers le modèle interne du Catalogue.
    """

    return {
        "id": produit_externe["productId"],
        "name": produit_externe["productName"],
        "price": produit_externe["unitPrice"]
    }
