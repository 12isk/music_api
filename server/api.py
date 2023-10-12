import fastapi
from fastapi import FastAPI, Depends, HTTPException
import database, models 
from database import SessionLocal
import models 

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello World"}


def get_db() -> SessionLocal:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@app.get("/artists/name/{artist_name}")
async def read_artist_name(artist_name: str, db = Depends(get_db)):
    qry = db.query(models.Artists)
    
    artists = qry.filter(models.Artists.Name.like(f'%{artist_name}%')).all()
    
    if artists:
        return {"artist_name": artists}
    raise HTTPException(status_code = 404, detail="Artist not found.")

@app.get("/artists/{id}")
async def get_album_by_id(id: int, db = Depends(get_db)):
    
    qry = db.query(models.Albums)
    albums = qry.filter(models.Albums.ArtistId == id).all()

    if (albums):
        return albums
    raise HTTPException(status_code = 404, detail="Albums not found.")
