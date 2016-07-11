# -*- coding: utf-8 -*-

from math import factorial


# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial
# of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.


c = 0
facts = [factorial(x) for x in xrange(0, 10)]

for i in xrange(3, 100000):
    if i == sum(facts[int(d)] for d in str(i)):
        c += i

ans = c
print ans  # 40730
