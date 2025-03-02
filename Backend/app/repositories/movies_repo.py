from app.db.mongo import mongo
from app.models.movies import MoviesSerializer, MovieSerializer


class MovieRepository:
    @staticmethod
    async def CreateMovie(movie_data: dict) -> str:
        new_movie = await mongo.db["movies"].insert_one(movie_data)
        return new_movie.inserted_id

    @staticmethod
    async def GetMovies(limit: int) -> list:
        cursor = mongo.db["movies"].find({})
        movies = await cursor.to_list(length=limit)
        return MoviesSerializer(movies)

    @staticmethod
    async def GetMovieById(movie_id: str) -> dict:
        movie =  await mongo.db["movies"].find_one({"_id": movie_id})
        return MovieSerializer(movie)

    @staticmethod
    async def UpdateMovie(movie_id: str, movie_data: dict) -> bool:
        await mongo.db["movies"].update_one({"_id": movie_id}, {"$set": movie_data})
        return True

    @staticmethod
    async def DeleteMovie(movie_id: str) -> bool:
        await mongo.db["movies"].delete_one({"_id": movie_id})
        return True