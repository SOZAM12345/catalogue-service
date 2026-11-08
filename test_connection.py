
from database import engine
from sqlalchemy import text

# Essayer de se connecter à PostgreSQL
try:
    with engine.connect() as connexion:
        resultat = connexion.execute(
            text("SELECT current_database()")
        )

        print("Connexion PostgreSQL réussie !")
        print("Base de données :", resultat.scalar())

except Exception as erreur:
    print("Erreur de connexion :", erreur)
