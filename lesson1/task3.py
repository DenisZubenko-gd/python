"""Суммирование чисел"""

number = input('Введите число: ')

term1 = int(number)
term2 = int(number+number)
term3 = int(number+number+number)

result_summ = term1 + term2 + term3

print(f"{term1}+{term2}+{term3} = {result_summ}")