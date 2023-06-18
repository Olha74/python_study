a: None = None  # неопределенное значение

# Numeric Type
i: int = 1  # integer целое число
f: float = 2.5  # float число с запятой

# Text Sequence Type
s: str = 'Hallo'  # string строка

# Boolean Type - True/ False
b1: bool = True
b2: bool = False

# Sequence Type
l: list = [1, 2, 'Olha', True, False]  # Это список. У одной переменной может быть много значений. Например, кто давал Путьке
t: tuple = (1, 2, 'Olha', True, False)  # Кортеж. Нельзя изменять. Есть и все...

# Set Types
se: set = {1, 2, 'Olha', True, False}  # Наз. Множество. Тоже, что и лист. Но,содержит только уникальные значения
fr: frozenset = {1, 2, 'Olha', True, False}  # Тоже самое, что и множество, но нельзя изменять. Как отличается кортеж от списка

# Mapping Types
d: dict = {'a': 1, 'b': 2}  # Это словарь. Структра - ключ:значение

x = 2
y = 3
result = (x+y)**2
print(result)

h = 10
abc = 5
result = h + abc
print(result)
result = h - abc

print(result)
my_list = [1, 2.5, True, "Hello", [1, 2, 3], (4, 5, 6), {"name": "Olha", "age": 48}, {"Olha", "Valentin", "Andrii"}, None]
print(my_list)

my_dict = {
    "integer": 100,
    "float": 3.8,
    "boolean": False,
    "string": "Hallo",
    "list": [1, 2, 3, 4, 5],
    "tuple": (6, 7, 8),
    "dictionary": {"name": "Olha", "age": 49},
    "set": {"Olha", "Valentin", "Andrii"},
    "none": None
}
print(my_dict)

my_string = "Number: " + str(10)  # конкатенация строк и преобразование целого числа в строку
print(my_string)

my_integer = 10  # Использование форматирования строк (F-string). мы использовали префикс "f" перед строкой,
# а затем поместили фигурные скобки "{}" для вставки значения переменной "my_integer" внутри строки.
my_string = f"Number: {my_integer}"
print(my_string)

z = 5

if z > 0:
    print("z положительное число")
elif z < 0:
    print("z отрицательное число")
else:
    print("z равно нулю")


m = 5
n = 5


def compare_numbers(n, m):
    if n > m:
        print(f"{n} больше, чем {m}")
    elif n < m:
        print(f"{n} меньше, чем{m}")
    else:
        print(f"{m} равно {n}")


compare_numbers(m, n)


q = 49
w = 49
e = 20
r = 10
t = 50


def compare_sister(q, w, e, r, t,):
    if q > w and e > r or e > t:
        print("Лена старше Оли")
    elif q < w and e > r or e > t:
        print("Оля младше Лены")
    elif q == w:
        print("Это незнакомец")


compare_sister(q, w, e, r, t, )

def kto_est_kto(q, w, e, r, t):
    if q-w ==4 or e > r:
        print("Это семья Богаченко")
    elif  q-w != 4 and r > e or t >e:
        print("Это семья Короп")
    else:
        print("Незнакомец")
kto_est_kto(q, w, e, r, t,)



















