from commands import AbstractCommand
from notes.Storage import AbstractStorage


class GetNotesCommand(AbstractCommand):
    def __init__(self, storage: AbstractStorage):
        super().__init__(storage)

    @property
    def name(self) -> str:
        return 'GET_NOTES'

    @property
    def help(self) -> str:
        return 'Prints all notes.'

    def can_execute(self, command: str) -> bool:
        return self.name == command

    def execute(self):
        print('\n'.join([str(note) for note in self._storage.get_all()]))
