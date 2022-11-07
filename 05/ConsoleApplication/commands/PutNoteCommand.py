from typing import Any, Dict, List

from commands import AbstractCommand

from notes.Note import Note
from notes.Storage import AbstractStorage


class PutNoteCommand(AbstractCommand):
    def __init__(self, storage: AbstractStorage):
        super().__init__(storage)

    @property
    def name(self) -> str:
        return 'PUT_NOTE'

    @property
    def help(self) -> str:
        return 'Inserts new note or updates existent.'

    @property
    def arguments(self) -> List[str]:
        return ['note_id', 'author', 'message']

    def execute(self, options: Dict[str, Any]):
        try:
            self._storage.put_one(self.__make_note(options))
        except (TypeError, ValueError) as error:
            print(f'ERROR: {error}')

    @staticmethod
    def __make_note(options: Dict[str, Any]) -> Note:
        del options['command']
        return Note(**options)
