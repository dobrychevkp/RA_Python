from commands import AbstractCommand
from notes.Storage import AbstractStorage

from typing import List


class GetNotesCommand(AbstractCommand):
    def __init__(self, storage: AbstractStorage):
        super().__init__(storage)

    @property
    def name(self) -> str:
        return 'GET_NOTES'

    @property
    def help(self) -> str:
        return 'Prints all notes.'

    @property
    def arguments(self) -> List[str]:
        return []

    def execute(self, _):
        print('\n'.join([str(note) for note in self._storage.get_all()]))
