# -*- coding: utf-8 -*-

from math import log


# 99)
# Comparing two numbers written in index form like 211 and 37 is not difficult,
# as any calculator would confirm that 211 = 2048 < 37 = 2187.
# However, confirming that 632382518061 > 519432525806 would be much more difficult,
# as both numbers contain over three million digits.
# Using base_exp.txt text file containing one thousand lines with a base/exponent pair
# on each line, determine which line number has the greatest numerical value.

f = open("../../data/p099_base_exp.txt", 'r')
base_pairs = [x.strip().split(',') for x in f.readlines()]
d = {e: int(x[1]) * log(int(x[0])) for e, x in enumerate(base_pairs)}
d[max(d.keys())]  # = 708.  Zero-based to add 1.  ans = 709