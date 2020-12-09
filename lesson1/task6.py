"""Расчет количество дней на тренировки"""

today_km = int(input('Сколько вы пробегаете сейчас? '))
target = int(input('Сколько хотите пробегать за день? '))

days = 1
print(f'{days} день. Вы пробежали {today_km} км')
while today_km < target:
    today_km = round(today_km + (today_km / 100 * 10), 2)
    days += 1
    print(f'{days} день. Вы пробежали {today_km} км')

print(f'Вы достигнете своей цели в {target} км за {days} дней')
