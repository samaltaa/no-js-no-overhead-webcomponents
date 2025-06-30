from sqlalchemy import *

metadata = MetaData()

items = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(30), nullable=False),
    Column("description", String(50), nullable=False),
    Column("price", String(30), nullable=False)
)