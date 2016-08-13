# -*- coding: utf-8 -*-

from math import ceil


# 87)
# The smallest number expressible as the sum of a prime square, prime cube,
# and prime fourth power is 28. In fact, there are exactly four numbers below
# fifty that can be expressed in such a way:
#
#     28 = 22 + 23 + 24
#     33 = 32 + 23 + 24
#     49 = 52 + 23 + 24
#     47 = 22 + 33 + 24
#
# How many numbers below fifty million can be expressed as the sum of a prime
# square, prime cube, and prime fourth power?


n = 50000000

# prime generator
def sundaram3(max_n):
    """
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
    """
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)

# function to generate prime power triples
def primes_powers(a, b, c):
    return a ** 2 + b ** 3 + c ** 4

# find iteration limits
a_limit = int(ceil(n ** (1./2.)))
a_limit = a_limit if a_limit % 2 == 1 else a_limit + 1

b_limit = int(ceil(n ** (1./3.)))
b_limit = b_limit if b_limit % 2 == 1 else b_limit + 1

c_limit = int(ceil(n ** (1./4.)))
c_limit = c_limit if c_limit % 2 == 1 else c_limit + 1

# get primes less than limits
primes_a = sundaram3(a_limit)[:-1]
primes_b = sundaram3(b_limit)[:-1]
primes_c = sundaram3(c_limit)[:-1]


ans = {}

for a in primes_a:
    for b in primes_b:
        for c in primes_c:
            num = primes_powers(a, b, c)
            if num < 50000000:
                ans[num] = True

ans = sum(ans.values())
print ans  # 1097343
