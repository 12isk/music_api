from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Artists(Base):
    __tablename__ = "artists"

    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

class Albums(Base):
    __tablename__ = "albums"

    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = relationship("Artists", back_populates="artistId")

class Tracks(Base):
    __tablename__ = "tracks"

    TruerackId = Column(Integer, primary_key= True)
    Name = Column(String)
    Composer = Column(String)
    Milliseconds = Column(Integer)
    AlbumID = relationship("Albums", back_populates="albumID")




    