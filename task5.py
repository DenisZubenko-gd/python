"""Добавление значения в рейтинг"""

rating = [5, 4, 3, 3, 2]

new_value = int(input('Новое значение рейтинга: '))

#Сразу сделаем проверку на случай, если новое значение будем самым маленьким
if new_value < rating[-1]:
    rating.append(new_value)
else:
    #Для остальных значений сравниваем новое значение и вставляем в середину списка, сдвигая остальные значения
    for i, el in enumerate(rating):
        if new_value >= el:
            rating.insert(i, new_value)
            break

print(rating)