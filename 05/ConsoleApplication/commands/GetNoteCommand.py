from typing import Any, Dict, List

from commands import AbstractCommand
from notes.Storage import AbstractStorage


class GetNoteCommand(AbstractCommand):
    def __init__(self, storage: AbstractStorage):
        super().__init__(storage)

    @property
    def name(self) -> str:
        return 'GET_NOTE'

    @property
    def help(self) -> str:
        return 'Prints note.'

    @property
    def arguments(self) -> List[str]:
        return ['node_id']

    def execute(self, options: Dict[str, Any]):
        try:
            note_id = int(options['node_id'])

            if note := self._storage.get_one(note_id):
                print(note)
            else:
                print(f'ERROR: note "{note_id}" not found.')
        except ValueError as error:
            print(f'ERROR: {error}')
