# -*- coding: utf-8 -*-

from math import sqrt, floor
from fractions import gcd


# 64)
# All square roots are periodic when written as continued fractions and can
# be written in the form:
# It can be seen that the sequence is repeating. For conciseness, we use the
# notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.
#
# The first ten continued fraction representations of (irrational) square
# roots are:
#
#     √2=[1;(2)], period=1
#     √3=[1;(1,2)], period=2
#     √5=[2;(4)], period=1
#     √6=[2;(2,4)], period=2
#     √7=[2;(1,1,1,4)], period=4
#     √8=[2;(1,4)], period=2
#     √10=[3;(6)], period=1
#     √11=[3;(3,6)], period=2
#     √12= [3;(2,6)], period=2
#     √13=[3;(1,1,1,1,6)], period=5
#
# Exactly four continued fractions, for N ≤ 13, have an odd period.
# How many continued fractions for N ≤ 10000 have an odd period?


def find_period(N):
    """
    finds the continued fraction representations
    of irrational square roots
    """
    # initialize
    a_0 = int(floor(sqrt(N)))
    denominator = 1
    a = a_0
    k = 0
    b = 1

    ans = []

    while True:
        k = (a * denominator) - k
        numerator = sqrt(N) + k
        denominator = (N - k*k) / gcd(N - k*k, b)
        a = int(floor(numerator / denominator))
        b = denominator
        ans.append(a)

        if k == a_0 and b == 1:
            break

    return ans

# don't have to check perfect squares
squares = {x*x: True for x in xrange(101)}
test_nums = [x for x in xrange(10001) if not squares.get(x, False)]

ans = sum([1 for x in test_nums if len(find_period(x)) % 2 == 1])
print ans  # 1322
