from fastapi import APIRouter
from app.models.movies import MovieModel, MovieUpdateModel, MovieCreateModel
from app.services.movies_service import MovieService

router = APIRouter()

@router.get("/movies")
async def GetAll():
    movies = await MovieService.GetMovies()
    return {
        "meta_data":[{
            "count" : len(movies)
        }],
        "data": movies
    }

@router.post("/movies", status_code=201)
async def Insert(movie: MovieCreateModel):
    movie_id = await MovieService.CreateMovie(movie)
    return {
        "message": "Movie Inserted Successfully",
        "movie_id": movie_id
    }

@router.get("/movies/{movie_id}")
async def GetOne(movie_id: str):
    movie = await MovieService.GetMovieById(movie_id)
    return movie

@router.put("/movies/{movie_id}")
async def Update(movie_id: str, movie: MovieUpdateModel):
    await MovieService.UpdateMovie(movie_id, movie)
    return {
        "message": "Movie Updated Successfully",
        "movie_id": movie_id
    }

@router.delete("/movies/{movie_id}")
async def Delete(movie_id: str):
    await MovieService.DeleteMovie(movie_id)
    return {
        "message": "Movie Deleted Successfully",
        "movie_id": movie_id
    }


