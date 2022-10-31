import unittest

from devices.Device import *


class DeviceTestCase(unittest.TestCase):
    def test_open(self):
        self.assertIsInstance(Device.open('/devices/dev0'), Device)
        self.assertIsInstance(Device.open('/devices/dev1'), Device)
        self.assertIsInstance(Device.open('/devices/dev2'), Device)
        self.assertIsInstance(Device.open('/devices/dev3'), Device)
        self.assertIsInstance(Device.open('/devices/dev4'), Device)

        self.assertRaises(IOError, Device.open, '/devices/unknown')

    def test_read_line(self):
        self.assertEqual('line_1', Device.open('/devices/dev0').read_line())
        self.assertRaises(PermissionError, Device.read_line, Device.open('/devices/dev1'))
        self.assertRaises(IOError, Device.read_line, Device.open('/devices/dev2'))
        self.assertEqual('1', Device.open('/devices/dev3').read_line())
        self.assertEqual('line_1', Device.open('/devices/dev4').read_line())

    def test_write_line(self):
        self.assertRaises(PermissionError, Device.write_line, Device.open('/devices/dev0'), 'line')

        device = Device.open('/devices/dev2')
        lines = ['line_1', 'line_2', 'line_3']

        for line in lines:
            device.write_line(line)

        self.assertSequenceEqual(lines, [device.read_line() for _ in range(len(lines))])


if __name__ == '__main__':
    unittest.main()
