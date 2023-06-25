# Функция для задачи "Как это починить?"

def fix_it():
    print("Это двигается?")
    answer1 = input("да или нет? ").lower()
    if answer1 == "да" or answer1 == "нет":
        if answer1 == "да":
            print("А должно?")
            answer2 = input("да или нет? ").lower()
            if answer2 == "да" or answer2 == "нет":
                if answer2 == "да":
                    print("Значит не трогай")
                else:
                    print("Значит намотай изоленту")
            else:
                print("Введите корректные данные")
        elif answer1 == "нет":
            print("А должно?")
            answer2 = input("да или нет? ").lower()
            if answer2 == "да" or answer2 == "нет":
                if answer2 == "нет":
                    print("Значит не трогай")
                else:
                    print("Значит пшикни WD-40")
            else:
                print("Введите корректные данные")
    else:
        print("Введите корректные данные")








# Вызываем функцию для выполнения задачи
fix_it()