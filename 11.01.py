a = int(input("Введите первое число: "))

b = int(input("Введите второе число: "))

def sravneie (a,b):

    if a > b:
        return (a)
    else:
        return (b)


print(f'Наибольшее число:{sravneie(a,b)}')
