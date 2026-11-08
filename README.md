# Catalogue Microservice — E-Commerce MSOA

## Description

Ce projet est un microservice Catalogue développé dans le cadre du TP *Building a Microservices-Oriented Application*.

Il permet de consulter les produits d'une plateforme e-commerce à travers des API REST.

Le microservice est développé indépendamment des autres services de l'application.

## Technologies utilisées

- Python 3.12
- FastAPI
- PostgreSQL 17
- SQLModel
- Psycopg
- Pytest

## Architecture

```text
Client / Frontend React
         |
         | HTTP / REST
         v
Microservice Catalogue (FastAPI)
         |
         | SQLModel
         v
PostgreSQL (catalogue_db)
```

## API REST

| Méthode | Endpoint | Description |
|---|---|---|
| GET | `/products` | Récupérer tous les produits |
| GET | `/products/{product_id}` | Récupérer un produit par son identifiant |

Le microservice fonctionne sur le port `8082`.

Documentation interactive : `http://127.0.0.1:8082/docs`

## Base de données

Le microservice dispose de sa propre base PostgreSQL appelée `catalogue_db`.

La table `products` contient les informations suivantes :

- id
- name
- category
- price
- image
- description

La gestion des stocks relève du microservice Inventory et non du Catalogue.

## Anti-Corruption Layer (ACL)

Le projet contient un adaptateur dans `acl/product_adapter.py`.

Cet adaptateur transforme un exemple de modèle externe :

- `productId` → `id`
- `productName` → `name`
- `unitPrice` → `price`

**État actuel :** cet adaptateur est une démonstration du principe ACL. Son intégration avec un véritable système externe reste à définir et à implémenter selon les contrats du groupe.

## Installation

Cloner le dépôt :

```bash
git clone https://github.com/SOZAM12345/catalogue-service.git
cd catalogue-service
```

Créer un environnement virtuel :

```bash
python -m venv .venv
```

Installer les dépendances :

```bash
python -m pip install -r requirements.txt
```

Créer une base PostgreSQL appelée `catalogue_db`.

Créer un fichier `.env` dans le dossier principal :

```dotenv
PG_HOST=localhost
PG_PORT=5432
PG_USER=postgres
PG_PASSWORD=votre_mot_de_passe
PG_DB=catalogue_db
```

Ne jamais publier le fichier `.env`.

Créer les tables :

```bash
python create_tables.py
```

**Remarque :** la création des tables ne remplit pas automatiquement la base de données. Des produits doivent être ajoutés séparément.

Lancer le microservice :

```bash
python -m uvicorn main:app --reload --port 8082
```

## Tests

Exécuter les tests automatiques :

```bash
python -m pytest -v
```

Quatre tests ont été validés dans l'environnement local de développement :

- Consultation de tous les produits.
- Consultation d'un produit par identifiant.
- Réponse HTTP 404 pour un produit inexistant.
- Conversion d'un produit externe avec l'adaptateur ACL.

Les tests des API utilisent actuellement la base PostgreSQL locale, avec des données de démonstration.

## Projet de référence

Frontend React fourni par le professeur :

https://github.com/ZOUHEIRBN/MSOA-E-com-Demo

## État du projet

- API Catalogue fonctionnelles.
- Connexion PostgreSQL opérationnelle.
- Tests automatiques validés localement.
- Démonstration d'adaptateur ACL.
- Intégration avec les autres microservices à réaliser.