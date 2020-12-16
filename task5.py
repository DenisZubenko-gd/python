def recursion_func(summ: int = 0):
    """Запрашивает ряд чисел через пробел, выводит сумму, запрашиавет ещё ряд чисел
    при вводе спецсимвола прекращает выполнение
    :param summ сумма предыдущего прохода"""

    nums = input('Введите числа: ')
    if not set(".,:;!_*-+()/#¤%&) ").isdisjoint(nums):
        pass
    else:
        nums = [int(x) for x in nums.split(' ')]
        summ += sum(nums)
        print(summ)
        recursion_func(summ)


recursion_func()
