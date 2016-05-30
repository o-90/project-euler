# -*- coding: utf-8 -*-

# 21)
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n
#which divide evenly into n).  If d(a) = b and d(b) = a, where a ≠ b, then a
#and b are an amicable pair and each of a and b are called amicable numbers.
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
#and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
#142; so d(284) = 220.
#
#Evaluate the sum of all the amicable numbers under 10000.

def factors(n):
    """
    http://stackoverflow.com/questions/6800193/
    what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    """
    try:
        return list(set(reduce(list.__add__,
            ([i, n//i] for i in range(2, int(n**0.5) + 1)
            if n % i == 0))))
    except TypeError:
        return [0]

d = {n: sum([1] + factors(n)) for n in xrange(2, 10000)}

want = []

for k in d.keys():
    amicable = d[k]
    if d.get(amicable, None) == k and amicable != k:
        want.append(amicable)
        want.append(k)

ans = sum(list(set(want)))
print ans  # 31626