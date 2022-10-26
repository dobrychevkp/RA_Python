from dataclasses import dataclass
from typing import List

from devices.DeviceMode import DeviceMode


@dataclass
class Device:
    mode: DeviceMode
    data: List[str]


def __take_line(collection: List[str]) -> str:
    try:
        return collection.pop(0)
    except IndexError:
        raise RuntimeError('No more data to read.')


def is_readable(device: Device) -> bool:
    return device.mode == DeviceMode.ReadOnly or device.mode == DeviceMode.ReadWrite


def is_writable(device: Device) -> bool:
    return device.mode == DeviceMode.WriteOnly or device.mode == DeviceMode.ReadWrite


def read_line(device: Device) -> str:
    if not is_readable(device):
        raise PermissionError('Reading from the device not allowed.')

    return __take_line(device.data)


def open_device(name: str) -> Device:
    devices = {
        '/devices/dev0': Device(DeviceMode.ReadOnly, ['line_1', 'line_2']),
        '/devices/dev1': Device(DeviceMode.WriteOnly, ['']),
        '/devices/dev2': Device(DeviceMode.ReadWrite, []),
        '/devices/dev3': Device(DeviceMode.ReadWrite, ['1', '2', '**']),
        '/devices/dev4': Device(DeviceMode.ReadOnly, ['line_1', 'line_2']),
    }

    try:
        return devices[name]
    except KeyError:
        raise RuntimeError('Device not found.')
