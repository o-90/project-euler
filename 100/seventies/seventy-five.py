# -*- coding: utf-8 -*-

from collections import defaultdict
from fractions import gcd
from math import ceil


# 75)
# It turns out that 12 cm is the smallest length of wire that can be bent to
# form an integer sided right angle triangle in exactly one way, but there
# are many more examples.
#
#     12 cm: (3,4,5)
#     24 cm: (6,8,10)
#     30 cm: (5,12,13)
#     36 cm: (9,12,15)
#     40 cm: (8,15,17)
#     48 cm: (12,16,20)
#
# In contrast, some lengths of wire, like 20 cm, cannot be bent to form an
# integer sided right angle triangle, and other lengths allow more than one
# solution to be found; for example, using 120 cm it is possible to form
# exactly three different integer sided right angle triangles.
#
#     120 cm: (30,40,50), (20,48,52), (24,45,51)
#
# Given that L is the length of the wire, for how many values of
# L ≤ 1,500,000 can exactly one integer sided right angle triangle be
# formed?


def triples(m, n, k):

    """
    formula for generating pythagorean triples

    constraints:
    ------------
        m > n
        m - n must be odd (i.e. if one is odd the other is even)
        m and n must by coprime.
    """

    a = k*(m*m-n*n)
    b = k*(2*m*n)
    c = k*(m*m+n*n)

    return tuple(sorted([a, b, c]))


def gen(m):
    """
    given m, return a list of possible n that
    could make a pythagorean triple.
    """
    return [x for x in range(1, m) if gcd(x,m) == 1 and (m - x) % 2 == 1]


d = defaultdict(set)

for a in range(2, 870):
    for b in gen(a):
        num = triples(a, b, 1)
        max_k = int(ceil(1500000. / float(sum(num))))
        for k in range(1, max_k):
            trip = triples(a, b, k)
            if sum(trip) <= 1500000:
                d[sum(trip)].add(trip)

ans = sum([True for x in d.values() if len(x) == 1])
print ans  # 161667
