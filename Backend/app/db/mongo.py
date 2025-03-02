from motor.motor_asyncio import AsyncIOMotorClient

class MongoDB:
    client: AsyncIOMotorClient = None
    db = None

    @classmethod
    async def connect(cls):
        cls.client = AsyncIOMotorClient("mongodb://localhost:27017")
        cls.db = cls.client["jap-show"]

    @classmethod
    async def disconnect(cls):
        if cls.client:
            cls.client.close()

mongo = MongoDB()
