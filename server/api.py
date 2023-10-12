import fastapi
from fastapi import FastAPI
from . import database, models 
from database import SessionLocal
from models import Artists, Albums, Tracks

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello World"}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@app.get("/artists/{name}")
async def read_artist_name(artist_name: str):
    db = get_db
    db_artists = db.query(Artists).filter(Artists.Name.contains(artist_name))
    return db_artists