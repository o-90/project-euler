#-*- coding: utf-8 -*-

import numpy as np
from primefac import primefac
from collections import OrderedDict

# 65)

# The important mathematical constant,
# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].
# The first ten terms in the sequence of convergents for e are:
# 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
# The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.
# Find the sum of digits in the numerator of the 100th convergent of the
# continued fraction for e.

tmp = [(1, i, 1) for i in xrange(100, 0, -2)]
tmp = [ts for t in tmp for ts in t]
tmp = tmp[-99:]

a = 1
b = tmp[0]

for ts in tmp[1:]:
    a += b * ts
    a, b = b, a

a += b * 2

ans = sum([int(x) for x in str(a)])  # 272

# 69)

# Euler's Totient function, φ(n) [sometimes called the phi function], is used
# to determine the number of numbers less than n which are relatively
# prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine
# and relatively prime to nine, φ(9)=6.
# It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
# Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

func = lambda x: (1 - (1 / x))

dic = 1. / np.prod(list(set(map(func, list(primefac(n)))))): n for n in xrange(1000000, 10, -1)}
ordered = OrderedDict(sorted(dic.items()))

ans = ordered[ordered.keys()[-1]]  # 510510