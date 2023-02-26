# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на
# вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
#
# *Пример:*
#
# ноутбук
#     12

a = input("Введите слово: ").lower()
sum = 0
dictionary = {'1': 'а в е и н о р с т a e i o u l n s t r', '2': 'д к л м п у d g', '3': 'б г ё ь я b c m p',
'4': 'й ы f h v w y', '5': 'ж з х ц ч k', '8': 'ш э ю j x', '10': 'ф щ ъ q z'}

for i in range(len(a)):
    if a[i] in dictionary['1']:
        sum += 1
    elif a[i] in dictionary['2']:
        sum += 2
    elif a[i] in dictionary['3']:
        sum += 3
    elif a[i] in dictionary['4']:
        sum += 4
    elif a[i] in dictionary['5']:
        sum += 5
    elif a[i] in dictionary['8']:
        sum += 8
    elif a[i] in dictionary['10']:
        sum += 10
print(sum)



