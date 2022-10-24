from math import *


def _sum(a, b):
    return a + b


def f(x: float) -> float:
    return _sum(3, x) * exp(10) + sin(34)


def _fib(max_value: int):
    a, b = 0, 1

    while a <= max_value:
        print(a)
        a, b = b, a + b


# NOTE: Функция-генератор. Может сохранять своё состояние между вызовами.
def _fib_gen():
    a, b = 0, 1

    # NOTE: Вот тут вернём a выйдем из функции.
    yield a

    # NOTE: При повторном вызове продолжим отсюда. (Вернём b и выйдем и т.д).
    yield b

    while True:
        a, b = b, a + b
        yield b


if __name__ == '__main__':
    # NOTE: λ-функция (безымянная функция, которая может быть использована сразу же на месте объявления).
    _f = lambda x: _sum(3, x) * exp(10) + sin(34)
    assert f(23.09) == _f(23.09)

    _fib(2000)

    gen = _fib_gen()

    for n in gen:
        print(n)
