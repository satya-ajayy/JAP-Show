from app.models.movies import MovieModel, MovieUpdateModel
from app.repositories.movies_repo import MovieRepository

class MovieService:
    @staticmethod
    async def CreateMovie(movie: MovieModel) -> str:
        movie_dict =  movie.model_dump(by_alias=True)
        return await MovieRepository.CreateMovie(movie_dict)

    @staticmethod
    async def GetMovies() -> list:
        movies = await MovieRepository.GetMovies(limit=10)
        return movies

    @staticmethod
    async def GetMovieById(movie_id: str) -> dict:
        movie = await MovieRepository.GetMovieById(movie_id)
        return movie

    @staticmethod
    async def UpdateMovie(movie_id: str, movie: MovieUpdateModel) -> bool:
        movie_dict = movie.model_dump(by_alias=True)
        return await MovieRepository.UpdateMovie(movie_id, movie_dict)

    @staticmethod
    async def DeleteMovie(movie_id: str) -> bool:
        return await MovieRepository.DeleteMovie(movie_id)