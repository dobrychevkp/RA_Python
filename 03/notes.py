from notes.NoteManager import NoteManager
from notes.Storage import *


if __name__ == '__main__':
    storage: AbstractStorage = ReadWriteStorage()
    storage.put_one(Note(1, 'a_1', 'm_1'))
    storage.put_one(Note(2, 'a_1', 'm_2'))

    manager = NoteManager('Work', storage)

    note: Note = manager.get_note(2)
    note.message = 'edited_message'

    manager.save_note(note)

    for note in manager.list_notes():
        print(note)
