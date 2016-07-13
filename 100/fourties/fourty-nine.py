# -*- coding: utf-8 -*-


# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways: (i) each of the three terms are
# prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or
# 3-digit primes, exhibiting this property, but there is one other 4-digit
# increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this
# sequence?


def sundaram3(max_n):
    """
    get all primes less than a given quantity
    """
    numbers = range(3, max_n+1, 2)
    half = (max_n) // 2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0

        initial += 2 * (step + 1)
        if initial > half:
            return [2] + filter(None, numbers)

def is_permutation(a, b, c):
    """
    check if three numbers are all permutations
    of each other.
    """
    return sorted(str(a)) == sorted(str(b)) == sorted(str(c))

upper = sundaram3(9999)
lower = sundaram3(1489)

primes = list(set(upper).difference(set(lower)))
dic = {p: True for p in primes}

for ps in primes:
    if dic.get(ps-3330, False) and dic.get(ps+3330):
        if is_permutation(ps-3330, ps, ps+3330):
            ans = str(ps-3330)+str(ps)+str(ps+3330)

print ans  # 296962999629
