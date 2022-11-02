import re
import sys

# NOTE: Библиотека для построения графиков. https://matplotlib.org/
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# NOTE: Двухсторонняя очередь (deque). https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque

# NOTE: Sequence как расширенный Iterable. https://docs.python.org/3/glossary.html#term-sequence
from typing import Sequence, Tuple


class PingParser(object):
    # NOTE: Шаблон вывода утилиты ping.
    __pattern = r'^64 bytes from (.*): icmp_seq=(\d+) ttl=\d+ time=(\d+.\d) ms$'

    # NOTE: Будем показывать не более 50-ти последних измерений.
    __results = deque(maxlen=50)

    host = str()

    @classmethod
    def parse(cls) -> Sequence[Tuple[int, float]]:
        while True:
            # NOTE: Читаем строку из stdin.
            line = sys.stdin.readline()

            # NOTE: Пишем считанную строку в stdout.
            sys.stdout.write(line)

            # NOTE: Проверяем строку на соответствие шаблону регулярного выражения.
            match = re.search(cls.__pattern, line.strip())

            # NOTE: В случае совпадения извлекаем нужные значения из соответствующих групп.
            if match:
                cls.host = match.group(1)

                package = int(match.group(2))
                time = float(match.group(3))
                cls.__results.append((package, time))

                return cls.__results


if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # NOTE: Перерисовываем график с очередной порцией данных.
    def animate(_):
        xs = []
        ys = []

        data = PingParser.parse()

        for x, y in data:
            xs.append(x)
            ys.append(y)

        ax.clear()
        ax.plot(xs, ys)

        plt.title(PingParser.host)
        plt.xlabel('Package')
        plt.ylabel('Time (ms)')

    _ = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()
