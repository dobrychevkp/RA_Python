from devices.Device import *


if __name__ == '__main__':
    try:
        device: Device = Device.open('/devices/dev3')

        for i in range(3):
            print(device.read_line())

    except Exception as exception:
        print(f'Error: {exception}')
