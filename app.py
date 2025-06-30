from fastapi import FastAPI, HTTPException
from databases import Database
from sqlalchemy import create_engine
from model import items, metadata
from schema import Item

DATABASE_URL = "postgresql://altagrasa:pinkelephant@localhost:5432/altagrasa"
database = Database(DATABASE_URL)

app = FastAPI()

@app.on_event("startup")
async def startup():
    engine = create_engine(DATABASE_URL)
    metadata.create_all(engine)
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
async def health():
    await database.execute("SELECT 1")
    return {"status": "ok"}

@app.post("/items/")
async def create_item(payload: Item):
    item_data = {
        "title": payload.title,
        "description": payload.description,
        "price": payload.price 
    }
    item_id = await database.execute(items.insert().values(**item_data))
    return {"message": "item created", "item_id": item_id}

@app.get("/items/")
async def get_items():
    query = items.select()
    results = await database.fetch_all(query)
    return results

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    item_check = await database.fetch_one(
        items.select().where(items.c.id == item_id)
    )
    if not item_check:
        raise HTTPException(status_code=404, detail="Item not found")
    
    await database.execute(items.delete().where(items.c.id == item_id))
    return {"message": "item deleted"}