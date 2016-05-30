# -*- coding: utf-8 -*-

import numpy as np

# 9)
# A Pythagorean triplet is a set of three natural numbers, a < b < c,
# for which, a**2 + b**2 = c**2
# There exists exactly one Pythagorean triple for which a + b + c = 1000
# Find a*b*c

lst = []
for c in xrange(1,1001):
    for b in xrange(c):
        for a in xrange(b):
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                lst.append((a, b, c))
                break

ans = np.prod(lst)
print ans  # 31875000