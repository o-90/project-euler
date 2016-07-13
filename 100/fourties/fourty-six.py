# -*- coding: utf-8 -*-

import numpy as np
from math import floor, sqrt


# 46)
# It was proposed by Christian Goldbach that every odd composite number
# can be written as the sum of a prime and twice a square.
#
#     9  = 7 + 2×1^2
#     15 = 7 + 2×2^2
#     21 = 3 + 2×3^2
#     25 = 7 + 2×3^2
#     27 = 19 + 2×2^2
#     33 = 31 + 2×1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of
# a prime and twice a square?

# ----------------------------------------------------------------------------
# NOTE:  Essentially, we are looking for an odd composite that when a prime
# is subtracted from it and then divided by two, the remainder is not a
# perfect square.
# ----------------------------------------------------------------------------

def sundaram3(max_n):
    """
    get all the primes less than N
    """
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)

def is_perfect_square(n):
    """
    test if a number is a perfect square
    """
    return floor(sqrt(n)) == sqrt(n)

primes = sundaram3(10001)
odd_composites = sorted(list(set(x for x in range(35, 10003, 2)).difference(set(primes))))
primes = np.array(primes)

ans = 0
for oc in odd_composites:
    if not any(is_perfect_square((oc - ps)/2) for ps in primes[primes <= oc].tolist()):
        ans = oc
        break

print ans  # 5777
