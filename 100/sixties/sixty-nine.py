#-*- coding: utf-8 -*-

from __future__ import division
import numpy as np
from primefac import primefac
from collections import OrderedDict

# 69)

# Euler's Totient function, φ(n) [sometimes called the phi function], is used
# to determine the number of numbers less than n which are relatively
# prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine
# and relatively prime to nine, φ(9)=6.
# It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
# Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

func = lambda x: (1 - (1 / x))

dic = {1. / np.prod(list(set(map(func, list(primefac(n)))))): n for n in xrange(1000000, 100000, -2)}
ordered = OrderedDict(sorted(dic.items()))

ans = ordered[ordered.keys()[-1]]
print ans  # 510510