from abc import abstractmethod
from typing import AsyncIterable

from notes.Note import Note


class AbstractStorage(object):
    """Интерфейс хранилища заметок."""

    def create(self, *args, **kwargs):
        """Создаёт хранилище заметок со специфичными параметрами."""
        pass

    async def contains(self, key: str) -> bool:
        """Проверяет, содержится ли в хранилище запись с указанным ключом."""
        return await self.get_one(key) is not None

    @abstractmethod
    def get_all(self) -> AsyncIterable[Note]:
        """Возвращает все доступные заметки."""
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, key: str) -> Note | None:
        """Возвращает указанную заметку, если таковая имеется."""
        raise NotImplementedError

    @abstractmethod
    async def put_one(self, note: Note):
        """Размещает указанную заметку в хранилище."""
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, key: str):
        """Удаляет указанную заметку, если таковая имеется."""
        raise NotImplementedError
