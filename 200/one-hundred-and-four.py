# -*- coding: utf-8 -*-


from itertools import permutations
from collections import defaultdict


# 104)
# The Fibonacci sequence is defined by the recurrence relation:
#    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#
# It turns out that F541, which contains 113 digits, is the first
# Fibonacci number for which the last nine digits are 1-9 pandigital
# (contain all the digits 1 to 9, but not necessarily in order). And F2749,
# which contains 575 digits, is the first Fibonacci number for which the
# first nine digits are 1-9 pandigital.  Given that Fk is the first Fibonacci
# number for which the first nine digits AND the last nine digits
# are 1-9 pandigital, find k.


d = defaultdit(int)

for ps in permutations(range(1, 10)):
    d[int("".join(str(x) for x in ps))] += 1

a, b = 0, 1

for k in xrange(1000000):
    # check progress
    if (k + 1) % 10000 == 0:
        print "@ iter := {}".format(k+1)

    a, b = b, a + b
    if a % 1000000000 in d:
        if int(str(a)[::-1]) % 1000000000 in d:
            print k + 1
            break


