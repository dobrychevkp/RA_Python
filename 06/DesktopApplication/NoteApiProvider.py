from typing import Dict, List

# NOTE: Очень простая библиотека для отправки HTTP-запросов. https://docs.python-requests.org/en/latest/
import requests


class NoteApiProvider(object):
    def __init__(self, service: str):
        self.__api_url = f'{service}/api/notes'

    def get_notes(self) -> List[str]:
        return requests.get(self.__api_url).json()

    def get_note(self, key: str) -> Dict[str, str]:
        return requests.get(f'{self.__api_url}/{key}').json()

    def add_note(self, key: str, data: Dict[str, str]):
        requests.post(f'{self.__api_url}/{key}', json=data)

    def update_note(self, key: str, data: Dict[str, str]):
        requests.put(f'{self.__api_url}/{key}', json=data)

    def delete_note(self, key: str):
        requests.delete(f'{self.__api_url}/{key}')
