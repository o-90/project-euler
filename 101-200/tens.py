# -*- coding: utf-8 -*-

from itertools import permutations
from collections import defaultdict

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
