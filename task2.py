#Возможно я не так понял задание. Функция которая принимает информацию о пользователе и выводит одной строкой
#Хотя через kwargs было бы логичнее
def print_user_info(firstname: str, surname: str, year_of_birth: int,
                    city: str, email: str, phone: str):
    """Выводит информацию о пользователе на экран
    :param firstname имя
    :param surname фамилия
    :param year_of_birth год рождения
    :param city город
    :param email емаил
    :param phone телефон"""

    print(f"Имя: {firstname}. Фамилия: {surname}. Год рождения: {year_of_birth}. Город проживания: {city}. "
          f"email: {email}. Телефон: {phone}")


print_user_info(surname='Иванов', email='aaa@mail.ru', firstname='Иван', phone='+79994443355',
                year_of_birth=1900, city='Ситиград')
