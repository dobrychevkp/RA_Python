from configparser import ConfigParser
from pathlib import Path
from typing import Any, Dict


class ApplicationSettings(object):
    """Класс доступа к настройкам приложения."""

    __organization_name = 'RA_Python'
    __config_file_name = 'Remainder.conf'

    def __new__(cls):
        # NOTE: Singleton. В конструкторе создаём экземпляр класса лишь один раз.
        if not hasattr(cls, '__instance'):
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self):
        # NOTE: Парсер файла настроек. https://docs.python.org/3/library/configparser.html
        self.__config = ConfigParser()

        # NOTE: Создаём файл настроек с параметрами по умолчанию, если его ещё нет.
        if not self.__local_config_path().exists():
            self.__create_default_local_config()

        self.__read_config()

    @property
    def collection(self) -> str:
        """Коллекция слов."""
        return self.__get_value('General', 'collection', 'animals')

    @property
    def notifier(self) -> str:
        """Тип уведомителя."""
        return self.__get_value('General', 'notifier', 'stdout')

    @property
    def timeout(self) -> int:
        """Время задержки между рассылкой (в секундах)."""
        return int(self.__get_value('General', 'timeout', 5))

    @property
    def settings(self) -> Dict[str, Any]:
        return {
            'General/collection': self.collection,
            'General/notifier': self.notifier,
            'General/timeout': self.timeout,
        }

    def __create_default_local_config(self):
        self.__config['General'] = {}
        self.__config['General']['collection'] = 'animals'
        self.__config['General']['notifier'] = 'stdout'
        self.__config['General']['timeout'] = '2'

        path = self.__local_config_path()
        path.parent.mkdir(exist_ok=True)

        with path.open('w') as config_file:
            self.__config.write(config_file)

    def __read_config(self):
        # NOTE: Парсим ini-файл с настройками приложения.
        self.__config.read(self.__local_config_path())

    def __get_value(self, section: str, key: str, default_value: Any) -> Any:
        # WARNING: Каждый раз перечитываем файл для горячей смены настроек (не самый эффективный способ).
        self.__read_config()

        try:
            return self.__config[section][key]
        except KeyError:
            return default_value

    @staticmethod
    def __home_directory() -> Path:
        return Path.expanduser(Path('~'))

    @classmethod
    def __local_config_path(cls) -> Path:
        return cls.__home_directory().joinpath('.config', cls.__organization_name, cls.__config_file_name)


# NOTE: Сразу создадим экземпляр класса настроек.
application_settings = ApplicationSettings()
