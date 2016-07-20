# -*- coding: utf-8 -*-

from primefac import primefac
from collections import Counter

# 72)
# Consider the fraction, n/d, where n and d are positive integers. If n<d and
# HCF(n,d)=1, it is called a reduced proper fraction.  If we list the set of
# reduced proper fractions for d ≤ 8 in ascending order of size, we get:
#      1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8,
#      2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
# It can be seen that there are 21 elements in this set.  How many elements
# would be contained in the set of reduced proper fractions for d ≤ 1,000,000?

# ----------------------------------------------------------------------------
# NOTE:  It can be shown that the number of reduced proper fractions of type
# n/d where (n, d)=1 is equal to euler phi(d).  This implementation could be
# much faster.  If the search parameters were much more, the phi(n)
# calculations could be cached and used to compute higher values.
# ----------------------------------------------------------------------------


def phi(x):
    """
    Implementation of Euler's Totient function
    """
    fac = Counter(list(primefac(x)))
    result = 1
    for factor in fac:
        result *= (factor-1) * (factor**(fac[factor]-1))

    return result

ans = []
for n in xrange(2, 1000001):
    ans.append(phi(n))

ans = sum(ans)
print ans  # 303963552391
