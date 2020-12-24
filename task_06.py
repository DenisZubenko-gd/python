"""Сформировать словарь, содержащий название предмета и общее количество занятий по нему"""

my_dict = dict()
with open('task_06.txt', encoding='UTF-8') as old_file:

    for line in old_file:
        #Переделываем строку в кортеж
        info = line.split(' ')
        #Проходим по всем занятиям выделяя число и суммируем их
        works = 0
        for work in info[1:]:
            #Исключим отсутвие работ
            if work != '—':
                works = works + int(work[:work.find('(')])

        my_dict[info[0][:-1]] = works

    old_file.close()
print(my_dict)