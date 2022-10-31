import io
import time
import sys

# NOTE: Для захвата изображений с камеры будем использовать OpenCV. https://opencv.org/
import cv2

from abc import abstractmethod
from typing import Tuple

# NOTE: Для захвата изображений с рабочего стола будем использовать Pillow. https://pillow.readthedocs.io/en/latest/
from PIL import Image, ImageGrab


class AbstractFrameGenerator(object):
    """Абстрактный генератор изображений."""

    def __init__(self, fps: int = 24):
        self.__fps = fps

    def __iter__(self):
        return self

    def __next__(self):
        # NOTE: Выдерживаем нужную нам паузу перед генерацией нового кадра.
        time.sleep(1 / float(self.__fps))

        if frame := self._generate_next_frame():
            return frame
        else:
            print("Can't read frame.")
            sys.exit(1)

    @abstractmethod
    def _generate_next_frame(self) -> bytes | None:
        raise NotImplementedError


class DesktopFrameGenerator(AbstractFrameGenerator):
    """Генератор изображений с захваченной области рабочего стола."""

    def __init__(self, box: Tuple[int, int, int, int], fps: int = 24):
        super().__init__(fps)
        self.__box = box

    def _generate_next_frame(self) -> bytes | None:
        return self.__to_jpeg(ImageGrab.grab(self.__box))

    @staticmethod
    def __to_jpeg(image: Image) -> bytes:
        buffer = io.BytesIO()
        image.save(buffer, format='JPEG')
        return buffer.getvalue()


class CameraFrameGenerator(AbstractFrameGenerator):
    """Генератор изображений с камеры."""

    def __init__(self, index: int = -1, fps: int = 24):
        super().__init__(fps)
        self.__capture = cv2.VideoCapture(index)

    def _generate_next_frame(self) -> bytes | None:
        success, data = self.__capture.read()
        if success:
            success, jpeg = cv2.imencode('.jpg', data)
            if success:
                return jpeg.tobytes()

        return None


if __name__ == '__main__':
    frame_generator = DesktopFrameGenerator(box=(10, 10, 810, 810))

    # NOTE: В цикле for получаем из генератора набор изображений кадр за кадром и сохраняем их.
    for i, f in enumerate(frame_generator):
        with open(f'frames/frame_{i}.jpg', 'wb') as file:
            file.write(f)
