import re

from commands import AbstractCommand
from notes.Storage import AbstractStorage


class GetNoteCommand(AbstractCommand):
    def __init__(self, storage: AbstractStorage):
        super().__init__(storage)
        self.__match = None

    @property
    def name(self) -> str:
        return 'GET_NOTE'

    @property
    def help(self) -> str:
        return 'Prints note.'

    def can_execute(self, command: str) -> bool:
        self.__match = re.match(rf'^{self.name} (\d+)$', command)
        return self.__match is not None

    def execute(self):
        try:
            note_id = int(self.__match[1])

            if note := self._storage.get_one(note_id):
                print(note)
            else:
                print(f'ERROR: note "{note_id}" not found.')
        except ValueError as error:
            print(f'ERROR: {error}')
