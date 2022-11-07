import subprocess


class Desktop(object):
    __notifier_util = 'notify-send'
    __xsel_util = 'xsel'

    @classmethod
    def send_notification(cls, title: str, body: str):
        subprocess.call((cls.__notifier_util, title, body))

    @classmethod
    def get_selection(cls) -> str:
        return subprocess.check_output([cls.__xsel_util, '-o']).decode()
