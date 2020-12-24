"""словарь с фирмами и их прибылями, а также словарь со средней прибылью"""

import json

#Задал все нужные списки и словари
profits = list()
damages = list()
profit_firm = dict()
damages_firm = dict()

with open('task_07.txt', encoding='UTF-8') as old_file:
    for line in old_file:
        info_firm = line.split(" ")

        #Определил прыбиль или убыток и добавил информацию в соответвующий словрь
        profit = int(info_firm[2]) - int(info_firm[3])
        if profit >= 0:
            profits.append(profit)
            profit_firm[info_firm[0]] = profit
        else:
            damages.append(profit)
            damages_firm[info_firm[0]] = abs(profit)
    old_file.close()

#Подсчитал среднию прибыль
average_profit = {"average_profit": round(sum(profits) / len(profits), 2)}

with open('task_07.json', 'w') as new_file:
    json.dump([profit_firm, #Фирмы с прибылью
               average_profit, #Средняя прибыль
               damages_firm], #Фирмы с убытками
              new_file)
    new_file.close()
