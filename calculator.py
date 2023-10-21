a = int(input("Vvedite chislo 1: "))
b = int(input("Vvedite chislo 2: "))


def summa(x: int, y: int) -> int:
    return x + y


print(f'Cумма: {summa(a, b)}')


def minus(x: int,y: int) -> int:
    return x - y


print(f'Разница: {minus(a, b)}')


def multiplication(x: int, y: int) -> None:
    print(f'Произведение: {x * y}')


def division(x: int, y: int) -> None:
    print(f'деление: {x/y}')


multiplication(a, b)
division(a, b)





