"""записать программно набор чисел, разделенных пробелами.
Программа подсчитывает сумму чисел в файле и выводить ее на экран."""

with open('task_05.txt', 'w') as new_file:
    print(input('Введите числа через пробел: '), file=new_file)
    new_file.close()

with open('task_05.txt') as old_file:
    #С получением чисел перемудрил. Если так, то значит забыл переписать и отправил так)
    numbers = [int(number) for number in old_file.readline().split(' ')]
    print(f'Сумма этих чисел: {sum(numbers)}')
    old_file.close()