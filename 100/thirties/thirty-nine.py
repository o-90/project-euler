# -*- coding: utf-8 -*-

from collections import defaultdict


# 39)
# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.
#
#     {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?


def triples(m, n, k):
    """
    formula for generating pythagorean triples
    """
    a = k*(m*m-n*n)
    b = k*(2*m*n)
    c = k*(m*m+n*n)

    return (a, b, c)

# create pythagorean triples below 1,000
d = defaultdict(list)
for j in range(1, 100):
    for m in xrange(2, 100):
        for n in xrange(1, m):
            if (m-n) % 2 == 1:
                pt = triples(m, n, j)
                if sum(pt) <= 1000:
                    d[sum(pt)].append(pt)

# reverse dictionary and find the number with max elements
val_to_key = defaultdict(int)
for k, v in d.iteritems():
    val_to_key[len(v)] = k

# find max value
ans = val_to_key[max(val_to_key.keys())]
print ans  # 840
