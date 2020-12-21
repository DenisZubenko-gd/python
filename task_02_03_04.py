"""Несколько заданий я реализовал в одном модуле несколькими функциями"""


def task_02(my_list: list):
    """Возаращет элементы исходного списка, значения которых больше предыдущего элемента
    :param my_list список"""

    #Исключим сразу первый элемент
    return [el for el in my_list[1:] if el > my_list[my_list.index(el) - 1]]


def task_03(min_range, max_range, multiplicity1, multiplicity2):
    """Возвращает список из заданного диапозона, со значения кратным заданным значениям
    :param min_range минимальное
    :param max_range максимальное
    :param multiplicity1 кратность1
    :param multiplicity2 кратность 2"""

    return [el for el in range(min_range, max_range) if el % multiplicity1 == 0 or el % multiplicity2 == 0]

def task_04(my_list: list):
    """Возвращает список, исключая элементы, которых больше одного
    :param my_list список"""

    return [el for el in my_list if my_list.count(el) == 1]


print(task_02([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]))

print(task_03(20, 240, 20, 21))

print(task_04([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]))
