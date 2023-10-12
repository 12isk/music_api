from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Artists(Base):
    __tablename__ = "artists"

    ArtistId = Column(Integer, primary_key = True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey('albums.AlbumId'))

class Albums(Base):
    __tablename__ = "albums"

    AlbumId = Column(Integer, primary_key = True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("artists.ArtistId"))

class Tracks(Base):
    __tablename__ = "tracks"

    TruerackId = Column(Integer, primary_key= True)
    Name = Column(String)
    Composer = Column(String)
    Milliseconds = Column(Integer)
    AlbumID = Column(Integer, ForeignKey("albums.AlbumId"))



    