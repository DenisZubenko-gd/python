def my_upper_funk(my_str: str):
    """Делает все слова в строке с большой буквы
    :param my_str строка
    :return изменённая строка"""

    result = []
    my_list = my_str.split(' ')
    for word in my_list:
        first_simbol = word[0]
        result.append(word.replace(first_simbol, first_simbol.upper()))

    return ' '.join(result)


print(my_upper_funk('list if not strong'))

#Зачем придумывать велосипед, если в питон уже есть)
print('list if not strong'.title())