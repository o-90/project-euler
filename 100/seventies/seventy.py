# -*- coding: utf-8 -*-


# 70)
# Euler's Totient function, φ(n) [sometimes called the phi function], is used
# to determine the number of positive numbers less than or equal to n which
# are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all
# less than nine and relatively prime to nine, φ(9)=6.
#
# The number 1 is considered to be relatively prime to every positive
# number, so φ(1)=1.
#
# Interestingly, φ(87109)=79180, and it can be seen that 87109 is a
# permutation of 79180.
#
# Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and
# the ratio n/φ(n) produces a minimum.


def sundaram3(max_n):
    """
    get primes below n
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

def totientsbelow(N):
    """
    generate number, totient pairs for numbers less than N
    http://stackoverflow.com/questions/1024640/calculating-phik-for-1kn
    """
    allprimes = sundaram3(N+1)
    def rec(n, partialtot=1, min_p = 0):
        for p in allprimes:
            if p > n:
                break

            if p < min_p:
                continue

            yield (p, p-1, [p])

            for t, tot2, r in rec(n//p, partialtot, min_p = p):
                yield (t*p, tot2 * p if p == r[0] else tot2 * (p-1), [p] + r)

    for n, t, factors in rec(N):
        yield (n, t)

def is_permutable(n, m):
    """
    are two numbers permutations of each other
    """
    return sorted(str(m)) == sorted(str(n))


ans = {}

for k, v in totientsbelow(int(1e7)+1):
    if is_permutable(k, v):
        ans[float(k) / float(v)] = k

ans = ans[min(ans.keys())]
print ans  # 8319823
