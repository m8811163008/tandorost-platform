
from fastapi import FastAPI, HTTPException
from pymongo import ReturnDocument
from repository.model.serializer import convert_doc, convert_doc_list

@app.get("/")
async def root():
    collections = await client.list_database_names()
    return {
        "message" : "Connected to mongodb ",
        "collections" : collections
    }

@app.post("/items/")
async def create_item(item: Item):
    await collection.insert_one(item.model_dump())
    return {"message" : "Item created", "item" : item}

@app.get("/items/")
async def read_items():
    items = await collection.find().to_list(length=10)
    return {"message" : convert_doc_list(items)}

@app.put("/items/{name}")
async def update_item(name: str, item: Item):
    updated_item = await collection.find_one_and_update(
        {"name": name},
        {"$set": item.model_dump()},  
        return_document=ReturnDocument.AFTER
    )
    if updated_item:
        return {"message": "item updated", "item": convert_doc(updated_item)}
    raise HTTPException(status_code=404, detail=f"Item with name '{name}' not found")

@app.delete("/items/{name}")
async def delete_item(name: str):
    result = await collection.delete_one(
        {"name": name}
    )
    if result.deleted_count:
        return {"message": f"item deleted {name}",}
    raise HTTPException(status_code=404, detail=f"Item with name '{name}' not found")