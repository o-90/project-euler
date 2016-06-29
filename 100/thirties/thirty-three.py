# -*- coding: utf-8 -*-

import numpy as np


# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting
# to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained
# by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in
# value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the
# value of the denominator.

def ends_in_zero(n):
    """
    """
    zero = False
    if str(n)[-1] == '0':
        return True
    return False

def first_digits_matches_last(x, y):
    """
    """
    sx = str(x)
    sy = str(y)

    if sx[-1] == sy[0] and float(sx[0]) / float(sy[-1]) == float(x) / float(y) and x != y:
        return True
    return False


# get two digit numbers
lst = [x for x in xrange(10, 100) if not ends_in_zero(x)]

num = []
denom = []

for i in lst:
    for j in lst:
        if first_digits_matches_last(i, j):
            num.append(i)
            denom.append(j)


ans = int(float(np.prod(denom)) / float(np.prod(num)))
print ans  # 100
