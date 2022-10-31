from typing import Iterable

from notes.Note import Note
from notes.Storage import AbstractStorage


class NoteManager(object):
    """Менеджер заметок. Управляет заметками определённой группы."""

    def __init__(self, name: str, storage: AbstractStorage):
        self.__name = name
        self.__storage = storage

    def list_notes(self) -> Iterable[Note]:
        """Возвращает все доступные заметки."""
        return self.__storage.get_all()

    def get_note(self, note_id: int) -> Note | None:
        """Возвращает указанную заметку, если таковая имеется."""
        return self.__storage.get_one(note_id)

    def save_note(self, note: Note):
        """Сохраняет заметку (создаёт новую или перезаписывает существующую)."""
        self.__storage.put_one(note)

    def delete_note(self, note_id: int):
        """Удаляет указанную заметку, если таковая имеется."""
        self.__storage.delete_one(note_id)
