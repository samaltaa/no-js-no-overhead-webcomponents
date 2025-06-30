from fastapi import FastAPI, HTTPException, Request
from databases import Database
from sqlalchemy import create_engine
from model import items, metadata
from schema import Item

#template 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

DATABASE_URL = "postgresql://altagrasa:pinkelephant@localhost:5432/altagrasa"
database = Database(DATABASE_URL)

app = FastAPI()

templates = Jinja2Templates(directory="templates")

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

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: int):
    #fetch item from db
    query = items.select().where(items.c.id == id)
    item = await database.fetch_one(query)

    #check if item exists
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # pass the item data to the template
    return templates.TemplateResponse(
        request=request,
        name="item.html",
        context={"item": item}
    )

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    item_check = await database.fetch_one(
        items.select().where(items.c.id == item_id)
    )
    if not item_check:
        raise HTTPException(status_code=404, detail="Item not found")
    
    await database.execute(items.delete().where(items.c.id == item_id))
    return {"message": "item deleted"}