import time

# NOTE: Модуль работы с процессами. https://docs.python.org/3/library/multiprocessing.html
from multiprocessing import Lock, Process, current_process


# NOTE: Обратите внимание на сходство с похожим примером с потоками.
class Task(object):
    @property
    def __pid(self):
        return current_process().pid

    @property
    def __process_name(self):
        return current_process().name

    def __call__(self, name: str, lock: Lock()):
        print(f'Task "{name}" started')

        # NOTE: Поскольку задача - отдельный процесс, обрабатываем KeyboardInterrupt в каждой из них.
        try:
            while True:
                with lock:
                    print(f'{self.__process_name}. task: {name}, pid: {self.__pid}')

                time.sleep(2)
        except KeyboardInterrupt:
            pass

        print(f'Task "{name}" stopped')


if __name__ == '__main__':
    _lock = Lock()
    tasks = [Task() for _ in range(4)]

    # NOTE: Формируем задачи для запуска в отдельных процессах.
    # WARNING: Блокировку передаём как параметр в задач, ибо у каждого процесса своё адресное пространство памяти.
    processes = [Process(target=task, args=(f'Task_{index}', _lock)) for index, task in enumerate(tasks)]

    try:
        for process in processes:
            process.start()

        for process in processes:
            process.join()
    except KeyboardInterrupt:
        pass


