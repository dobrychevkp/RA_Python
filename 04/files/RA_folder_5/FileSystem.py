from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass
class FileInfo:
    name: str
    size: int
    content: str


class FileFilter(object):
    def __init__(self, prefix: str, extension: str):
        self.__folder_prefix = prefix
        self.__file_extension = extension

    def find(self, path: Path) -> Iterable[FileInfo]:
        # NOTE: Перебираем все элементы в указанной папке.
        for folder in path.iterdir():
            # NOTE: Оставляем только папки, начинающиеся с указанного префикса.
            if folder.is_dir() and folder.name.startswith(self.__folder_prefix):
                # NOTE: Перебираем все элементы в каждой такой папке.
                for file in folder.iterdir():
                    # NOTE: Оставляем только файлы с указанным расширением.
                    if file.is_file() and file.suffix == f'.{self.__file_extension}':
                        # NOTE: Собираем нужную информацию по файлу и возвращаем её.
                        yield FileInfo(str(file.absolute()), file.stat().st_size, file.open('r').read())


if __name__ == '__main__':
    for info in FileFilter('RA_', 'txt').find(Path('files')):
        print(info)
