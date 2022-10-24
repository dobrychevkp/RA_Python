number = int(input('input a number: '))
if number % 2 == 0:
    print("it's a even number")
else:
    print("it's a odd number")

print(f"it's a {'even' if number % 2 == 0 else 'odd'} number")

if number < 10:
    print('too small!')
elif number < 100:
    print('suitable')
elif number < 500:
    print("too big")
else:
    raise ValueError('prohibitively large number')

while int(input('input a number: ')) % 2 == 0:
    print('once again...')

print("done")

for x in [1, 2, 3, 4, 5]:
    print(x * x)
    print(x ** 3)
    print('--')

# NOTE: Печатаем квадраты чисел от 0 до 9.
for x in range(10):
    print(x * x)

for x in [1, 201, 3, 7, 4, 5]:
    if x % 2 == 0:
        print('found an even number in the list')

        if x == 20:
            print('but it is 20')
            continue    # NOTE: Переход на следующую итерацию цикла.

        break   # NOTE: Выход из цикла.

    print(x)
else:
    print('all of them are odd')


names = ['Alice', 'Bob', 'Carlos', 'David', 'Eva']

# NOTE: Генератор списка (Не путать с просто генераторами!). Пишем код наполнения списка прямо внутри [].
transformed_names = [name.upper() for name in names if len(name) > 3]
print(transformed_names)

# NOTE: А это генератор. Очень похоже на список выше, но полученная коллекция вычисляется по мере итерации по ней.
transformed_names_gen = (name.upper() for name in names if len(name) > 3)
