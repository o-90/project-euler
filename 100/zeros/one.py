# -*- coding: utf-8 -*-

# 1)
# Find the sum of all the multiples of 3 or 5 below 1000
ans = sum([x for x in xrange(1000) if x % 3 == 0 or x % 5 == 0])
print ans  # 233168