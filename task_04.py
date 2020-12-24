"""английские числительные заменяются на русские"""
numbers = {'One': 'Один',
           'Two': 'Два',
           'Three': 'Три',
           'Four': 'Четыре'}

with open('task_04_01.txt', 'r', encoding='UTF-8') as old_file:
    with open('task_04_02.txt', 'w', encoding='UTF-8') as new_file:
        for line in old_file:
            old_number = line.split(' ')[0]
            new_line = line.replace(old_number, numbers[old_number])
            print(new_line, file=new_file)
        new_file.close()
    old_file.close()