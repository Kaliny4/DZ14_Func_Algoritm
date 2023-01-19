"""
Написать программу которая состоит из вечного цикла ожидающего ввод числа или
одно из значений: "выход", "exit", "quit", "e" или "q" в любом регистре.
При вводе одного из этих значений происходит выход из вечного цикла.
При любом другом вводе вызывается отдельная функция которая умеет распознавать введённые числа.
Сама функция ничего не распечатывает, она возвращает строку, типа:
"Вы ввели отрицательное дробное число: -6.7" или "Вы ввели не корректное число: Erdf"
Затем в цикле выводится это сообщение и цикл начинается заново ожидая следующего ввода.
Функция на вход принимает строку из ввода из вечного цикла.
Анали-.77зирует её исключительно методом .isdigit() и другими методами строк, без доп.библиотек
и переводит строку в число, если это возможно.
Функция умеет распознавать отрицательные числа и десятичные дроби,
а так же распознаёт десятичные дроби как с точкой, так и с запятой.
Функция возвращает строку в которой описывается какое число введено -
отрицательное или положительно, целое или дробное и выводит его или же сообщает,
что введено не корректное число.
*Дополнительно: правильно распознаётся десятичная дробь без первого значащего нуля

Примеры:
0 → Вы ввели ноль
-6,7 → Вы ввели отрицательное дробное число: -6.7
5 → Вы ввели - целое число: 5
5.4r → Вы ввели не корректное число: 5.4r
7 → Вы ввели отрицательное дробное число: -0.777
.000 → Вы ввели ноль
5.49.3 → Вы ввели не корректное число: 5.49.3
--.49 → Вы ввели не корректное число: --.49

"""


def func_num(k):
    if k.count('-') == 1 and k.find('.') == -1 and k.find(',') == -1:
        k = int(k)
        return 'Вы ввели отрицательное целое число: ', k
    elif k.isdigit():
        k = int(k)
        if k == 0:
            return 'Вы ввели ноль'
        elif k > 0:
            return 'Вы ввели положительное целое число: ', k
    elif k.count('.') == 1 and k.find(',') == -1 and k.count('-') == 1:
        return 'Вы ввели отрицательное дробное число: ', k
    elif k.count('.') == 1 and k.find(',') == -1 and k.count('-') == 0:
        k = float(k)
        if k > 0:
            return 'Вы ввели положительное дробное число: ', k
        elif k == 0:
            return 'Вы ввели ноль'
    elif k.count(',') == 1 and k.find('.') == -1 and k.count('-') == 1:
        return 'Вы ввели отрицательное дробное число: ', k
    elif k.count(',') == 1 and k.find('.') == -1 and k.count('-') == 0:
        return 'Вы ввели положительное дробное число: ', k
    else:
        return 'Вы ввели не корректное число: ', k


def name_number():
    while True:
        n = input('Ввести число n или Желаете выйти? ("выход", "exit", "quit", "e" или "q"): ')
        if n.lower() in ('выход', 'exit', 'quit', 'e', 'q'):
            break
        else:
            print(func_num(n))


name_number()


