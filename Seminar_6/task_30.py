# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го
# члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность элементов: "))
n = int(input("Введите количество элементов прогрессии: "))
list_1 = []
for i in range(1, n + 1):
    list_1.append(a1 + (i - 1) * d)
print(list_1)