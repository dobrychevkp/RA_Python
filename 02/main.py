from devices.Device import *


if __name__ == '__main__':
    try:
        device: Device = open_device('/devices/dev5')

        for _ in range(3):
            print(read_line(device))
    except Exception as e:
        print(f'error: {e}')
