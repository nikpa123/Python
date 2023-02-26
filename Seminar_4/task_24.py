# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 8 2 3 4 5
# 9

a = int(input("Введите количество кустов: "))
list_1 = list()
for i in range(a):
    list_1.append(int(input()))
print(list_1)
sum = 0
max = 0
for i in range(a):
    if i + 2 == a:
        sum = list_1[i] + list_1[i+1] + list_1[0]
        if sum > max:
            max = sum
    elif i + 1 == a:
        sum = list_1[i] + list_1[0] + list_1[1]
        if sum > max:
            max = sum
    else:
        sum = list_1[i] + list_1[i + 1] + list_1[i + 2]
        if sum > max:
            max = sum
print(max)
