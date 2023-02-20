# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input("Введите размер массива: "))
list_1 = []
for i in range(n):
    list_1.append(i + 1)
print(list_1)
x = int(input("Введите число х: "))
diff1 = 0
a = x - list_1[0]
c = list_1[0]
for i in range(n):
    if x == list_1[i]:
        c = list_1[i]
        break
    else:
        diff1 = x - list_1[i]
        if x > list_1[i]:
            if diff1 < a:
                a = diff1
                c = list_1[i]
        else:
            if diff1 > a:
                a = diff1
                c = list_1[i]
print(c)


