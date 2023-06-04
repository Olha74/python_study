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







