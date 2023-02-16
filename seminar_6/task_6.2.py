"""
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""
from random import randint

a = int(input("Ведите нижнюю границу диапозона: "))
b = int(input("Введите верхнюю границу диапозона: "))
array_number = [randint(-10, 10) for i in range(20)]
print(array_number)
for i in range(20):
    if a <= array_number[i] <= b:
        print(f"{i} ", end='')