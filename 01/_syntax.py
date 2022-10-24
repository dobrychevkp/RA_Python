#!/usr/bin/env python3
# -*- coding: utf-8 -*-

number: int = 42

it_is_a_list: bool = True

value: object = [1, 2, 3, 8] if it_is_a_list else number

print(value)

text = "it's a string"

multi_line_text = '''
line_1
line_2
line_3
'''

# Это просто комментарий

a = 3 + 3  # Комментарии могут быть и тут


def user_info(name, age, city):
    """
    Возвращает информацию о пользователе.

    :param name: имя
    :param age: возраст в годах
    :param city: город
    """
    return name + ' ' + age + ', ' + city


