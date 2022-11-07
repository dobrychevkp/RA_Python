from abc import abstractmethod

# NOTE: Коллекция с счётчиком элементов. https://docs.python.org/3/library/collections.html#collections.Counter
from collections import Counter

from pathlib import Path
from typing import Dict, Any


class AbstractCollector(object):
    @abstractmethod
    def push(self, word: str):
        pass

    @abstractmethod
    def save(self):
        pass


class PrintCollector(AbstractCollector):
    def push(self, word: str):
        print(word)

    @abstractmethod
    def save(self):
        pass


class WordCountCollector(AbstractCollector):
    def __init__(self,):
        self.__filename = None
        self.__ignore_case = False
        self.__words = Counter()

    def configure(self, options: Dict[str, Any]):
        self.__ignore_case = options.get('ignore_case', False)
        self.__filename = Path(options['output'])

    def push(self, word: str):
        # NOTE: Обновляем коллекцию слов (вставляем новые или увеличиваем счётчики уже существующих).
        self.__words.update([word.lower() if self.__ignore_case else word])

    def save(self):
        with self.__filename.open('w') as f:
            for key, value in self.__results():
                f.write(f'{key}: {value}\n')

    def __results(self):
        # NOTE: Сортируем слова по убыванию значения счётчика.
        return sorted(self.__words.items(), key=lambda x: x[1], reverse=True)
