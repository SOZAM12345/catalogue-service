
from sqlmodel import SQLModel

from database import engine
from models import Product

SQLModel.metadata.create_all(engine)

print("Table products créée avec succès !")
