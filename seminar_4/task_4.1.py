"""Вычислить число c заданной точностью d
Пример: при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$"""
import math
from decimal import Decimal


def calc_pi(epsilon):
    n = 2
    pi = 4 * [1, -1 / 3]
    dif = 1
    if dif > epsilon:
        pi.append(4 * (-1) ** n / (2 * n + 1))
        dif = abs(sum(pi[:-1]) - sum(pi[:-2]))
        n += 1
    return math.floor(sum(pi) * int(1/epsilon))*epsilon


f = calc_pi(0.0001)
print(f)


def gauss_Pi(d):
    accuracy = 1
    Gauss_pi = 48 * math.atan(1 / 18) + 32 * math.atan(
        1 / 57) + 20 * math.atan(1 / 239)
    number_of_digits = int(len(str(d).split(".")[1]))
    print(number_of_digits)
    while (number_of_digits) > 0:
        accuracy *= 10
        number_of_digits -= 1
    return int(Gauss_pi * accuracy) / accuracy


pi_1 = gauss_Pi(0.0001)
print(pi_1)
