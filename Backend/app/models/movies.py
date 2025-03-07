import uuid
from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict, field_validator
from app.utils.helpers import GetCurrentUTCTime


class MovieCreateModel(BaseModel):
    title: str
    image_url: str
    rating: float
    votes: int
    genre: List[str]

    @field_validator('genre')
    def validate_genre_not_empty(cls, value: List[str]) -> List[str]:
        if not value:
            raise ValueError("Genre list cannot be empty")
        return value


class MovieUpdateModel(BaseModel):
    rating: Optional[float] = None
    votes: Optional[int] = None
    image_url: Optional[str] = None

    def model_dump(self, **kwargs):
        kwargs.setdefault("exclude_none", True)
        return super().model_dump(**kwargs)


class MovieModel(BaseModel):
    movie_id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    title: str
    image_url: str
    rating: float
    votes: int
    genre: List[str]
    created_at: str = Field(default_factory=lambda: GetCurrentUTCTime())

    model_config = ConfigDict(populate_by_name=True)

    @classmethod
    def from_create_model(cls, create_model: "MovieCreateModel") -> "MovieModel":
        return cls(
            title=create_model.title,
            image_url=create_model.image_url,
            rating=create_model.rating,
            votes=create_model.votes,
            genre=create_model.genre
        )


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