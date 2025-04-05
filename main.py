from fastapi import FastAPI

app = FastAPI(root_path="/api/v1")

@app.get("/")
async def read_root():
    return {"Hello": "World"}