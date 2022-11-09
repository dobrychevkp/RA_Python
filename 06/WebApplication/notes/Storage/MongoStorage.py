import asyncio
import uuid

from typing import Any, AsyncIterable, Dict

# NOTE: Модуль для работы с базами данных MongoDB. https://motor.readthedocs.io/en/stable/
from motor.motor_asyncio import AsyncIOMotorClient

from notes.Note import Note
from notes.Storage import AbstractStorage


class MongoStorage(AbstractStorage):
    """Хранилище заметок в базе данных MongoDB."""

    def __init__(self):
        self.__client = None
        self.__collection = None

    def create(self, connection: Dict[str, Any], database: str, collection: str):
        self.__client = AsyncIOMotorClient(self.__mongo_uri(**connection))

        # WARNING: Подменяем event_loop на текущий, запущенный в рамках aiohttp-приложения.
        self.__client.get_io_loop = asyncio.get_running_loop

        self.__collection = self.__client[database][collection]

    async def get_all(self) -> AsyncIterable[Note]:
        async for value in self.__collection.find():
            yield self.__make_note(value)

    async def get_one(self, note_id: str) -> Note | None:
        return self.__make_note(await self.__collection.find_one({'_id': note_id}))

    async def put_one(self, note: Note):
        value = note.to_json()

        # NOTE: Подменяем стандартный идентификатор документа на тот, который уже есть у заметки.
        # NOTE: https://www.mongodb.com/docs/manual/reference/bson-types/#objectid
        value['_id'] = value.pop('note_id')

        await self.__collection.find_one_and_replace({'_id': str(note.note_id)}, value, upsert=True)

    async def delete_one(self, note_id: str):
        await self.__collection.delete_one({'_id': note_id})

    @staticmethod
    def __mongo_uri(host: str, port: int, user: str, password: str):
        return f'mongodb://{user}:{password}@{host}:{port}'

    @staticmethod
    def __make_note(value: Dict[str, Any]) -> Note | None:
        if value:
            # NOTE: Возвращаем нужный нам идентификатор заметки.
            value['note_id'] = uuid.UUID(value.pop('_id'))
            return Note(**value)

        return None
