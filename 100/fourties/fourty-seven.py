# -*- coding: utf-8 -8-

from primefac import primefac
from collections import Counter, defaultdict, deque
from Queue import Queue


# 47)
# The first two consecutive numbers to have two distinct prime factors are:
#
#     14 = 2 × 7
#     15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors
# are:
#
#     644 = 2² × 7 × 23
#     645 = 3 × 5 × 43
#     646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime
# factors. What is the first of these numbers?


def distinct_primes(n):
    return list(k ** v for k, v in Counter(primefac(n)).iteritems())

q = deque(maxlen=16)
success = 0

for num in xrange(647, 200000):
    primes = distinct_primes(num)

    if len(primes) != 4:
        q.clear()
        success = 0

    else:
        q.extend(primes)
        success += 1

        if success >= 4:
            if len(set(q)) == len(list(q)):
                break

ans = num - 3
print ans  # 134043
