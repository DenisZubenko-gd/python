"""Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников"""

#Считал данные из файла и записал в словарь, чтобы потом с ним работать
staff = dict()
with open('task_03.txt', 'r', encoding='UTF-8') as old_file:
    for line in old_file:
        list_staff = line.split(' ')
        staff[list_staff[0]] = int(list_staff[1])
    old_file.close()

wages = []
print('Сотрудники с зарплата меньше 20 тыс. руб:')
for key, valie in staff.items():
    if valie < 20000:
        print(key)
    wages.append(valie)

average_wage = round(sum(wages, 0.0) / len(wages), 2)
print(f'Средняя зарплата по всем сотрудникам: {average_wage}')
