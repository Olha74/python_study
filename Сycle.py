m = str(input("Введите месяц своего рождения: "))
winter = ["декабрь", "январь", "февраль"]
spring = ["март", "апрель", "май"]
summer =["июнь","июль", "август"]
autumn =["сентябрь","октябрь", "ноябрь"]


def Jareszeit(month) -> list:

    month = month.lower()
    month = month.isalpha()
    if month in winter:
        print("Вы родились зимой")
    elif month in spring:
        print("Вы родились весной")
    elif month in summer:
        print("Вы родились летом")
    elif month in autumn:
        print("Вы родились осенью")
    else:
        print("Неверный месяц")
Jareszeit (m)

