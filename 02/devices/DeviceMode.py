from enum import Enum


class DeviceMode(Enum):
    ReadOnly = 0x01
    WriteOnly = 0x02
    ReadWrite = 0x03
