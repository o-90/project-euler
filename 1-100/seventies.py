# -*- coding: utf-8 -*-


import time
from math import factorial
from collections import defaultdict


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
