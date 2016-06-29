# -*- coding: utf-8 -*-


# 63)
# The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit
# number, 134217728=89, is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?

ans = []

for i in xrange(1, 100):
    ans.extend([x**i for x in xrange(1,1000) if len(str(x**i)) == i])

ans = len(ans)
print ans  # 49
