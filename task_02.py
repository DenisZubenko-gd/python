"""Подсчет количества строк в файле, количества слов в каждой строке"""

with open('task_02.txt', 'r', encoding='UTF-8') as old_file:
    lines_in_file = old_file.readlines()
    old_file.close()

print(f'Кол-во строк: {len(lines_in_file)}')
for line in lines_in_file:
    number_line = lines_in_file.index(line) + 1
    print(f'Строка {number_line} - кол-во слов {len(line.split(" "))}')