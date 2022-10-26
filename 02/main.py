from dataclasses import dataclass
from enum import Enum


class DeviceMode(Enum):
    ReadOnly = 0x01
    WriteOnly = 0x02
    ReadWrite = 0x03


@dataclass
class Device:
    mode: DeviceMode
    data: list


devices = {
    '/devices/dev0': Device(DeviceMode.ReadOnly, ['line_1', 'line_2']),
    '/devices/dev1': Device(DeviceMode.WriteOnly, ['']),
    '/devices/dev2': Device(DeviceMode.ReadWrite, []),
    '/devices/dev3': Device(DeviceMode.ReadWrite, ['1', '2', '**']),
    '/devices/dev4': Device(DeviceMode.ReadOnly, ['line_1', 'line_2']),
}

device = devices['/devices/dev3']

for i in range(3):
    if not (device.mode == DeviceMode.ReadOnly or device.mode == DeviceMode.ReadWrite):
        raise PermissionError('Reading from the device not allowed.')

    print(device.data.pop(0))
