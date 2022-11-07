from abc import abstractmethod

from typing import Any, Dict, List

from notes.Storage import AbstractStorage


class AbstractCommand(object):
    def __init__(self, storage: AbstractStorage):
        self._storage = storage

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def help(self) -> str:
        pass

    @property
    @abstractmethod
    def arguments(self) -> List[str]:
        pass

    @abstractmethod
    def execute(self, options: Dict[str, Any]):
        pass
