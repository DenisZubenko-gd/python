"""Запись в новый файл построчно данные, вводимые пользователем"""

with open('task_01.txt', 'w', encoding='UTF-8') as new_file:
    while True:
        new_line = input('Введите новую строку(для прекрящения записи введите пустую строку): ')
        if not new_line:
            print('Ввод закончен')
            break
        print(new_line, file=new_file)
    new_file.close()