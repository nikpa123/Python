# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

import random
my_list = [random.randint(0,20) for _ in range(int(input('Укажите размер списка: ')))]
min_range = int(input("Введите минимальное число в диапазоне: "))
max_range = int(input("Введите максимальное число в диапазоне: "))
print(my_list)
final_list = []
for i in range(len(my_list)):
    if max_range >= my_list[i] >= min_range:
        final_list.append(i)
print(final_list)
