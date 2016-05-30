# -*- coding: utf-8 -*-

import itertools

# 10)
# Find the sum of the primes less than 2000000

def erat2():
    d = {}
    yield 2

    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = d.pop(q, None)
        if p is None:
            d[q*q] = q
            yield q
        else:
            x = p + q
            while x in d or not (x&1):
                x += p
            d[x] = p

def get_primes_erat(n):
    return list(itertools.takewhile(lambda p: p < n, erat2()))

ans = sum(get_primes_erat(2000000))
print ans  # 142913828922