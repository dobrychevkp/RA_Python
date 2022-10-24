# NOTE: Пустой тип. https://docs.python.org/3/library/constants.html#None
var = None

# NOTE: Булев тип. https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
isCat: bool = True
isDog = False

isAnimal = isCat or isDog

# NOTE: Числа. https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
a: int = -1
b: float = 19.6676e-15
c: complex = 19 + 12j
print(c.imag, c.real)

d = a + b * 12 / 3
print(d)

# NOTE: Деление целых чисел.
print(9 / 7)
print(9 // 7)
print(9 % 7)

bin_var = 0b101
oct_var = 0o066
hex_var = 0xff

# NOTE: Строки. https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
string: str = 'just a string'
print(string)

multi_line_text = 'line_1\nline_2\nline_3'
print(multi_line_text)

raw_string = r'line_1\nline_2\nline_3'
print(raw_string)

# NOTE: Списки. https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
numbers: list = [1, 2, 3, 5, 6]
users = ['Alice', 'Bob', 'Carlos']
things = [1, True, 'Text', None, [1, 2, 3]]

numbers += [34, 35, 35]
print(numbers)
print(len(numbers))
print(numbers[2])
print(numbers[-2])
print(numbers[1:3], numbers[2:-2])

# NOTE: Кортежи. https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
location = (56.484640, 84.947649, 'Tomsk')
print(location)

# NOTE: Распаковка кортежа.
latitude, longitude, label = location
assert latitude == 56.484640
assert longitude == 84.947649
assert label == 'Tomsk'

# NOTE: Словари. https://docs.python.org/3/tutorial/datastructures.html#dictionaries
location = {
    'latitude': 56.484640,
    'longitude': 84.947649,
    'label': 'Tomsk',
}

print(location)

assert location['latitude'] == 56.484640
assert location['longitude'] == 84.947649
assert location['label'] == 'Tomsk'

location['label'] = 'Tomsk, Russia'
location['population'] = 500_000
print(location)

del location['label']
print(location)
