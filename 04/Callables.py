# NOTE: Callable. https://docs.python.org/3/library/typing.html#callable
from typing import Any, Callable, Iterable, List


# NOTE: Декоратор принимает оригинальную функцию и возвращает декорированную.
def debug(func: Callable) -> Callable:
    """Декоратор, добавляющий отладочную информацию о вызове функции."""

    # NOTE: Создаём функцию-обёртку, которую потом и вернём.
    def wrapper(*args, **kwargs) -> Callable:
        # NOTE: Внедряем вывод отладочной информации
        print(f'Call: {func} with {len(args) + len(kwargs)} args')

        # NOTE: Вызываем оригинальную функцию.
        return func(*args, **kwargs)

    return wrapper


# NOTE: Обычная функция - Callable.
def f_sum(a: float, b: float) -> float:
    return a + b


# NOTE: λ-функция (анонимная однострочная функция) - Callable.
l_sum = lambda a, b: a + b


class Sum(object):
    def __call__(self, a: float, b: float) -> float:
        return a + b


# NOTE: Объект класса с переопределённым методом __call__() - Callable.
o_sum = Sum()


def partial_apply(x: Any, func: Callable) -> Callable:
    """Частично применяет функцию func."""
    # NOTE: Фиксируем первый аргумент как x, возвращаем функцию f(x0..xn-1) вместо f(x0..xn))
    return lambda *args, **kwargs: func(x, *args, **kwargs)


# NOTE: Callable c сохранением истории вызовов.
class Sqr(object):
    def __init__(self):
        self.__calls_history = []

    @property
    def calls_history(self) -> List[str]:
        return self.__calls_history

    def __call__(self, x: float) -> float:
        result = x ** 2

        self.__calls_history.append(f'{x} ** 2 = {result}')

        return result


# NOTE: Пример функции высшего порядка (может принимать и/или возвращать другие функции).
def for_each(iterable: Iterable, func):
    for value in iterable:
        func(value)

    return func


if __name__ == '__main__':
    sqr_with_history: Sqr = for_each(range(10), Sqr())
    print(sqr_with_history.calls_history)
