from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routers.books import router as book_router

config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient('localhost', 27017)
    app.database = app.mongodb_client['pymongo_tutorial']

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(book_router, tags=["books"], prefix="/book")

