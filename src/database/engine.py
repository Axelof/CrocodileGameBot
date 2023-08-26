from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel as PydanticModel


class Engine:
    def __int__(self, name: str):
        # self.database = AsyncIOMotorClient()  # TODO: добавить генерацию URI для подключения

        self.remove_id = {"addresses": {"$slice": [0, 1]}, "_id": 0}

    async def add(self, data: dict):
        return NotImplemented

    async def add_many(self, data: list[dict]):
        return NotImplemented

    async def find(self, data: dict, model: type[PydanticModel]):
        return NotImplemented

    async def find_many(self, data: dict, model: type[PydanticModel]):
        return NotImplemented

    async def delete(self, data: dict):
        return NotImplemented

    async def update(self, old_data: dict, new_data: dict):
        return NotImplemented

    async def update_many(self, old_data: dict, new_data: dict):
        return NotImplemented

    async def delete_many(self, data: dict):
        return NotImplemented
