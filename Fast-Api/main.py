from fastapi import FastAPI
from database import init_db
from routes import product_router

app = FastAPI()

init_db()
app.include_router(product_router)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI server is running!"}
