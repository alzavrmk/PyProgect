# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

from random import randint

nams_i = []
set1 = set()
for i in range(20):
    nams_i.append(randint(1, 9))
    set1.add(nams_i[i])
print(nams_i)
print(set1)
