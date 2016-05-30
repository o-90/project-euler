# -*- coding: utf-8 -*-

# 6)
# Find the difference between the sum of the squares of the first
# 100 natural numners and the square of the sum.

ans = (100*101 / 2)**2 - sum([x**2 for x in xrange(1,101)])
print ans  # 25164160