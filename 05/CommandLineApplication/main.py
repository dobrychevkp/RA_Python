from pathlib import Path

from commands import AbstractCommand, CommandFactory
from notes.Storage import DatabaseStorage


if __name__ == '__main__':
    factory = CommandFactory(DatabaseStorage(Path('notes.db')))

    while True:
        try:
            line = input('==> ')
            command: AbstractCommand = factory.get_command(line)
            command.execute()
        except KeyboardInterrupt:
            print('closing...')
            break
