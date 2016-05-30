# -*- coding: utf-8 -*-

# 2)
# Find the sum of the even-valued terms in the Fibonacci sequence
# whose value doesn't exceed 4,000,000

fibs = [1,1]

while fibs[-1] < 4000000:
    fibs.append(fibs[-1]+fibs[-2])

ans = sum([x for x in fibs if x % 2 == 0])
print ans  # 4613732