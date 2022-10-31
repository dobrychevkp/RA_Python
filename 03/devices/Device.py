from typing import List

from devices.DeviceMode import DeviceMode


class Device:
    __devices = {
        '/devices/dev0': (DeviceMode.ReadOnly, ['line_1', 'line_2']),
        '/devices/dev1': (DeviceMode.WriteOnly, ['']),
        '/devices/dev2': (DeviceMode.ReadWrite, []),
        '/devices/dev3': (DeviceMode.ReadWrite, ['1', '2', '**']),
        '/devices/dev4': (DeviceMode.ReadOnly, ['line_1', 'line_2']),
    }

    @classmethod
    def open(cls, name: str) -> 'Device':
        """
        Открывает указанное устройство.

        :param name: имя устройства
        :return: открытое устройство

        :exception IOError: если устройство не зарегистрировано в таблице
        """

        try:
            mode, data = cls.__devices[name]
            return Device(mode, data)
        except KeyError:
            raise IOError('Device not found')

    def __init__(self, mode: DeviceMode, data: List[str]):
        self.__mode = mode
        self.__data = data

    @property
    def mode(self) -> DeviceMode:
        return self.__mode

    @property
    def is_readable_device(self) -> bool:
        """Показывает, можно ли читать из устройства."""
        return DeviceMode.ReadOnly in self.__mode

    @property
    def is_writable_device(self) -> bool:
        """Показывает, можно ли писать в устройство."""
        return DeviceMode.WriteOnly in self.__mode

    def read_line(self) -> str:
        """
        Читает строку текста из устройства.

        :return: считанная строка
        :exception IOError: если строка не может быть прочитана из устройства
        :exception PermissionError: если устройство не открыто на чтение
        """

        if not self.is_readable_device:
            raise PermissionError('Reading from the device not allowed.')

        return Device.__take_line(self.__data)

    def write_line(self, line: str):
        """
        Пишет строку текста в устройство.

        :param line: записываемая строка
        :exception PermissionError: если устройство не открыто на запись
        """

        if not self.is_writable_device:
            raise PermissionError('Writing to the device not allowed.')

        self.__data.append(line)

    @staticmethod
    def __take_line(collection: List[str]) -> str:
        try:
            return collection.pop(0)
        except IndexError:
            raise IOError('No more for reading')
