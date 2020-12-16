def my_func(num1: int, num2: int, num3: int):
    """Суммирует два наибольших чисел из трёх принимаемых
    :param num1 число1
    :param num2 число2
    :param num3 число3
    :return result сумма"""

    # При желании можно одной строкой всё реализовать, но я решил немного размазать для читаемости
    nums = [num1, num2, num3]
    nums.remove(min(nums))
    result = sum(nums)

    return result


my_func(34, 2, 56)