# -*- coding: utf-8 -*-

from math import factorial


# 53)
# There are exactly ten ways of selecting three from five, 12345:
#
#     123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
# In combinatorics, we use the notation, 5C3 = 10.
#
# In general,
#
#    nCr =
#    n!nCr
#    r!(n−r)! ,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
#
# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
# How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100,
# are greater than one-million?


def n_choose_k(n, k):
    """
    """
    return factorial(n) / (factorial(k) * factorial(n - k))

ans = 0

for i in xrange(1, 101):
    for j in xrange(1, i):
        if n_choose_k(i, j) > 1000000:
            ans += 1

print ans  # 4075
