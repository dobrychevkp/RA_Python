# NOTE: Модуль для запуска сторонних процессов. https://docs.python.org/3/library/subprocess.html
import subprocess


class Desktop(object):
    # NOTE: Утилита рассылки уведомлений на рабочий стол. https://manpages.org/notify-send
    __notifier_util = 'notify-send'

    # NOTE: Утилита захвата выделенного текста. https://manpages.org/xsel
    __xsel_util = 'xsel'

    @classmethod
    def send_notification(cls, title, body):
        """Посылает уведомление на рабочий стол."""
        subprocess.call((cls.__notifier_util, title, body))

    @classmethod
    def get_selection(cls) -> str:
        """Возвращает выделенный в текущем окне текст."""
        return subprocess.check_output([cls.__xsel_util, '-o']).decode()


if __name__ == '__main__':
    Desktop.send_notification('Title', Desktop.get_selection())
