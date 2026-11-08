
import os

from dotenv import load_dotenv
from sqlalchemy import URL
from sqlmodel import create_engine, Session

# 1. Lire les informations du fichier .env
load_dotenv()

# 2. Préparer l'adresse de PostgreSQL
database_url = URL.create(
    drivername="postgresql+psycopg",
    username=os.environ["PG_USER"],
    password=os.environ["PG_PASSWORD"],
    host=os.getenv("PG_HOST", "localhost"),
    port=int(os.getenv("PG_PORT", "5432")),
    database=os.getenv("PG_DB", "catalogue_db")
)

# 3. Préparer la connexion à PostgreSQL
engine = create_engine(database_url)

# 4. Permettre aux API d'utiliser la base
def get_session():
    with Session(engine) as session:
        yield session
