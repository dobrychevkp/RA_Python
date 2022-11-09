# NOTE: Для уникальных идентификаторов заметок используем модуль uuid. https://docs.python.org/3/library/uuid.html
import uuid

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Note:
    note_id: uuid
    author: str
    message: str

    def to_json(self) -> Dict[str, Any]:
        return {
            'note_id': str(self.note_id),
            'author': self.author,
            'message': self.message,
        }
