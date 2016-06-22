# -*- coding: utf-8 -*-

from math import factorial


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
