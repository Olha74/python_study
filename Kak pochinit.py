# Функция для задачи "Как это починить?"

def fix_it():
    print("Это двигается?")
    answer1 = input("Да или нет? ")
    if answer1 == "да":
        print("А должно?")
        answer2 = input("Да или нет? ")
        if answer2 == "да":
            print("Значит не трогай")
        else:
            print("Значит намотай изоленту")
    elif answer1 == "нет":
        print("А должно?")
        answer2 = input("Да или нет? ")
        if answer2 == "нет":
            print("Значит не трогай")
        else:
            print("Значит пшикни WD-40")



    else:
        print("А должно?")

# Вызываем функцию для выполнения задачи
fix_it()