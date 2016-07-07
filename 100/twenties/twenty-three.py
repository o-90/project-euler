# -*- coding: utf-8 -*-

import time
from itertools import combinations_with_replacement


# 23)
# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors
# of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than
# n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123 can
# be written as the sum of two abundant numbers. However, this upper limit cannot
# be reduced any further by analysis even though it is known that the greatest
# number that cannot be expressed as the sum of two abundant numbers is less than
# this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of
# two abundant numbers.


def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def is_abundant(n):
    if sum(sorted(list(factors(n)))[:-1]) <= n:
        return False
    else:
        return True

abundants = [x for x in range(1, 28124) if is_abundant(x)]
ab_sum = list(set([sum(combos) for combos in combinations_with_replacement(abundants, 2)]))
ab_sum = [x for x in ab_sum if x < 28124]
ans = sum(set(range(1, 28124)).difference(set(ab_sum)))

print ans  # 4179871
