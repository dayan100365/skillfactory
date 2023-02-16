''''
Вам дан словарь per_cent с распределением процентных ставок по вкладам в различных банках таким образом,
что ключ — название банка, значение — процент. Напишите программу, в результате которой будет сформирован
список deposit значений — накопленные средства за год вклада в каждом из банков. На вход программы с клавиатуры вводится
сумма money, которую человек планирует положить под проценты.

Для самостоятельного изучения вам была дана ссылка на методы для работы со списками. Изучите методы и найдите тот,
который позволяет найти максимальное значение среди элементов в списке.

 Добавьте в программу поиск максимального значения и его вывод на экран в формате:

 Максимальная сумма, которую вы можете заработать — deposit[i]

Где вместо deposit[i] будет выведено максимальное значение списка.

Для проверки загрузите полученное решение на GitHub и прикрепите ссылку.

При оценивании вы можете получить 3 балла за верное выполнение первой части задания и 4 балла, если выполните вторую часть.
'''
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}


def get_max_deposit():
    money_client = int(input(f" Введите сумму, которую хотите вложить(целое число): "))
    deposit = []


    for value in per_cent.values():
        deposit.append((money_client * value) / 100)

    print(f" Максимальная сумма, которую вы можете заработать - {max(deposit)} ")


client = get_max_deposit()
print(client)