from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Artists(Base):
    __tablename__: str = "artists"

    ArtistId: Column = Column(Integer, primary_key=True)
    Name: Column = Column(String)
    # AlbumId: Column = Column(Integer, ForeignKey('albums.AlbumId'))


class Albums(Base):
    __tablename__: str = "albums"

    AlbumId: Column = Column(Integer, primary_key=True)
    Title: Column = Column(String)
    ArtistId: Column = Column(Integer, ForeignKey("artists.ArtistId"))


class Tracks(Base):
    __tablename__: str = "tracks"

    TrackId: Column = Column(Integer, primary_key=True)
    Name: Column = Column(String)
    AlbumID: Column = Column(Integer, ForeignKey("albums.AlbumId"))
    GenreId: Column = Column(Integer, ForeignKey("tracks.GenreId"))


class Genres(Base):
    __tablename__: str = "genres"

    GenreId: Column = Column(Integer, primary_key=True)
    Name: Column = Column(String)
