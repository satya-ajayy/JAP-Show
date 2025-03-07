from motor.motor_asyncio import AsyncIOMotorClient
from app.config.settings import settings

class MongoDB:
    client: AsyncIOMotorClient = None
    db = None

    @classmethod
    async def connect(cls):
        cls.client = AsyncIOMotorClient(settings.MONGO_URI)
        cls.db = cls.client["jap-show"]

    @classmethod
    async def disconnect(cls):
        if cls.client:
            cls.client.close()

mongo = MongoDB()
