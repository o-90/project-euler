# -*- coding: utf-8 -*-

# 4)
# Find the largest palindrome made from the product of two
# 3-digit numbers

tmp = []

for i in xrange(100, 1000):
    for j in xrange(100, 1000):
        prod = i*j
        if str(prod) == str(prod)[::-1]:
            tmp.append(prod)

ans = max(tmp)
print ans  # 906609
