import time

from multiprocessing import current_process

# NOTE: Модуль работы с потоками. https://docs.python.org/3/library/threading.html
from threading import Thread, Lock, current_thread


class Task(object):
    def __init__(self):
        self.__is_running = False

    @property
    def __pid(self):
        return current_process().pid

    @property
    def __tid(self):
        return current_thread().native_id

    @property
    def __thread_name(self):
        return current_thread().name

    # NOTE: Оформляем задачу как Callable.
    def __call__(self, name: str):
        print(f'Task "{name}" started')
        self.__is_running = True

        while self.__is_running:
            # NOTE: Захватываем блокировку, чтобы предотвратить одновременный доступ к ресурсу (stdout).
            with lock:
                print(f'{self.__thread_name}. task: {name}, pid: {self.__pid}, tid: {self.__tid}')

            time.sleep(2)

        print(f'Task "{name}" stopped')

    def cancel(self):
        self.__is_running = False


if __name__ == '__main__':
    lock = Lock()
    tasks = [Task() for _ in range(4)]

    # NOTE: Формируем задачи для запуска в отдельных потоках.
    threads = [Thread(target=task, args=(f'Task_{index}',)) for index, task in enumerate(tasks)]

    try:
        for thread in threads:
            # NOTE: Запускаем потоки.
            thread.start()

        for thread in threads:
            # NOTE: Ожидаем завершения потоков с задачами.
            thread.join()
    except KeyboardInterrupt:
        for task in tasks:
            task.cancel()
