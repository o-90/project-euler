# -*- coding: utf-8 -*-

from itertools import permutations


# 32)
# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
# through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
# multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.


def get_prod(n, k=1):
    """
    """
    str_num = str(n)
    prod = int(str_num[5:])
    if int(str_num[:k]) * int(str_num[k:5]) == prod:
        return prod
    else:
        return 0

perms = [''.join(str(i) for i in x) for x in permutations(range(1, 10), 9)]

ans = []

for k in xrange(1, 5):
    for perm in perms:
        ans.append(get_prod(perm, k))

ans = sum(list(set(ans)))
print ans  # 45228
