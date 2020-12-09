"""Перевод секунд в 24 часовой формат"""

input_second = int(input('Введите количество секунд: '))

#Определяем количество часов и выделяем оставщиеся секунды
hours = input_second // (60 * 60)
input_second %= (60 * 60)

#Определяем количество минут и выделяем оставщиеся секунды
minutes = input_second // 60
input_second %= 60

print("%02i:%02i:%02i" % (hours, minutes, input_second))
