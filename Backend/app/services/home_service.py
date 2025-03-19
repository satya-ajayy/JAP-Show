from app.models.movies import MovieModel, MovieUpdateModel, MovieCreateModel
from app.repositories.movies_repo import MovieRepository


class HomePageService:
    @staticmethod
    async def GetRecommendedMovies() -> str:
       return ""

    @staticmethod
    async def GetBanners() -> dict:
        return {}
