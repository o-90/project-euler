#-*- coding: utf-8 -*-

# 65)
#The important mathematical constant,
#e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].
#
#The first ten terms in the sequence of convergents for e are:
#
#2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
#The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.
#
#Find the sum of digits in the numerator of the 100th convergent of the
#continued fraction for e.

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
