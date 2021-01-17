"""Здесь происходит возов методов склада, для проверки работы"""

from task4_6.warehouse import Warehouse

# Создаём склады
warehouse1 = Warehouse('Склад1')
warehouse2 = Warehouse('Склад2')

# Заполняем склады
warehouse1.acceptance_of_goods('Мышь', 3)
warehouse1.acceptance_of_goods('Клавиатура', 5)
warehouse1.acceptance_of_goods('Принтер', '1')  # Проверка валидации количество
print(warehouse1)
warehouse2.acceptance_of_goods('Монитор', 1)
warehouse2.acceptance_of_goods('Клавиатура', 3)
warehouse2.acceptance_of_goods('Системный блок', 10)
print(warehouse2)

# Перемещем товар между складами
Warehouse.moving(warehouse1, warehouse2, 'Мышь', 4)  # Проверяем валидация отрицательного остатка
print(warehouse1)
print(warehouse2)
Warehouse.moving(warehouse2, warehouse1, 'Монитор', 1)  # Проверяем нулевой остаток, создание и удаления позиций на складе
print(warehouse1)
print(warehouse2)
Warehouse.moving(warehouse2, warehouse1, 'Клавиатура', 2)  # Обычное перемещение
print(warehouse1)
print(warehouse2)
