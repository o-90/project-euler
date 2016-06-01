# -*- coding: utf-8 -*-

from math import factorial

facts = [factorial(x) for x in xrange(0, 10)]

c = 0

for i in xrange(3, 100000):
	if i == sum(facts[int(d)] for d in str(i)):
		c += i

ans = c
print ans  # 40730