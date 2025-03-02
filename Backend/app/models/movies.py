import uuid
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict

class MovieModel(BaseModel):
    movie_id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    title: str
    image_url: str
    rating: float
    votes: int
    genre: str
    model_config = ConfigDict(populate_by_name=True)

class MovieUpdateModel(BaseModel):
    rating: float
    votes: int
    image_url: Optional[str]

def MovieSerializer(movie) -> dict:
    return {
        "movie_id": movie["_id"],
        "title": movie["title"],
        "image_url": movie["image_url"],
        "rating": movie["rating"],
        "votes": movie["votes"],
        "genre": movie["genre"],
    }

def MoviesSerializer(movies) -> list:
    return [MovieSerializer(movie) for movie in movies]
