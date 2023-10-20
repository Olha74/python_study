a = float(input("Vvedite chislo 1: "))
b = float(input("Vvedite chislo 2: "))
def summa(x,y):
    return x + y
k = summa(a,b)

def minus(x,y):
    return x - y
m = minus(a,b)
def multiplication(x,y):
    c = x*y
    print(c)
def division(x,y):
    d = x/y
    print(d)
print('Сумма:')
print(k)
print('Разница:')
print(m)
print('Произведение;')
multiplication(a,b)
print('Деление:')
division(a,b)
