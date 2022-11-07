import json
import re

from commands import AbstractCommand

from notes.Note import Note
from notes.Storage import AbstractStorage


class PutNoteCommand(AbstractCommand):
    def __init__(self, storage: AbstractStorage):
        super().__init__(storage)
        self.__match = None

    @property
    def name(self) -> str:
        return 'PUT_NOTE'

    @property
    def help(self) -> str:
        return 'Inserts new note or updates existent.'

    def can_execute(self, command: str) -> bool:
        self.__match = re.match(rf'^{self.name} (.*)$', command)
        return self.__match is not None

    def execute(self):
        try:
            data = self.__match[1]
            self._storage.put_one(Note(**json.loads(data)))
        except (TypeError, ValueError) as error:
            print(f'ERROR: {error}')
