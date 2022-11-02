from pathlib import Path
from zipfile import ZipFile

if __name__ == '__main__':
    # NOTE: Путь к папке с исходниками.
    source_directory = Path(__file__).parent

    # NOTE: Файлы исходного кода на Python (с расширением ".py").
    source_files = [entry for entry in source_directory.iterdir() if entry.is_file() and entry.name.endswith('.py')]

    # NOTE: Упаковываем исходники в архив.
    with ZipFile(source_directory.joinpath('sources.zip'), 'w') as zip_file:
        for file in source_files:
            zip_file.write(file.relative_to(source_directory))
