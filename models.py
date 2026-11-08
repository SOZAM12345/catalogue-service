
from sqlmodel import SQLModel, Field


class Product(SQLModel, table=True):
    __tablename__ = "products"

    id: int | None = Field(
        default=None,
        primary_key=True
    )
    name: str
    category: str
    price: float
    image: str
    description: str
