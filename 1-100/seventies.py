# -*- coding: utf-8 -*-


import time
from math import factorial, floor
from collections import OrderedDict, defaultdict

# 70)


# 71)
# Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1,
# it is called a reduced proper fraction.  If we list the set of reduced proper fractions
# for d ≤ 8 in ascending order of size, we get:
#    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
# It can be seen that 2/5 is the fraction immediately to the left of 3/7.
# By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size,
# find the numerator of the fraction immediately to the left of 3/7.
a = 2
b = 5

for i in range(100, 1000000):
    tmp = defaultdict(str)
    for j in range(int(floor(i*a/b)), int(floor(3*i/7))):
        tmp[j / i] += str(j) + '/' + str(i)

    d = OrderedDict(sorted(tmp.items()))
    str_ = d[d.keys()[-1]]
    a, b = str_.split('/')
    a, b = int(a), int(b)

# ans: 428570

# 72)
# 73)


# 74)
# The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
#    1! + 4! + 5! = 1 + 24 + 120 = 145
# Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns ou$
#    169 → 363601 → 1454 → 169
#    871 → 45361 → 871
#    872 → 45362 → 872
# It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
#    69 → 363600 → 1454 → 169 → 363601 (→ 1454)
#    78 → 45360 → 871 → 45361 (→ 871)
#    540 → 145 (→ 145)
# Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting $
# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

# helper functions

facts = {x: factorial(x) for x in xrange(10)}

def _get_new_num(n):
    return sum([facts[int(x)] for x in str(n)])

st = time.time()
c = 0

for i in xrange(1000000):
    # do updates for shits and gigs
    if (i + 1) % 100000 == 0 and i > 0:
        et = time.time()
        print "c-value := {}\t@ iter := {}\ttime elapsed := {}".format(c, i+1, et-st)

    d = defaultdict(int)
    lst = [i]

    while d.get(lst[-1], None) is None:
        d[lst[-1]] += 1
        n = _get_new_num(lst[-1])
        lst.append(n)

    if len(lst) - 1 == 60:
        c += 1

# c-value := 402
