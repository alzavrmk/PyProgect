# Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.
from typing import List
import math


def check_is_prime_number(n: int) -> bool:
    n_prey = int(n) - 1
    factorial_n_prev = math.factorial(n_prey)
    if (factorial_n_prev + 1) % int(n) == 0:
        return True
    else:
        return False


def find_primes(n: int) -> List[int]:
    primes = []
    for num in range(2, n + 1):
        if not n % num and check_is_prime_number(num):
            primes.append(num)
    return primes


x = []
numb = int(input('Введите натуральное число: '))
x = find_primes(numb)
print(x)
