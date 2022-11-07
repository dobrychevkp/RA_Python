from commands import *

from notes.Storage import AbstractStorage


class CommandFactory(object):
    def __init__(self, storage: AbstractStorage):
        self.commands = [
            GetNoteCommand(storage),
            GetNotesCommand(storage),
            PutNoteCommand(storage),
            DeleteNoteCommand(storage),
        ]

    def get_command(self, line: str) -> AbstractCommand:
        for command in self.commands:
            if command.name == line:
                return command
